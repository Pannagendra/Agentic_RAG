import argparse, json, os
import numpy as np
from pathlib import Path
from scipy.spatial.distance import jensenshannon
from scipy.stats import entropy
from sentence_transformers import SentenceTransformer

MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

def embed(texts):
    m = SentenceTransformer("all-MiniLM-L6-v2")
    vecs = m.encode(texts, normalize_embeddings=True)
    return np.array(vecs)

def vector_hist(vecs, bins=30):
    hist, _ = np.histogram(vecs.flatten(), bins=bins, range=(-1,1), density=True)
    return hist + 1e-12

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=False, help="(optional) path to FAISS meta to read texts", default="data/processed/index.meta.json")
    ap.add_argument("--baseline", required=True)
    args = ap.parse_args()

    meta_path = Path(args.index).with_suffix(".meta.json") if str(args.index).endswith(".faiss") else Path(args.index)
    texts = [j["text"] for j in json.loads(meta_path.read_text())]

    vecs = embed(texts)
    hist = vector_hist(vecs)

    baseline_path = Path(args.baseline)
    if not baseline_path.exists():
        baseline = {"hist": hist.tolist()}
        baseline_path.write_text(json.dumps(baseline, indent=2))
        print("[baseline created] saved to", baseline_path)
        raise SystemExit(0)

    baseline = json.loads(baseline_path.read_text())
    h0 = np.array(baseline["hist"])
    h1 = hist

    jsd = jensenshannon(h0, h1)
    kl = float(entropy(h1, h0))

    print({"embedding_jsd": float(jsd), "embedding_kl": kl})

    if jsd > 0.15:
        print("[ALERT] Embedding distribution drift detected (JSD>", 0.15, ")")
