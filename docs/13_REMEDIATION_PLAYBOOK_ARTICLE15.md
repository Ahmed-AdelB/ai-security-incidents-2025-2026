# Remediation Playbook — Article 15 (Robustness)

**Scope:** `api_vulnerability` | `model_weights` | `training_data` | `api_keys`

---

## 1. Executive Summary

Article 15 of the EU AI Act mandates that high-risk AI systems maintain an appropriate level of accuracy, robustness, and cybersecurity throughout their lifecycle. This playbook provides a concise, actionable remediation framework for incidents involving API vulnerabilities, model weight exposure, training data compromise, and API key leakage. It centers on a primary case study—CVE-2025-55284—to illustrate how prompt injection can bypass robustness controls, and delivers seven technical controls plus CVSS 4.0 scoring guidance tailored to AI-specific vulnerabilities.

---

## 2. Primary Case Study: CVE-2025-55284

### Incident
**CVE-2025-55284 — Claude Code DNS Exfiltration via Prompt Injection**

In this incident, an attacker embedded malicious instructions inside code comments (prompt injection) that were processed by Claude Code. The injected prompt manipulated the AI agent into invoking the `BashTool`, which subsequently executed DNS queries containing exfiltrated data.

### Article 15 Robustness / Cybersecurity Failure

This incident represents a systemic failure under Article 15:

- **Adversarial Resilience:** The AI system failed to distinguish between legitimate developer intent and adversarial input embedded in seemingly benign code comments.
- **Cybersecurity Controls:** The agent’s tool execution layer lacked sufficient isolation and egress monitoring, allowing unauthorized DNS exfiltration of sensitive artifacts (environment variables, API keys, and local files).
- **System Integrity:** The breach altered the intended use and performance of the AI system, converting a coding assistant into an unwitting exfiltration mechanism.

### Remediation Takeaway

Organizations must treat prompt injection not merely as a model behavior issue, but as a **system-level security vulnerability**. Effective remediation requires layered defenses: rigorous input validation, strict sandboxing of AI agent actions, and real-time monitoring of network egress to block exfiltration channels.

---

## 3. 7 Technical Controls Checklist

| # | Control | Actionable Description |
|---|---------|------------------------|
| 1 | **Input Validation** | Implement strict parsing, schema enforcement, and adversarial input filtering on all prompts, user data, and file contents before they reach the model or tool layer. |
| 2 | **Sandboxing** | Execute all AI agent actions—especially code interpretation and tool use—inside ephemeral, isolated environments (e.g., containers or VMs) with no access to host secrets or critical network paths. |
| 3 | **Rate Limiting** | Apply dynamic rate limits and quota enforcement on model APIs and tool endpoints to mitigate brute-force probing, data scraping, and automated exploitation attempts. |
| 4 | **Exfiltration Detection** | Monitor and alert on anomalous network egress (DNS queries, HTTP requests, unexpected outbound connections) initiated by AI systems to detect and block unauthorized data transfers. |
| 5 | **Dependency Pinning** | Pin all third-party package and dependency versions, verifying cryptographic hashes during build and deployment to prevent supply chain poisoning and unexpected malicious updates. |
| 6 | **Supply Chain Signing** | Cryptographically sign model weights, datasets, container images, and executable artifacts (e.g., using Sigstore or Notary) to ensure end-to-end integrity from development to production. |
| 7 | **Model Access Logging** | Maintain immutable, cryptographically secure audit logs of all API requests, model queries, administrative actions, and key usage to enable rapid incident response and forensic investigation. |

---

## 4. CVSS Scoring Guidance for AI System Vulnerabilities

When scoring AI-specific vulnerabilities, use **CVSS 4.0** and emphasize the following metric groups to accurately capture the unique risk profile of autonomous and semi-autonomous systems:

### Key Metrics to Emphasize

| Metric Group | Scoring Consideration |
|--------------|----------------------|
| **Attack Vector (AV)** | Favor `Network (N)` when the vulnerability is reachable via public APIs or shared model endpoints; use `Local (L)` only if physical or authenticated host access is strictly required. |
| **Attack Complexity (AC)** | Rate as `Low (L)` if the exploit requires only standard prompt injection or API manipulation; rate `High (H)` if multiple chained conditions or rare environmental factors are needed. |
| **Privileges Required (PR)** | Typically `None (N)` for prompt injection attacks against publicly exposed models; adjust to `Low (L)` or `High (H)` if authenticated sessions or admin credentials are prerequisites. |
| **User Interaction (UI)** | Use `None (N)` when the AI agent acts autonomously on malicious input without human approval; use `Passive (P)` or `Active (A)` if human review or explicit confirmation is required for exploitation. |
| **Scope (S)** | Pay special attention here. Autonomous AI agents often have delegated access to downstream systems (databases, CI/CD pipelines, email, code repositories). If a compromise of the AI system can lead to unauthorized impact on these connected resources, **increase the Scope metric** accordingly. |
| **Confidentiality (C) / Integrity (I) / Availability (A)** | Evaluate based on the data classes and systems the AI agent can touch. High ratings are common when agents process source code, PII, or production credentials. |

### Important Note on Autonomous Agents

Autonomous AI agents that operate with broad tool access or broad system permissions can act as **force multipliers** for attackers. When scoring, consider whether successful exploitation extends beyond the AI application itself to downstream infrastructure. If so, elevate the **Scope** and downstream impact metrics to reflect the full blast radius of the vulnerability.

---

*Document prepared for CISOs and compliance officers as part of the AI Security Incidents Research project by Ahmed Adel Bakr Alderai.*
