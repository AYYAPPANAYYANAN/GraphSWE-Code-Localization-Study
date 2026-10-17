# Fixed-Budget Graph Expansion Does Not Improve a Small Function-Localization Pilot
## A Provenance-Aware Diagnostic of Candidate Displacement in Repository Retrieval

**Submission type:** Exploratory empirical report and reproducibility resource. Results below are transcribed from frozen project artifacts and were not independently rerun in this package.

## Abstract

Code-localization systems often expand lexical or semantic retrieval results with repository-graph neighbors. This can surface structurally related code, but under a fixed candidate budget it can also replace candidates supported by the initial ranking. We report an exploratory comparison of BM25 top-20 retrieval with two existing graph-expansion policies on a frozen 17-task function-localization pilot. Mean reciprocal rank (MRR) was 0.214651 for BM25, 0.212990 for fixed expansion, and 0.213717 for conservative expansion. All three policies had identical reported Hit@1, Hit@5, Hit@10, and Hit@20 values. In the available task-level displacement audit, fixed expansion worsened three target ranks and improved none; conservative expansion worsened one and improved none among cases with both ranks available. These observations are small-sample and descriptive: they do not establish that graph expansion is generally harmful, nor do they demonstrate a causal mechanism or a validated predictor of harmful expansion. The supplied graph-generation provenance and exact-revision edge semantics remain unverified, while several historical held-out tasks have unresolved eligibility or label conflicts and are excluded from confirmatory interpretation. We contribute a transparent account of this bounded result, explicit claim limits, and a machine-readable evaluation protocol for future source-aligned studies. The main finding is methodological: aggregate retrieval scores alone are insufficient to explain expansion behavior, and graph provenance, target availability, rank displacement, and label eligibility must be reported separately.

## 1. Introduction

Automated software-engineering agents must identify code entities relevant to an issue before inspecting, modifying, or testing them. Lexical retrieval such as BM25 is inexpensive and provides a useful baseline. Repository graphs can encode relationships among functions, classes, files, and dependencies, enabling search beyond the initially retrieved candidates. Recent systems demonstrate that graph-guided localization and adaptive search are active research directions, including LocAgent, SpIDER, and FuseSearch [1–3].

However, graph expansion changes the candidate pool. When the final list is capped at a fixed size, adding neighbors can push out candidates already retrieved by lexical evidence. This motivates a narrow question: **on the available frozen pilot, did two existing graph-expansion policies improve function-localization ranking over BM25, and what does the recorded candidate displacement reveal?**

This paper does not introduce graph expansion as a new method. It does not claim to train or validate a prospective harm predictor. Instead, it documents an exploratory, non-improving pilot and the limits imposed by incomplete graph provenance and unresolved historical evaluation conflicts.

### Contributions

1. A compact report of the existing frozen 17-task comparison among BM25 top-20, fixed expansion, and conservative expansion.
2. A descriptive account of target-rank changes and candidate-list displacement under a fixed output budget.
3. An explicit provenance and eligibility statement that prevents supplied graph artifacts from being mistaken for independently verified source-level call graphs.
4. A reusable evaluation schema and analysis script for future task-level rank tables.

## 2. Related Work

LocAgent builds directed heterogeneous repository graphs and uses graph-guided multi-hop reasoning for code localization [1]. SpIDER combines dense retrieval with LLM reasoning over context obtained through graph exploration, directly establishing graph-based expansion as prior art [2]. FuseSearch studies adaptive parallel search breadth as a quality–efficiency optimization problem and adjusts search behavior to avoid redundant tool calls [3]. These works make it indefensible to claim novelty from graph traversal, candidate expansion, or budget-aware search alone.

The present report differs in scope rather than claiming a new algorithm: it records a small BM25-versus-expansion pilot, reports associated rank changes, and makes data-provenance uncertainty part of the result interpretation. This is not a completed systematic review and does not establish that prior work omits similar diagnostics. The implementation-level comparison completed so far is partial; therefore, no novelty claim is made for a prospective harmfulness predictor or for candidate displacement analysis itself.

## 3. Research Questions

- **RQ1:** Did the two existing expansion policies improve aggregate top-k localization metrics over BM25 on the frozen pilot?
- **RQ2:** Among tasks with comparable target ranks, how many target ranks improved or worsened?
- **RQ3:** Which conclusions are blocked by unresolved graph provenance, relation semantics, label eligibility, and prior-art coverage?

## 4. Methods

### 4.1 Evaluation scope

