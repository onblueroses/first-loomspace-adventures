"""
M1 — Embedding distribution shape analysis for a headline run.

For each cell, embed all 200 completions with sentence-transformers, then compute:
  - per-cell centroid
  - cross-cell centroid distances (cosine), pairwise within each tradition group
  - within-cell median pairwise cosine distance (spread)
  - multimodality: BIC for GaussianMixture k=1..5 (PCA-reduced to 50 dims first)

Output: writes results/<run-id>/embedding_shape.json + prints summary.

Usage:
    python src/embed_shape.py results/headline-2026-05-30-deepseek
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer  # type: ignore[import-not-found]
from sklearn.decomposition import PCA  # type: ignore[import-not-found]
from sklearn.mixture import GaussianMixture  # type: ignore[import-not-found]


REPO_ROOT = Path(__file__).resolve().parent.parent
MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # 90MB, fast, 384-dim


def cosine_centroid_dist(a: np.ndarray, b: np.ndarray) -> float:
    ca = a.mean(axis=0)
    cb = b.mean(axis=0)
    return float(1 - np.dot(ca, cb) / (np.linalg.norm(ca) * np.linalg.norm(cb)))


def within_cell_spread(X: np.ndarray, sample_pairs: int = 500) -> float:
    n = len(X)
    if n < 2:
        return 0.0
    norms = X / np.linalg.norm(X, axis=1, keepdims=True)
    rng = np.random.default_rng(0)
    idx = rng.integers(0, n, size=(min(sample_pairs, n * (n - 1) // 2), 2))
    idx = idx[idx[:, 0] != idx[:, 1]]
    cos = (norms[idx[:, 0]] * norms[idx[:, 1]]).sum(axis=1)
    return float(np.median(1 - cos))


def gmm_bic_scan(X: np.ndarray, k_max: int = 5) -> dict:
    if len(X) < k_max:
        return {"k_best": 1, "bic_curve": []}
    pca = PCA(n_components=min(50, len(X) - 1, X.shape[1]))
    Xr = pca.fit_transform(X)
    bics = []
    for k in range(1, k_max + 1):
        gmm = GaussianMixture(n_components=k, random_state=0, max_iter=200)
        try:
            gmm.fit(Xr)
            bics.append((k, float(gmm.bic(Xr))))
        except Exception:  # noqa: BLE001
            bics.append((k, float("inf")))
    k_best = min(bics, key=lambda kv: kv[1])[0]
    return {"k_best": k_best, "bic_curve": bics}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("run_dir", type=str)
    args = p.parse_args()
    run_dir = Path(args.run_dir).resolve()

    completions_root = run_dir / "completions"
    cells = sorted([p for p in completions_root.glob("*/*") if p.is_dir()])
    if not cells:
        sys.exit(f"no cells in {completions_root}")

    print(f"[embed] loading model {MODEL}", flush=True)
    model = SentenceTransformer(MODEL)

    out: dict = {"run_id": run_dir.name, "model": MODEL, "cells": {}}
    cell_embs: dict[str, np.ndarray] = {}

    for cell_dir in cells:
        cell_key = f"{cell_dir.parent.name}/{cell_dir.name}"
        files = sorted(cell_dir.glob("*.txt"))
        texts = [f.read_text() for f in files if f.stat().st_size > 5]
        if not texts:
            continue
        print(f"[embed] {cell_key}: {len(texts)} completions", flush=True)
        # truncate to ~512 tokens-ish
        texts = [t[:2000] for t in texts]
        X = model.encode(texts, batch_size=64, show_progress_bar=False)
        cell_embs[cell_key] = X
        spread = within_cell_spread(X)
        gmm = gmm_bic_scan(X)
        out["cells"][cell_key] = {
            "n": len(texts),
            "centroid_norm": float(np.linalg.norm(X.mean(axis=0))),
            "spread_cos": spread,
            "k_best": gmm["k_best"],
            "bic_curve": gmm["bic_curve"],
        }

    # Pairwise cross-cell cosine distance between centroids.
    cell_keys = sorted(cell_embs.keys())
    out["pairwise_centroid_cos"] = {}
    for i, k1 in enumerate(cell_keys):
        for k2 in cell_keys[i + 1 :]:
            out["pairwise_centroid_cos"][f"{k1}__vs__{k2}"] = cosine_centroid_dist(
                cell_embs[k1], cell_embs[k2]
            )

    (run_dir / "embedding_shape.json").write_text(json.dumps(out, indent=2))
    print(f"\n[embed] wrote {run_dir / 'embedding_shape.json'}")

    # Print headline comparisons
    print("\n=== Per-cell embedding profile ===")
    print(f"{'Cell':45s} {'n':>4} {'spread':>8} {'k_best':>7}")
    for ck in cell_keys:
        c = out["cells"][ck]
        print(f"  {ck:45s} {c['n']:4d} {c['spread_cos']:8.3f} {c['k_best']:>7d}")

    print("\n=== Key cross-cell centroid distances (L_real vs controls, per tail) ===")
    interesting = [
        ("astrachios/visitor_at_door", "astrachios_denamed/visitor_at_door"),
        ("astrachios/visitor_at_door", "astrachios_nonsense/visitor_at_door"),
        ("astrachios/visitor_at_door", "astrachios_random/visitor_at_door"),
        ("astrachios/visitor_at_door", "empty/visitor_at_door"),
        ("astrachios/page_continues", "astrachios_denamed/page_continues"),
        ("headless/visitor_at_door", "headless_denamed/visitor_at_door"),
        ("headless/visitor_at_door", "headless_nonsense/visitor_at_door"),
        ("headless/visitor_at_door", "headless_random/visitor_at_door"),
        ("headless/page_continues", "headless_denamed/page_continues"),
        ("astrachios/visitor_at_door", "headless/visitor_at_door"),
    ]
    for a, b in interesting:
        key = f"{a}__vs__{b}" if a < b else f"{b}__vs__{a}"
        d = out["pairwise_centroid_cos"].get(key)
        if d is not None:
            print(f"  {a:42s} ↔ {b:42s}  cos_dist={d:.4f}")


if __name__ == "__main__":
    main()
