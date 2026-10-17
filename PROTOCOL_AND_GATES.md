# Protocol and Remaining Gates

## Frozen decisions
- Preserve the original 17-task pilot and protected CSVs unchanged.
- Treat supplied graph JSONs as fixed, unverified artifacts.
- Do not score disputed historical held-out tasks as confirmatory.
- Do not claim a trained pre-expansion harm predictor, causal mechanism, statistical significance, or established novelty.
- Report aggregate pilot values exactly as recorded.

## Current reported result
| Policy | Tasks | MRR | Hit@1 | Hit@5 | Hit@10 | Hit@20 |
|---|---:|---:|---:|---:|---:|---:|
| BM25 top-20 | 17 | 0.214651 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |
| Fixed expansion | 17 | 0.212990 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |
| Conservative expansion | 17 | 0.213717 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |

Recorded target-rank movement among comparable cases: fixed expansion 0 improved / 3 worsened; conservative expansion 0 improved / 1 worsened.

## Gates not closed
1. **Graph provenance:** original builder, revision, configuration, dependencies, and graph-to-source mapping not established.
2. **Relation semantics:** the `calls` label has not been independently verified against exact source revisions.
3. **Held-out eligibility:** four historical tasks remain excluded pending independent review.
4. **Label adjudication:** two target discrepancies in the broader audit require independent adjudication; original labels must remain unchanged until then.
5. **Prior art:** implementation-level review is partial, not a novelty proof.
6. **Confirmatory evaluation:** not authorized by the existing project record.

## Acceptable paths forward
- Keep the paper as a provenance-aware exploratory diagnostic report.
- Or build a new, separate dataset from exact source commits using an independently documented graph generator. Clearly label these as newly generated graphs, not reproductions of the supplied artifacts.
- Do not describe a new graph as a reproduction without structural and relation-level comparison.

## Pre-expansion predictor — future work only
If pursuing a predictor later, features must be observable before expansion. Candidate examples include seed-list concentration, graph-neighbor count, fraction of neighbors already in the retrieval pool, rank distribution of eligible neighbors, and estimated number of baseline candidates that would be displaced. Exclude target labels, post-expansion rankings, and outcome-derived features. Evaluate with repository-separated splits, simple baselines, calibration, uncertainty, and a preregistered rejection rule. These features are proposals, not tested findings in this package.
