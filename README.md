# Hybrid-RAG MS MARCO Benchmark

This repository contains code and experiments for a hybrid BM25 / dense / fusion
retrieval benchmark on the MS MARCO passage dataset, including:

- Sparse BM25 baselines (Pyserini/Lucene)
- Dense retrieval with Sentence-Transformers + FAISS
- Hybrid score fusion and Reciprocal Rank Fusion (RRF)
- Reproducible configs, scripts, and analysis notebooks

See `notebooks/` for exploratory analysis and `scripts/` for end-to-end pipelines.

Here’s a concrete “this is how I’d use it every day” workflow for your Git Control Center notebook.

---

## 1. First-time setup (one-off)

1. **Open the notebook in Colab**

   * Use “Open from GitHub” or upload it to Drive and open it from there.

2. **Run `Project & GitHub configuration` (Cell 1)**

   * Make sure:

     * `PROJECT_NAME = "hybrid-rag-msmarco"`
     * `GITHUB_REPO_URL` points to your repo
       (currently `https://github.com/sanaridas/hybrid-rag-msmarco.git`)
     * `DRIVE_BASE_DIR` is where you want your projects (e.g. `/content/drive/MyDrive/projects`).
   * Run the cell, check the printed config to avoid path typos.

3. **Set global Git identity (Cell 2)**

   * Run the cell that does:

     ```bash
     git config --global user.email "..."
     git config --global user.name "..."
     ```
   * This is one-time per Colab account (unless you change identity).

4. **Mount Google Drive (Cell 3)**

   * Run the “Mount Google Drive” cell.
   * Confirm Drive is mounted at `/content/drive`.
   * Your repo will live under something like:

     ```text
     /content/drive/MyDrive/projects/hybrid-rag-msmarco
     ```

5. **Clone or prepare the repo (Cell 4 / scaffolding cell)**
   Rough idea of what this cell is for:

   * If `PROJECT_DIR` doesn’t exist:

     * `git clone` the repo into `BASE_DIR / PROJECT_NAME`.
     * Optionally scaffold files (e.g. `src/`, `scripts/`, `.github/workflows/`).
   * If it *does* exist:

     * `git pull` to update from `origin/main`.
   * After running, verify:

     ```bash
     ls /content/drive/MyDrive/projects/hybrid-rag-msmarco
     ```

6. **Install Python dependencies (Cell 6)**

   * Run the “Install Python dependencies (editable install if possible)” cell.
   * It will:

     * Look for `pyproject.toml` / `setup.cfg` / `setup.py` / `requirements.txt`.
     * Run `pip install -e .` when possible (so changes in `src/` are picked up without reinstall).
   * Let it finish; this is the base environment for all your later notebooks.

7. **Configure `src/` on `sys.path` (Cell 5)**

   * Run the “Configure Python path for src/ package” cell.
   * It should print something like:

     ```text
     Added to sys.path: /content/drive/MyDrive/projects/hybrid-rag-msmarco/src
     ```
   * After this, you can `import hybrid_rag_benchmark` (or whatever you set as `PYTHON_PACKAGE_NAME`).

After this first session, your Drive and repo are wired up. Future sessions are simpler.

---

## 2. Typical daily session

Every time you start a new Colab runtime and want to work on the project:

1. **Open the Control Center notebook.**

2. **Run these cells top-down:**

   1. `Project & GitHub configuration`
   2. `Mount Google Drive`
   3. (Optional) `Clone or update GitHub repo` if you want to force a fresh `git pull`
   4. `Install Python dependencies` (fast if already installed; Colab runtimes are ephemeral)
   5. `Configure Python path for src/ package`

3. **Check repo state with the git status / monitor cell (Cell 14 + your monitor cell)**

   * Run the cell with:

     ```bash
     git status -sb
     ```
   * And your “git monitor” cell (the one that periodically prints changed files).
   * Use this as your “mini-IDE gutter” to see:

     * `M` = modified files
     * `??` = untracked files
   * Re-run it after editing notebooks or code to get a quick diff signal.

