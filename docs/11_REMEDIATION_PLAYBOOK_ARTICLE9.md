# Remediation Playbook — Article 9 (Risk Management)

**Scope:** `supply_chain` and `state_sponsored_misuse` incident types  
**Author:** Ahmed Adel Bakr Alderai  
**Target Audience:** CISOs, Compliance Officers, AI Risk Managers

---

## Executive Summary

Article 9 of the EU AI Act mandates that high-risk AI system providers establish, implement, and maintain a continuous risk management system throughout the entire AI lifecycle. For organizations deploying AI in supply-chain-dependent environments or facing state-sponsored threats, this means extending traditional risk management to cover third-party dependencies, adversarial misuse of AI tooling, and cascading failure scenarios. This playbook provides a concise, actionable framework for assessing supply chain exposure, documenting compliance artifacts, and operationalizing a 12-month remediation roadmap grounded in real-world incidents from the AI Security Incidents Research dataset.

---

## 5-Step AI Supply Chain Risk Assessment Checklist

1. **Inventory all AI-related third-party dependencies.**
   - Map every open-source package, model registry, API gateway, and vendor SDK used in AI training, inference, and deployment pipelines.
   - Maintain machine-readable Software Bills of Materials (SBOMs) for each high-risk system.

2. **Classify vendors and dependencies by criticality.**
   - Apply a tiered classification (Tier 1–3) based on data sensitivity, system availability requirements, and downstream blast radius.
   - Prioritize Tier 1 vendors for enhanced due diligence and continuous monitoring.

3. **Evaluate access controls and CI/CD hygiene.**
   - Audit maintainer access, multi-factor authentication (MFA) enforcement, and signing-key management for all build pipelines.
   - Require commit signing, artifact attestation, and immutable build logs for every release.

4. **Model adversarial and misuse scenarios.**
   - Conduct threat-modeling exercises that explicitly include state-sponsored misuse of AI tools, typosquatting, and multi-stage cascading attacks.
   - Update risk registers quarterly or after every significant architecture change.

5. **Define measurable residual-risk thresholds and escalation triggers.**
   - Set quantitative KPIs (e.g., mean time to patch critical dependencies ≤ 48 hours, SBOM coverage ≥ 95%).
   - Establish board-level escalation criteria for breaches exceeding residual-risk thresholds.

---

## Required Documentation Artifacts for Article 9 Compliance

- **Risk Management Plan (RMP)** — lifecycle-wide risk identification, evaluation, mitigation, and monitoring strategy.
- **Vendor Assessment Reports** — documented due diligence for all Tier 1 and Tier 2 AI supply-chain vendors.
- **Software Bills of Materials (SBOMs)** — machine-readable inventories of open-source and commercial components.
- **Threat Model & Risk Register** — adversarial scenarios, likelihood/impact ratings, and residual-risk acceptance records.
- **Incident Response Playbooks** — step-by-step procedures for supply-chain compromise and state-sponsored misuse events.
- **Audit Trail & Change Logs** — immutable records of risk-assessment updates, patch decisions, and exception approvals.

---

## 12-Month Implementation Roadmap

| Quarter | Milestone | Key Deliverables |
|:--------|:----------|:-----------------|
| **Q1** | **Discovery & Baseline** | Complete dependency inventory; generate SBOMs for all high-risk AI systems; finalize vendor criticality matrix. |
| **Q2** | **Control Hardening** | Enforce MFA, commit signing, and artifact attestation across all AI build pipelines; onboard automated SBOM drift detection. |
| **Q3** | **Adversarial Validation** | Run tabletop exercises for supply-chain cascade and state-sponsored misuse scenarios; update threat models and risk registers. |
| **Q4** | **Compliance Certification** | Conduct internal audit against Article 9 requirements; remediate gaps; produce audit-ready documentation package for notified bodies. |

---

## Case Studies from the Dataset

### 1. Shai-Hulud npm Worm v1 (`supply_chain`)

| Attribute | Detail |
|:----------|:-------|
| **Incident name** | Shai-Hulud npm Worm v1 |
| **What happened** | A self-replicating worm compromised over 500 npm packages in the AI/ML ecosystem via maintainer account takeover, harvesting developer credentials and propagating through CI/CD pipelines. |
| **Article 9 compliance gap** | Inadequate third-party dependency risk monitoring and lack of continuous vendor-access-control verification allowed the worm to spread unchecked. |
| **Remediation takeaway** | Treat every open-source dependency as a potential attack vector: enforce MFA on all maintainer accounts, require signed commits, and implement automated SBOM drift alerting. |

### 2. TeamPCP Cascading Supply Chain Attack (`supply_chain`)

| Attribute | Detail |
|:----------|:-------|
| **Incident name** | TeamPCP Cascading Supply Chain Attack |
| **What happened** | A multi-stage zero-day campaign exploited the Trivy vulnerability scanner, then self-propagated through CI/CD worms to compromise Checkmarx, LiteLLM, and Telnyx—abusing downstream VoIP APIs. |
| **Article 9 compliance gap** | Failure to model cascading, cross-vendor failure scenarios and insufficient residual-risk thresholds for security-tooling supply chains. |
| **Remediation takeaway** | Security scanners are part of the supply chain too; map transitive dependencies, run red-team exercises against your own tooling, and enforce strict network segmentation between build and runtime environments. |

### 3. PRC Cyber Operation Using Claude-Based Tools (`state_sponsored_misuse`)

| Attribute | Detail |
|:----------|:-------|
| **Incident name** | PRC Cyber Operation Using Claude-Based Tools |
| **What happened** | Chinese state-sponsored actors leveraged Claude-based AI tools in AI-assisted, partially autonomous cyber operations targeting U.S. systems. |
| **Article 9 compliance gap** | Risk management frameworks did not adequately anticipate adversarial misuse of frontier AI capabilities by nation-state actors. |
| **Remediation takeaway** | Expand threat models to include state-sponsored misuse of AI assistants; implement usage anomaly detection, geofencing, and strict API access governance for high-capability models. |

---

*End of Playbook*