The primary set consists of 17 tasks from the project's frozen evaluation artifacts. Results in this paper are transcribed from existing reports; this package does not rerun the evaluator or modify frozen labels. Historical held-out tasks with unresolved eligibility or label conflicts are not treated as confirmatory evidence.

### 4.2 Compared policies

- **BM25 top-20:** lexical baseline returning the top 20 retrieval candidates.
- **Fixed expansion:** starts from the top 10 BM25 candidates and expands using the supplied graph relation labelled `calls`, with the recorded lexical-pool cutoff of 100.
- **Conservative expansion:** uses the same recorded setup but a lexical-pool cutoff of 50.

The recorded implementation treats the supplied `calls` relation as undirected, restricts expanded candidates to nodes present in the retrieval corpus, selects candidates in BM25-rank order, and fills remaining slots from the baseline list until the 20-candidate budget is reached. These are implementation descriptions, not endorsements of the relation's semantic correctness. The original graph builder, exact generation configuration, and source-revision-to-graph mapping have not been independently established.

### 4.3 Metrics and displacement audit

The primary reported metric is mean reciprocal rank (MRR). Secondary metrics are Hit@1, Hit@5, Hit@10, and Hit@20. Values are retained from the frozen reports and are not recalculated from raw task-level ranks. The absolute MRR differences from BM25 are −0.001661 for fixed expansion and −0.000934 for conservative expansion. These descriptive differences are not claimed to be statistically significant.

The existing audit compares target ranks when both baseline and expanded ranks are available and records candidates introduced or displaced from the bounded list. Counts below are occurrence counts, not necessarily unique functions. Namespace/name-based categories (including test-like names) are heuristics; they do not prove leakage, semantic correctness, or causation.

### 4.4 Provenance and eligibility

The project inventory reports 127 supplied graph files and 452,588 parsed edges, with every parsed edge labelled `calls`. Structural parse success and file presence do not establish how graphs were generated or whether their edges match source-level call relationships at the exact task revision. In the existing provenance audit, independent generation provenance and exact-revision edge semantics were established for 0 of 30 examined candidate tasks. A separately reconstructed graph for one sampled repository differed substantially from the supplied graph, so it cannot be treated as a reproduction of the original builder.

Four historical held-out tasks remain excluded pending independent audit because of eligibility, label-review, or prior-exposure conflicts. No new confirmatory scoring is authorized by the current project record. These exclusions are not silently treated as negative retrieval outcomes.

## 5. Results

### 5.1 Aggregate metrics

| Policy | Tasks | MRR | Hit@1 | Hit@5 | Hit@10 | Hit@20 |
|---|---:|---:|---:|---:|---:|---:|
| BM25 top-20 | 17 | 0.214651 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |
| Fixed expansion | 17 | 0.212990 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |
| Conservative expansion | 17 | 0.213717 | 0.176471 | 0.235294 | 0.294118 | 0.470588 |

Neither expansion policy improved the reported aggregate hit-rate metrics. MRR was slightly lower for both expansion policies. The result is bounded to this frozen sample and these specific policies; it does not establish a general property of graph-based retrieval.

### 5.2 Target-rank movement

| Policy | Improved | Worsened | Interpretation |
|---|---:|---:|---|
| Fixed expansion | 0 | 3 | No improvements recorded among comparable cases |
| Conservative expansion | 0 | 1 | No improvements recorded among comparable cases |

These counts apply only where both ranks were available. They should not be interpreted as counts across every task or label state. The small sample does not support a broad performance claim.

### 5.3 Candidate-list changes

| Policy | Candidate occurrences introduced | Test-named introduced occurrences | Candidate occurrences displaced |
|---|---:|---:|---:|
| Fixed expansion | 122 | 11 | 122 |
| Conservative expansion | 85 | 3 | 85 |

The existing audit reports zero eligible-target occurrences among introduced candidates for both policies. These are occurrence counts, not unique symbols. A test-like namespace is only a heuristic category and is not evidence of data leakage. Displacement indicates that the candidate list changed; it does not by itself establish why a target rank changed or whether any individual added candidate caused the change.

## 6. Discussion

The pilot provides no evidence that the two tested expansion policies improve the reported aggregate top-k metrics over BM25. The lower MRR values and observed target-rank changes are consistent with the possibility that expansion can consume a fixed candidate budget without adding a useful target. They do not prove that mechanism, and they do not show that graph expansion is generally harmful. A different graph, seed ranking, edge direction, candidate budget, or expansion policy may behave differently.