4. **Navigate structure (optional)**

   * Run the `tree` cell:

     ```bash
     !tree /content/drive/MyDrive/projects/hybrid-rag-msmarco
     ```
   * Use this to remind yourself where scripts, configs, and notebooks live (e.g. `src/`, `scripts/`, `notebooks/`, `configs/`).

---

## 3. Doing actual work (experiments, notebooks, scripts)

Once the environment is ready:

1. **Open experiment notebooks from the repo**

   * In the left Colab file browser, navigate to:

     ```
     /content/drive/MyDrive/projects/hybrid-rag-msmarco
     ```
   * Open the relevant notebook from `notebooks/` (e.g. `notebooks/dense_retriever_100k.ipynb`, `notebooks/bm25_100k.ipynb`, etc.).
   * Those notebooks will:

     * Assume the environment and paths you set up in the Control Center.
     * Import your `src/` code (thanks to `sys.path` / editable install).

2. **Run scripts via helper cells (if you add them)**

   * You can keep small launcher cells in the Control Center, e.g.:

     ```python
     # Run an indexing script
     !python scripts/index_dense_100k.py --config configs/dense_100k.yaml
     ```
   * Or:

     ```python
     # Run evaluation
     !python scripts/eval_bm25_vs_dense.py --config configs/eval_100k.yaml
     ```

3. **Edit code in `src/` and configs in `configs/`**

   * Use Colab’s text editor (or VS Code on your local machine synced to the same repo).
   * Because of `pip install -e .` and the `sys.path` tweak:

     * Changes in `src/` are immediately visible to notebooks without reinstall.

4. **Use the git monitor cell as you work**

   * After you change notebooks, scripts, or configs:

     * Re-run the monitor/status cell.
     * This gives you a quick overview of what will go into the next commit.

---

## 4. Committing and pushing changes

Once you’ve made a meaningful set of changes:

1. **Check status first**

   * Run the git status / monitor cell:

     ```bash
     !git status -sb
     ```
   * Decide what should go into this commit (e.g. new notebook, modified script, updated config).

2. **Stage and commit (you can do it in a single Control Center cell)**
   Typical pattern (either from an existing cell or a new one you add):

   ```bash
   !git add -A
   !git status -sb  # optional double-check

   commit_message = "Add dense retriever 100k experiments"  # edit per change
   !git commit -m "{commit_message}"
   ```

3. **Push with PAT (Push helper cell)**

   * Run the push helper cell that:

     * Asks for your GitHub PAT via `getpass`.
     * Builds the authenticated remote URL.
     * Runs:

       ```bash
       git push --set-upstream <auth_url> main
       ```
   * You do **not** store the PAT in the notebook; you paste it when prompted.

4. **Confirm clean working tree**

   * Re-run `!git status -sb`.
   * You want to see:

     ```text
     ## main...origin/main
     nothing to commit, working tree clean
     ```

Now your Drive copy and GitHub are in sync, and the next time you open the Control Center, you’ll `git pull` any changes you made from another machine.

---

## 5. How the Control Center fits into your overall workflow

Very concretely, a “day in the life” with this notebook looks like:

1. Open Control Center in Colab.
2. Run: config → mount Drive → (optional) clone/pull → install deps → configure `src/`.
3. Run git monitor/status cell → see current state of repo.
4. Open experiment notebooks in `notebooks/` and run/edit them.
5. Keep re-running the git monitor/status cell as you change files.
6. When you’re done:

   * `git add -A`
   * `git commit -m "..."`
   * Run the PAT-based push cell.
7. Close the session; all code + notebooks are safely in Drive + GitHub.

If you want, next step I can sketch a tiny “Run this every session” checklist cell at the top of the notebook that prints these steps as a reminder.

