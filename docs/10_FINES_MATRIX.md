# EU AI Act Fines Matrix

This matrix maps the nine primary AI security incident types in the dataset to their corresponding EU AI Act obligations, maximum penalties, and estimated financial exposure for a large enterprise.

## Penalty Tiers

The EU AI Act establishes two main penalty tiers for non-compliance:

- **Prohibited AI practices (Art. 5):** Up to **€35 million** or **7%** of global annual turnover, whichever is higher.
- **High-risk AI system obligations (Arts. 8–15):** Up to **€15 million** or **3%** of global annual turnover, whichever is higher.

> **August 2026: EU AI Act high-risk AI obligations become enforceable. Max penalty: €35M or 7% global annual turnover.**

## Fines Matrix

| Incident Type | EU AI Act Article Violated | Maximum Fine | Real Example from Dataset | Estimated Exposure for a €10B-Revenue Company |
|---|---|---|---|---|
| supply_chain | Art. 9 (Risk Management) | €15M or 3% global turnover | Shai-Hulud npm Worm v1 | €300M |
| source_code | Art. 13 (Transparency) | €15M or 3% global turnover | Claude Code npm Source Map Leak | €300M |
| user_data | Art. 9 (Risk Management) | €15M or 3% global turnover | Meta AI Agent Rogue Data Breach (SEV1) | €300M |
| api_keys | Art. 15 (Robustness) | €15M or 3% global turnover | Claude Code CVE-2026-21852 (API Key Exfiltration) | €300M |
| training_data | Art. 15 (Robustness) | €15M or 3% global turnover | Stability AI Training Pipeline Compromise | €300M |
| model_weights | Art. 15 (Robustness) | €15M or 3% global turnover | Claude Opus 4.6 Mass Distillation on HuggingFace | €300M |
| state_sponsored_misuse | Art. 9 (Risk Management) | €15M or 3% global turnover | PRC Cyber Operation Using Claude-Based Tools | €300M |
| system_prompt | Art. 13 (Transparency) | €15M or 3% global turnover | Claude System Prompts 57,000-Word Collection | €300M |
| api_vulnerability | Art. 15 (Robustness) | €15M or 3% global turnover | CVE-2025-55284 - Claude Code DNS Exfiltration via Prompt Injection | €300M |

## Exposure Interpretation

For a company with €10 billion in annual global revenue, a 3% turnover penalty translates to **€300 million** per incident type. Because the EU AI Act applies the higher of the fixed cap or the percentage of turnover, large enterprises face material, balance-sheet-level risk. The matrix above shows that all nine incident types mapped from the dataset fall under the high-risk obligations tier (Arts. 9, 13, and 15). While none of these nine types currently map to the prohibited-practices tier under Art. 5, organizations deploying general-purpose or high-risk AI systems should monitor for use cases that could trigger the higher **€35 million / 7%** penalty tier—particularly those involving subliminal manipulation, social scoring, or real-time biometric identification in publicly accessible spaces.

---

*Prepared by Ahmed Adel Bakr Alderai | AI Security Incidents Research*