Three evidence layers must remain separate: (1) ranking behavior reported by the frozen evaluation; (2) graph validity—whether supplied edges correspond to meaningful relations at the exact source revision; and (3) label and task validity—whether the target existed at the base revision, was eligible for localization, and was adjudicated independently of rankings. The first layer has a recorded exploratory result. The second and parts of the third remain unresolved. Therefore, the paper does not use the supplied graph relation as ground truth and does not interpret excluded historical held-out results as confirmation.

A natural next hypothesis is that target availability, reachability from initial lexical seeds, and the amount of candidate displacement may help explain when expansion helps or hurts. That hypothesis has **not** been tested here as a predictive model. A valid predictive study would need pre-expansion features only, repository-separated evaluation, a predeclared target and threshold, and held-out labels independent of ranking outcomes. It would also need a broader implementation-level comparison with closest prior work before making a novelty claim.

## 7. Limitations

1. **Small sample:** 17 tasks are insufficient for broad generalization or reliable subgroup claims.
2. **No confirmatory rerun:** results are reported from frozen artifacts and were not independently regenerated in this package.
3. **Graph provenance unresolved:** the original builder, configuration, and exact graph-to-source mapping are unavailable in the current evidence.
4. **Relation semantics unresolved:** all parsed edges are labelled `calls`, but this label has not been independently verified at the exact source revision.
5. **Historical held-out conflicts:** four tasks remain excluded pending independent eligibility and label review.
6. **Partial prior-art audit:** the literature and implementation comparison is not systematic or exhaustive.
7. **No predictor evaluation:** no trained or calibrated pre-expansion harmfulness predictor is reported.
8. **Descriptive displacement:** candidate counts do not prove causal mechanisms; name-based classifications do not prove leakage.
9. **No statistical-significance claim:** no inferential claim is made from the reported aggregate differences.

## 8. Reproducibility and Future Work

The release should retain frozen result tables and their hashes, task-level audit outputs, the exact configuration used by the original run, and provenance limitations. The included analysis script accepts a CSV containing task identifiers and target ranks for baseline and each policy; it recomputes descriptive rank metrics from that supplied table. It does not recreate original graph artifacts or claim to reproduce the reported experiment unless the correct task-level input is supplied.

A future confirmatory study should: (1) obtain the authoritative graph builder and configuration or regenerate graphs at exact source commits; (2) compare nodes, edges, relation types, direction, and attributes; (3) adjudicate targets against base-revision patches before inspecting rankings; (4) define inclusion/exclusion rules and budgets before evaluation; (5) separate training, validation, and test repositories if a predictor is developed; and (6) report paired per-task differences and uncertainty intervals. If these conditions cannot be met, the work should remain an exploratory diagnostic resource.

## 9. Conclusion

On the frozen 17-task pilot, neither tested graph-expansion policy improved the reported aggregate Hit@K metrics over BM25, and both had slightly lower MRR. The displacement audit recorded no target-rank improvements among comparable cases, but these observations are descriptive and do not establish causality or generalize beyond the sample. Unresolved graph provenance, relation semantics, held-out eligibility, and incomplete prior-art review prevent stronger claims. The defensible contribution is a transparent report of the bounded pilot, its failure to show improvement under the tested setup, and a protocol for conducting a more rigorous source-aligned evaluation.

## References

[1] Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, and Xingyao Wang. 2025. “LocAgent: Graph-Guided LLM Agents for Code Localization.” *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics*, 8697–8727. https://aclanthology.org/2025.acl-long.426/

[2] Shravan Chaudhari, Rahul Thomas Jacob, Mononito Goswami, Jiajun Cao, Shihab Rashid, and Christian Bock. 2025. “SpIDER: Spatially Informed Dense Embedding Retrieval for Software Issue Localization.” arXiv:2512.16956. https://arxiv.org/abs/2512.16956

[3] Ke Xu, Siyang Xiao, Ming Liang, Yichen Yu, Zhixiang Wang, Jingxuan Xu, Dajun Chen, Wei Jiang, and Yong Li. 2026. “FuseSearch: Learning Adaptive Parallel Execution for Efficient Code Localization.” *Findings of the Association for Computational Linguistics: ACL 2026*, 2954–2967. https://aclanthology.org/2026.findings-acl.143/

[4] “The Gemma 4 Developer Agent Paper Track — Submission Requirements.” Kaggle. https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/overview/submission-requirements
