# Executive Summary: AI Security Incidents 2025–2026 Research Project

**Author:** Ahmed Adel Bakr Alderai
**Date:** April 4, 2026

## Project Overview

The "AI Security Incidents 2025-2026" research project is a pioneering empirical investigation into the operational vulnerabilities, supply chain attacks, and regulatory compliance failures affecting production Artificial Intelligence systems. Built by PhD Researcher Ahmed Adel Bakr Alderai, this project systematically catalogs, analyzes, and correlates real-world AI security breaches with emerging governance frameworks. 

At its core, this project transforms scattered incident reports, vulnerability disclosures, and underground threat intelligence into the first structured, machine-readable dataset of AI security incidents mapping directly to the European Union (EU) AI Act. By moving beyond theoretical threat modeling to document actual production failures, the project provides critical, actionable evidence for cybersecurity practitioners, compliance officers, and regulators. 

The significance of this work lies in its timing and its focus. As the EU AI Act enforcement deadline (August 2026) approaches, enterprises face immense financial liabilities (fines up to €35M or 7% of global turnover) for non-compliance. Yet, the industry lacks empirical data on how AI systems actually fail in the wild. This project bridges that gap, offering the necessary data to perform robust AI Vendor Risk Assessments (AI VRA), develop threat models, and establish accountability for AI deployment.

## Timeline and Evolution

The genesis of this specific dataset iteration occurred on **March 31, 2026**, catalyzed by the critical discovery of the Claude Code npm source map leak. This exposure revealed internal architectural details, prompting an exhaustive, multi-agent retrospective analysis of the AI threat landscape spanning from January 2025 to the present. Since that inflection point, the project has rapidly evolved from initial data aggregation to deep forensic analysis, regulatory mapping, and the preparation of academic and commercial deliverables.

## Key Metrics and Scope

The research encompasses a rigorously verified dataset and a massive underlying corpus of forensic evidence:

*   **Total Incidents Documented:** 56 total incidents (40 original baseline + 16 newly discovered incidents spanning recent exploits).
*   **Verification Anchors:** 12 incidents meticulously verified against independent public sources to serve as precision anchors for the `aisec-euaiact-v1.0` benchmark.
*   **Research Corpus:** A 2.0 GB comprehensive research data corpus stored on a Hetzner server.
*   **Vulnerability Classes:** Categorization across 9 critical domains, including supply chain poisoning, training data leaks, model weight extraction, and system prompt compromises.
*   **Severity Distribution:** A stark skew toward high-impact events, with over 80% of baseline incidents rated as High or Critical severity.

## Academic Contribution

This project introduces **AISecIncidents-2025-26**, the first large-scale, open dataset that correlates real-world LLM security incidents with compliance requirements. Unlike existing databases (e.g., AIID or AIAAIC) that focus broadly on AI harms, this dataset specifically targets information security breaches, extraction attacks, and supply chain poisonings. It provides a standardized incident taxonomy, severity classification, and a benchmark (`aisec-euaiact-v1.0`) for evaluating the legal and regulatory implications of AI failures. This foundation enables future academic study of AI system vulnerabilities, incident response maturity, and the effectiveness of regulatory frameworks.

## Commercial Relevance and EU AI Act Compliance

Commercially, this dataset is an indispensable tool for enterprise compliance. Every incident in the dataset is mapped to specific obligations under the EU AI Act:
*   **Article 9:** Risk Management System failures (e.g., supply chain and third-party risks).
*   **Article 13:** Transparency and Provision of Information (e.g., disclosure and data handling visibility).
*   **Article 15:** Accuracy, Robustness, and Cybersecurity failures.

This mapping transforms the dataset from a simple historical record into a proactive **AI Vendor Risk Assessment** tool. Organizations can use this empirical data to conduct due diligence, audit their AI supply chains, and demonstrate conformity to regulators, directly mitigating the risk of massive financial penalties.

## Flagship Finding: Unauthorized Model Distillation at Scale

The most critical and novel finding of this research is the empirical proof of unauthorized LLM distillation at a massive production scale. Discovered via authenticated HuggingFace API queries, the research documents **2.1 million unauthorized downloads** of "Claude Opus 4.6" distillation models. This comprises 50 open-source model variants fine-tuned on over 10,000 scraped Claude API outputs. This represents a blatant Terms of Service violation and provides the first documented evidence of a novel Intellectual Property (IP) extraction vector operating openly in public model repositories.

## Technical Architecture

The research infrastructure utilizes a hybrid, multi-agent approach to handle the vast amount of threat intelligence:
*   **Local Environment (Mac):** 32 core files handling project strategy, schemas, validation logic (`validate.py`), and publication drafts (`arXiv_draft.md`, dataset cards).
*   **Remote Server (Hetzner):** A 2.0 GB, 13,615-file research corpus organized into 14 distinct categories (e.g., `git-forensics`, `cve-pocs`, `system-prompts`, `huggingface`). This server processes the raw data, coordinates 12 parallel AI research agents for source triangulation, and stores the extensive metadata necessary for ongoing investigation.
