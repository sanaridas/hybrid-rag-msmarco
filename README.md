# Hybrid-RAG MS MARCO Benchmark

This repository contains code and experiments for a hybrid BM25 / dense / fusion
retrieval benchmark on the MS MARCO passage dataset, including:

- Sparse BM25 baselines (Pyserini/Lucene)
- Dense retrieval with Sentence-Transformers + FAISS
- Hybrid score fusion and Reciprocal Rank Fusion (RRF)
- Reproducible configs, scripts, and analysis notebooks

See `notebooks/` for exploratory analysis and `scripts/` for end-to-end pipelines.
