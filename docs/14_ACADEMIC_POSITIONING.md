# Academic Positioning and Submission Strategy

## Venue Comparison

### IEEE S&P 2027
- **Deadline:** January 27, 2027
- **Acceptance Rate:** ~15%
- **Fit:** Excellent. The paper's empirical security focus, static analysis of a production AI agent, and regulatory compliance mapping align closely with IEEE S&P's emphasis on rigorous security research with real-world impact. The Semantic Desync vulnerability class and AST-based analysis provide the technical depth expected at this venue.

### USENIX Security 2027
- **Deadline:** February 2027 (estimated)
- **Acceptance Rate:** ~15–17%
- **Fit:** Strong. USENIX Security has a robust incident response and empirical security community. The dataset's incident archaeology and multi-agent verification methodology would resonate with this audience, though the regulatory focus is slightly less central than at IEEE S&P.

### NDSS 2027
- **Deadline:** June/July 2026 (estimated)
- **Acceptance Rate:** ~16–18%
- **Fit:** Moderate. NDSS emphasizes network and distributed system security. While the supply chain and API vulnerability components fit well, the static analysis and regulatory mapping aspects are somewhat outside NDSS's core scope.

**Recommendation:** Primary submission to **IEEE S&P 2027**, with USENIX Security 2027 as the fallback venue.

---

## Contribution Bullet Points for Cover Letter

1. **First large-scale open dataset correlating real-world LLM security incidents with EU AI Act compliance requirements**, bridging the empirical gap between theoretical AI threat modeling and documented operational breaches.

2. **Novel static analysis framework for AI agent security assessment**, including the discovery of 23 AST-based checks in a production system, the formalization of the *Semantic Desync* vulnerability class, and the analysis of a 57,000-word hidden instruction set with direct regulatory implications.

3. **Release of aisec-euaiact-v1.0**, the first multi-label classification benchmark for automated EU AI Act compliance assessment, with 12 verified ground-truth labels and established baselines for the research community.

---

## Ethical Considerations

This research adheres to responsible disclosure and ethical research practices:

- **Publicly accessible artifacts:** The npm source maps analyzed were publicly distributed metadata, not obtained through unauthorized access, exploitation, or circumvention of access controls.
- **No exploits developed:** No active exploits were developed, tested, or deployed against production systems. The research was limited to passive static analysis of already-public artifacts.
- **No PoC published:** No proof-of-concept code has been published for the vulnerabilities identified in this work.
- **Responsible notification:** Affected organizations were notified of unpatched vulnerabilities with adherence to 90-day disclosure timelines where applicable.
- **Analysis scope:** The static analysis was confined to security-relevant architectural patterns (permission systems, sandbox configs, AST checks) and did not involve extraction of proprietary business logic, user data, or training datasets.

---

## IEEE S&P Cover Letter Template (200 words)

Dear Editors and Reviewers,

We submit "AISecIncidents-2025-26: A Dataset of AI Security Breaches with EU AI Act Compliance Mapping and Static Analysis of Claude Code" for consideration at the IEEE Symposium on Security and Privacy (S&P) 2027.

This paper makes three core contributions. First, we present AISecIncidents-2025-26, a dataset of 55 AI security incidents (12 verified, 43 with confidence scores) spanning January 2025 to April 2026, mapped to EU AI Act Articles 9, 13, and 15. Second, we conduct the first systematic static analysis of a production AI agent (Claude Code v2.1.88), identifying 23 AST-based security checks, formalizing a novel *Semantic Desync* vulnerability class, and analyzing a 57,000-word hidden instruction set with Article 13 transparency implications. Third, we release aisec-euaiact-v1.0, a multi-label classification benchmark with 12 ground-truth labels for automated compliance assessment.

Our work bridges empirical incident archaeology with rigorous technical analysis, directly addressing the operational security risks emerging from deployed LLM systems. We believe the paper's combination of dataset contribution, novel vulnerability analysis, and regulatory mapping is well-suited to the IEEE S&P audience.

Thank you for your consideration.

Sincerely,  
Ahmed Adel Bakr Alderai
