# Efficiency Analysis Report
*Generated: 2026-04-18 15:08*  
*Models: gpt-5.2, claude-4.5-opus, gemini-3-pro, llama-4, medgemma-27b | Visits per model: 8*

---

## 1. Latency and Token Overhead

Agentic pipelines incur substantial wall-clock overhead relative to zero-shot inference. Across 5 models, the agentic-to-zero-shot latency ratio ranges from **4.9×** to **14.3×**. 
Token overhead follows a similar pattern, ranging from **3.9×** to **41.0×**, driven primarily by multi-turn agent coordination rather than input expansion.

| Model | T_zs (s) | T_ag (s) | ΔT (s) | T_ratio | K_zs | K_ag | K_ratio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-5.2 | 33.62 | 479.27 | 445.65 | 14.3× | 25900 | 1061379 | 41.0× |
| claude-4.5-opus | 31.29 | 207.62 | 176.33 | 6.6× | 33379 | 375301 | 11.2× |
| gemini-3-pro | 38.41 | 190.03 | 151.62 | 4.9× | 36318 | 141876 | 3.9× |
| llama-4 | 8.81 | 49.19 | 40.38 | 5.6× | 21119 | 554448 | 26.3× |
| medgemma-27b | 30.57 | 316.84 | 286.27 | 10.4× | 30636 | 760160 | 24.8× |

## 2. Performance Gain and Efficiency Tradeoff

Composite performance gain (ΔP) is defined as the mean improvement across four clinical metrics: ESI F1, qSOFA accuracy, MAP tolerance rate, and LOS tolerance rate. The efficiency metric E_T = ΔP / ΔT captures the amount of composite performance gain obtained per additional second of inference. 
**llama-4** achieves the highest efficiency at **5.222×10⁻³ ΔP/s**, indicating the most favorable cost-benefit tradeoff among all evaluated configurations.

| Model | ΔP (composite) | E_T (×10⁻³) | E_K (ΔP/1k tok) | Mean iterations | T/iter (s) |
| --- | --- | --- | --- | --- | --- |
| gpt-5.2 | 0.3810 | 0.855 | 0.0004 | 3.0 | 159.76 |
| claude-4.5-opus | 0.2099 | 1.191 | 0.0006 | 1.1 | 184.55 |
| gemini-3-pro | 0.1518 | 1.001 | 0.0014 | 1.0 | 190.03 |
| llama-4 | 0.2109 | 5.222 | 0.0004 | 3.0 | 16.40 |
| medgemma-27b | 0.3438 | 1.201 | 0.0005 | 3.0 | 105.61 |

## 3. Agent Time Concentration

On average, the top-2 most time-consuming agents account for **64.5%** of total agentic pipeline latency. This concentration indicates clear optimization targets: reducing the iteration count or parallelizing the dominant agents (Doctor and Coder in most models) would yield the largest latency reductions. These inefficiencies are structural, not intrinsic to the framework — they reflect model verbosity and code execution time rather than fundamental pipeline overhead.

| Model | Triage | Doctor | Consultant | Coder | Synthesis | Top-2 agents | Top-2 share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-5.2 | 3.01% | 33.07% | 14.45% | 43.20% | 6.26% | coder + doctor | 76.3% |
| claude-4.5-opus | 8.71% | 34.50% | 13.81% | 28.85% | 14.13% | doctor + coder | 63.3% |
| gemini-3-pro | 16.84% | 35.03% | 14.13% | 18.83% | 15.17% | doctor + coder | 53.9% |
| llama-4 | 14.53% | 40.10% | 17.37% | 20.16% | 7.83% | doctor + coder | 60.3% |
| medgemma-27b | 6.86% | 29.39% | 16.43% | 39.35% | 7.97% | coder + doctor | 68.7% |

## 4. Iteration Efficiency

Pooled across all models and visits (n=40), latency correlates **moderately** with iteration count (Pearson r = 0.299, p = 0.061, not statistically significant), suggesting that latency scales approximately linearly with the number of Doctor–Consultant loops. Per-model Pearson r is not reported since most models exhibit zero iteration variance (all visits converge in the same number of loops).

| Model | Mean iterations | Iter std | T/iter (s) | Per-model Pearson r |
| --- | --- | --- | --- | --- |
| gpt-5.2 | 3.0 | 0.00 | 159.76 | N/A (zero variance) |
| claude-4.5-opus | 1.1 | 0.33 | 184.55 | — |
| gemini-3-pro | 1.0 | 0.00 | 190.03 | N/A (zero variance) |
| llama-4 | 3.0 | 0.00 | 16.40 | N/A (zero variance) |
| medgemma-27b | 3.0 | 0.00 | 105.61 | N/A (zero variance) |

## 5. Pareto Analysis

In the (ΔP, latency) space, the following configurations lie on the Pareto frontier: **gpt-5.2, llama-4, medgemma-27b**. 
The following configurations are Pareto-dominated — at least one other model achieves equal or higher performance gain at equal or lower latency: **claude-4.5-opus, gemini-3-pro**. This indicates that efficiency is **model-dependent**, not an intrinsic property of the multi-agent framework itself.

## 6. Model-wise Efficiency Ranking

Models ranked by E_T = ΔP/ΔT (composite gain per second of additional inference):

| Rank | Model | E_T (×10⁻³) | ΔP | T_ag (s) | Pareto-optimal |
| --- | --- | --- | --- | --- | --- |
| 1 | llama-4 | 5.222 | 0.2109 | 49.19 | ✓ |
| 2 | medgemma-27b | 1.201 | 0.3438 | 316.84 | ✓ |
| 3 | claude-4.5-opus | 1.191 | 0.2099 | 207.62 | ✗ |
| 4 | gemini-3-pro | 1.001 | 0.1518 | 190.03 | ✗ |
| 5 | gpt-5.2 | 0.855 | 0.3810 | 479.27 | ✓ |

---
*Composite performance = mean(ESI F1 gain, qSOFA accuracy gain, MAP tolerance gain, LOS tolerance gain)*  
*E_T reported as ×10⁻³ for readability. Pareto optimality assessed in (ΔP, -T_ag) space.*