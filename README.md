# GraphSWE submission package

This package is a submission-oriented, evidence-bounded draft for the Gemma 4 Developer Agent Paper Track.

## Contents
- `Kaggle_Writeup.md` — paper draft structured around the required sections.
- `analysis/score_rank_table.py` — utility to calculate MRR and Hit@K from a user-supplied per-task rank CSV.
- `analysis/rank_table_template.csv` — input schema template, intentionally header-only.
- `PROTOCOL_AND_GATES.md` — remaining scientific gates and decision rules.
- `PRIOR_ART_SUMMARY.md` — bounded prior-art comparison and novelty guardrails.
- `SHA256SUMS.txt` — integrity hashes for package files.

## Scientific status
This package does not close graph provenance, exact-revision edge semantics, held-out label eligibility, or novelty. It does not rerun the frozen 17-task evaluator. Aggregate results are transcribed from existing project reports. The included script is a reusable analysis utility, not proof that the original experiment has been reproduced.

## Kaggle submission checklist
1. Create a new Kaggle Writeup in the official Paper Track.
2. Paste `Kaggle_Writeup.md` into the writeup editor and check its word count.
3. Verify every reference and final venue requirements.
4. If sharing code, publish the script and protocol in a public repository or public Kaggle notebook accessible without login/paywall.
5. State that the result is exploratory and graph provenance remains unresolved.
6. Submit the Writeup explicitly before the official deadline; a saved draft is not a submission.

Official page: https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/overview/submission-requirements
