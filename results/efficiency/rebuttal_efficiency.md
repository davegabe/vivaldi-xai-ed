We thank the reviewer for the constructive feedback and for engaging with our work, which helped clarify the concerns regarding efficiency. While additional ablation studies are not feasible due to the need for clinician evaluation, we provide here a more detailed quantitative analysis of efficiency tradeoffs based on existing results. This analysis will be included in the revised version as an appendix section.

We define ΔP as the mean gain across ESI F1, qSOFA accuracy, MAP tolerance rate, and LOS tolerance rate. All metrics are normalized in [0,1] and capture complementary aspects of ED triage. Efficiency rankings show consistent trends across alternative weightings, with Llama 4 ranking first under all schemes. We report two efficiency metrics: $E_T = ΔP / ΔT$ (gain per second, relevant for latency-constrained settings) and $E_K = ΔP / ΔK$ (gain per 1k tokens, relevant for cost-constrained deployment).

---

**Table 1. Latency and Token Overhead**

| Model | $T_{zs}$ (s) | $T_{ag}$ (s) | ΔT (s) | Latency ratio | Token ratio |
|---|---|---|---|---|---|
| GPT 5.2 | 33.62 | 479.27 | 445.65 | 14.3x | 41.0x |
| Claude 4.5 Opus | 31.29 | 207.62 | 176.33 | 6.6x | 11.2x |
| Gemini 3 Pro | 38.41 | 190.03 | 151.62 | 4.9x | 3.9x |
| Llama 4 | 8.81 | 49.19 | 40.38 | 5.6x | 26.3x |
| MedGemma | 30.57 | 316.84 | 286.27 | 10.4x | 24.8x |

Latency refers to end-to-end inference time per case; $T_{zs}$ denotes zero-shot latency, while $T_{ag}$ denotes agentic inference latency.
Agentic inference introduces latency overheads of 4.9×-14.3× and token overheads of 3.9×-41× across models. Importantly, this variability indicates that overhead varies substantially across models. In particular, Llama 4 achieves sub-minute latency (49s), while GPT 5.2 reaches 479s, showing a nearly 10× spread under the same framework.

---

**Table 2. Performance Gain and Efficiency**

| Model | ΔP | $E_T$ (x10^-3 ΔP/s) | Mean iter. | T/iter (s) | Pareto-optimal |
|---|---|---|---|---|---|
| Llama 4 | 0.2109 | **5.222** | 3.0 | 16.40 | yes |
| MedGemma | 0.3438 | 1.201 | 3.0 | 105.61 | yes |
| Claude 4.5 Opus | 0.2099 | 1.191 | 1.1 | 184.55 | no |
| Gemini 3 Pro | 0.1518 | 1.001 | 1.0 | 190.03 | no |
| GPT 5.2 | **0.3810** | 0.855 | 3.0 | 159.76 | yes |



Pareto optimality is assessed in the ($ΔP$, $-T_{ag}$) space, i.e., performance improvement over zero-shot versus latency: configuration A dominates B if it achieves equal or higher $ΔP$ at equal or lower latency, with at least one strict inequality. You can see the Pareto-optimality plot in the figure at *results/efficiency_analysis/figures/pareto_scatter.png* in our repository.

A clear efficiency–performance tradeoff emerges. GPT 5.2 achieves the highest absolute gain (ΔP = 0.3810) but the lowest latency efficiency ($0.855 \times 10^-3$ ΔP/s), while Llama 4 achieves the highest efficiency ($5.222 \times 10^-3$ ΔP/s), approximately six times higher. This shows that the configuration with the highest performance gain (ΔP) is not the one with the highest latency efficiency ($E_T$).

Pareto analysis further highlights structured tradeoffs under the ($ΔP$, $T_{ag}$) objective. Llama 4 dominates both Claude 4.5 Opus and Gemini 3 Pro, achieving higher performance gain at substantially lower latency. The Pareto frontier is therefore formed by three configurations: Llama 4 (low latency, high efficiency), MedGemma (high gain at moderate cost), and GPT 5.2 (maximum gain at the highest latency). This structure reflects distinct operating regimes depending on resource constraints. Notably, all Pareto-optimal configurations correspond to non-thinking models, whereas the considered thinking models are dominated under this objective.

---

**Table 3. Agent-Level Latency Allocation**

| Model | Triage | Doctor | Consultant | Coder | Synthesis | Doctor + Coder share |
|---|---|---|---|---|---|---|
| GPT 5.2 | 3.0% | 33.1% | 14.5% | 43.2% | 6.3% | 76.3% |
| Claude 4.5 Opus | 8.7% | 34.5% | 13.8% | 28.9% | 14.1% | 63.3% |
| Gemini 3 Pro | 16.8% | 35.0% | 14.1% | 18.8% | 15.2% | 53.9% |
| Llama 4 | 14.5% | 40.1% | 17.4% | 20.2% | 7.8% | 60.3% |
| MedGemma | 6.9% | 29.4% | 16.4% | 39.4% | 8.0% | 68.7% |

Latency is not uniformly distributed across the pipeline. The Doctor and Coder agents jointly account for 54% to 76% of total runtime, with the Coder alone contributing up to 43%. This concentration indicates that inefficiencies are localized rather than systemic, and identifies clear optimization targets (e.g., limiting Doctor–Consultant iterations or parallelizing specific steps).

---

Taken together, these analyses clarify the efficiency–performance tradeoffs discussed above. Although agentic inference introduces additional computational cost, the overhead is not uniform: efficiency varies substantially across models (up to 6×), Pareto-optimal configurations emerge under different resource constraints, and latency is concentrated in a small subset of pipeline components. This suggests that efficiency is not fully explained by the multi-agent design alone, but also varies across models and is influenced by the distribution of computation across agent interactions.
