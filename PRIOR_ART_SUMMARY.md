# Prior-Art Summary (bounded, not systematic)

| Work | What it establishes | Implication | Limit of this audit |
|---|---|---|---|
| LocAgent (ACL 2025) — https://aclanthology.org/2025.acl-long.426/ | Directed heterogeneous repository graphs and graph-guided multi-hop code localization. | Graph-guided localization is prior art; graph usage alone is not novel. | Does not prove whether every displacement diagnostic here is already covered. |
| SpIDER (arXiv:2512.16956) — https://arxiv.org/abs/2512.16956 | Dense retrieval combined with LLM reasoning over graph-explored context. | Graph exploration and retrieval integration are prior art. | Full text/supplement and exact-version comparison still needed. |
| FuseSearch (Findings ACL 2026) — https://aclanthology.org/2026.findings-acl.143/ | Adaptive parallel search breadth and joint quality/efficiency optimization. | Efficiency-aware adaptive search is prior art; budget awareness alone is not novel. | Earlier local code audit sampled selected functions and is not a complete implementation audit. |
| ARISE (local audit copy) | Bounded traversal and token-budgeted context packing in inspected functions. | Bounded graph traversal and context packing are prior art. | Upstream URL/revision and local-copy provenance need verification before publication. |
| SpIDER implementation audit | Inspected code includes graph-neighbor expansion, filtering, and usage/budget tracking. | Fixed-budget graph expansion is not the contribution. | Exact repository URL/commit from the earlier audit still needs to be attached. |

## Safe novelty statement
No novelty claim is made. The current defensible contribution is an exploratory report of a small frozen comparison plus explicit provenance/eligibility caveats and a reusable rank-table analysis utility. A prospective predictor of harmful displacement is a future hypothesis, not a result.
