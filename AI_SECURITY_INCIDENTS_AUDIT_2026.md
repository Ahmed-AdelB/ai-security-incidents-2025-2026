# SECURITY INCIDENT ACCESSIBILITY & REMEDIATION AUDIT
## IEEE Code of Ethics Section 1.2 | NIST SP 800-61 Compliance
### Audit Date: March 31, 2026
### Classification: PUBLIC - EDUCATIONAL/RESEARCH PURPOSES

---

## EXECUTIVE SUMMARY

This audit documents publicly-reported AI security incidents from March 2026, cataloging GitHub repositories, archive snapshots, CDN URLs, DMCA status, and remediation status for each incident. All information gathered from public sources for security research and educational purposes.

---

## INCIDENT A: CLAUDE CODE NPM SOURCE MAP LEAK
### Date: March 31, 2026

### Overview
Anthropic's Claude Code CLI tool (version 2.1.88) accidentally included a 59.8MB JavaScript source map file in its npm package, exposing approximately 512,000 lines of TypeScript source code (1,900+ files) including internal feature flags, system prompts, and unreleased features.

### GitHub Repository URLs (Archive/Mirror)
| Repository | Status | URL |
|------------|--------|-----|
| instructkr/claude-code | ACTIVE - Fastest to 30K stars | https://github.com/instructkr/claude-code |
| instructkr/claw-code | ACTIVE - Python porting work | https://github.com/instructkr/claw-code |
| Kuberwastaken/claude-code | ACTIVE | https://github.com/Kuberwastaken/claude-code |
| nirholas/claude-code | ACTIVE | https://github.com/nirholas/claude-code |
| abubakarsiddik31/leaked-claude-code | ACTIVE - With legal notice | https://github.com/abubakarsiddik31/leaked-claude-code |
| leeyeel/claude-code-sourcemap | ARCHIVED - Original research | https://github.com/leeyeel/claude-code-sourcemap |
| dnakov/anon-kode | FORK - Active development | https://github.com/dnakov/anon-kode |

### DMCA/Takedown Status
- **DMCA Status**: NO formal DMCA takedown notices filed as of March 31, 2026
- **Anthropic Response**: Removed source map from npm registry, deprecated npm installation method
- **Repository Compliance**: Repositories include DMCA compliance notices (e.g., abubakarsiddik31/leaked-claude-code)
- **Historical Precedent**: Anthropic issued DMCA takedown in April 2025 for reverse-engineered code (techshotsapp.com)

### Wayback Machine / Archive Snapshots
- **Original Discovery**: https://x.com/Fried_rice/status/2038894956459290963 (Chaofan Shou's post)
- **Hacker News Discussion**: https://news.ycombinator.com/item?id=47584540
- **No direct archive.org snapshot of source map** - file too large for standard archival

### CDN URLs That Served Exposed Files
| CDN | URL | Status |
|-----|-----|--------|
| jsDelivr | https://www.jsdelivr.com/package/npm/@anthropic-ai/claude-code | CLEAN - Current version only |
| unpkg | https://unpkg.com/@anthropic-ai/claude-code@2.1.88/ | REMOVED |
| npm registry | https://registry.npmjs.org/@anthropic-ai/claude-code/-/claude-code-2.1.88.tgz | REMOVED |
| R2 Storage | Referenced in source map (r2.dev subdomain) | REVOKED |

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| Source map removed from npm | COMPLETED | March 31, 2026 |
| Version 2.1.88 unpublished | COMPLETED | March 31, 2026 |
| npm installation deprecated | ANNOUNCED | March 31, 2026 |
| Native installer recommended | ACTIVE | Ongoing |
| GitHub mirrors taken down | NOT INITIATED | - |

### News Article URLs
1. https://dev.to/evan-dong/claude-codes-entire-source-code-just-leaked-512000-lines-exposed-3139
2. https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo
3. https://qiita.com/xiji2646/items/87158c616b1ab3101bc1 (Japanese)
4. https://www.penligent.ai/hackinglabs/ar/claude-code-source-map-leak-what-was-exposed-and-what-it-means/
5. https://m.economictimes.com/news/international/us/claude-code-source-code-leak-did-anthropic-just-expose-its-ai-secrets-hidden-models-and-undercover-coding-strategy-to-the-world/articleshow/129930888.cms
6. https://rollingout.com/2026/03/31/anthropic-claude-code-leak-512000-lines/
7. https://securityonline.info/claude-code-source-leak-npm-anthropic-source-map/
8. https://www.the-ai-corner.com/p/claude-code-source-code-leaked-2026

### Exposed Internal Features (44 Feature Flags)
- KAIROS: Background autonomous daemon mode
- BUDDY: Digital pet system (Easter egg)
- PROACTIVE, VOICE_MODE, BRIDGE_MODE
- Full Playwright browser control
- Cron scheduling for agents
- Multi-agent orchestration (swarms)
- Model codenames: Capybara, Fennec, Numbat

---

## INCIDENT B: ANTHROPIC MYTHOS CMS LEAK
### Date: March 26, 2026

### Overview
Anthropic's Sanity CMS was misconfigured, exposing ~3,000 unpublished assets including draft blog posts about the unreleased "Claude Mythos" (codename: Capybara) model positioned above Opus tier.

### GitHub Repository URLs
- **No direct GitHub mirrors** - leak was CMS content, not source code
- **Research/analysis repos**: Various security research repositories reference findings

### DMCA/Takedown Status
- **DMCA Status**: N/A - CMS content leak, not code
- **Anthropic Response**: Restricted access within hours of Fortune notification
- **Current Status**: Original assets removed, screenshots circulate

### Wayback Machine / Archive Snapshots
- **Fortune Article (Original Report)**: https://fortune.com/2026/03/26/anthropic-claude-mythos-leak-cms/
- **No direct archive of CMS assets** - restricted before archival
- **Screenshots archived via social media**: X/Twitter, Reddit

### CDN URLs
| CDN | URL | Status |
|-----|-----|--------|
| Sanity CMS | staging-docs.anthropic.com (reported) | RESTRICTED |
| CloudFront (reported) | Various asset URLs | REVOKED |

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| CMS access restricted | COMPLETED | March 26, 2026 |
| Public URLs disabled | COMPLETED | March 26, 2026 |
| Draft content removed | COMPLETED | March 26, 2026 |
| Screenshots circulating | ACTIVE | - |

### News Article URLs
1. https://fortune.com/2026/03/26/anthropic-claude-mythos-leak-cms/ (ORIGINAL)
2. https://aitoolhunt.co/blog/anthropic-claude-mythos-leaked-everything-we-know-2026
3. https://www.abhs.in/blog/anthropic-claude-mythos-cms-leak-march-2026
4. https://claudemythos.info/anthropic-data-leak-2026/
5. https://www.igorslab.de/en/anthropic-confirms-new-model-following-cms-error-leak-claude-myth-suggests-advanced-cyber-capabilities/
6. https://www.tekedia.com/anthropics-claude-mythos-details-leaked-via-a-misconfigured-content-management-system/
7. https://www.techzine.eu/news/applications/140017/details-leak-on-anthropics-step-change-mythos-model/
8. https://www.ayautomate.com/blog/claude-vs-chatgpt-2026

### Exposed Information
- Claude Mythos/Capybara model details
- Internal benchmark data ("dramatically higher" than Opus 4.6)
- CEO retreat details (18th-century English manor)
- ~3,000 unpublished marketing assets
- Draft blog posts with performance claims

---

## INCIDENT C: OPENAI GPT-5.4 CODEX REPO LEAK
### Date: February 27 - March 2, 2026

### Overview
OpenAI accidentally leaked GPT-5.4 references through two pull requests in the public Codex GitHub repository, including minimum model version requirements and fast mode toggle descriptions.

### GitHub Repository URLs (Official)
| Repository | URL | Status |
|------------|-----|--------|
| OpenAI Codex (Official) | https://github.com/openai/codex | ACTIVE |
| PR #13050 (Original-Resolution Vision) | https://github.com/openai/codex/pull/13050 | MERGED - Modified |
| PR #13212 (Fast Mode Toggle) | https://github.com/openai/codex/pull/13212 | MERGED - Modified |

### DMCA/Takedown Status
- **DMCA Status**: N/A - Public repository, PRs still accessible
- **OpenAI Response**: Force-pushed changes to remove GPT-5.4 references
- **PR #13050**: 7 force pushes between 19:30-22:44 UTC on Feb 27
- **PR #13212**: Scrubbed within 3 hours of publication

### Wayback Machine / Archive Snapshots
- **GitHub commit history**: Auditable via git log
- **Screenshots preserved**: Community captured before scrubbing
- **No archive.org needed** - Git history retains evidence

### CDN URLs
- N/A - This incident involved GitHub repository content only

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| PR #13050 modified | COMPLETED | Feb 27, 2026 |
| PR #13212 modified | COMPLETED | Mar 2, 2026 |
| GPT-5.4 references removed | COMPLETED | Mar 2, 2026 |
| Code history still auditable | ACTIVE | - |

### News Article URLs
1. https://awesomeagents.ai/news/gpt-5-4-codex-repo-leak/
2. https://www.theneurondaily.com/p/openai-leaked-gpt-5-4-three-times
3. https://www.eweek.com/news/gpt-5-4-codex-leak-model-update-neuron/
4. https://evolink.ai/blog/gpt-5-4-release-date-2026
5. https://awesomeagents.ai/news/openai-gpt-5-4-sooner-than-you-think/
6. https://eu.36kr.com/en/p/3706836982804612 (Chinese/English)
7. https://manifold.markets/Bayesian/gpt-54-openai-release-date

### Leaked Information
- Full-resolution vision support (`detail: "original"`)
- Fast mode toggle with priority service tier
- Model version requirement: (5, 4) → later changed to (5, 3)
- Internal model identifier: `gpt-5.4-ab-arm1-1020-1p-codexswic-ev3`
- Employee screenshot (Tibo @tibo-openai) showing GPT-5.4 in model selector

---

## INCIDENT D: GOOGLE GEMINI PROTO FILE LEAK
### Date: Searched - No confirmed March 2026 leak found

### Search Results
- **No specific March 2026 Google Gemini proto file leak identified**
- Previous Cloud Build misconfigurations documented in security literature
- gemini-cli-extensions/devops repository is legitimate Google project

### Note
The requested incident appears to be either:
1. A historical reference to prior incidents
2. Unreported/undisclosed
3. Confused with other incidents

---

## INCIDENT E: TEAMPCP SUPPLY CHAIN CAMPAIGN
### Date: March 19-27, 2026

### Overview
TeamPCP (also tracked as PCPcat, PersyPCP, ShellForce, DeadCatx3) executed a cascading supply chain attack compromising Trivy, npm packages, Checkmarx, LiteLLM, and Telnyx through credential harvesting and self-propagating worms.

### GitHub Repository URLs
| Repository | URL | Purpose |
|------------|-----|---------|
| aquasecurity/trivy | https://github.com/aquasecurity/trivy | Compromised via CVE-2026-33634 |
| aquasecurity/trivy-action | https://github.com/aquasecurity/trivy-action | 76/77 tags force-pushed |
| BerriAI/litellm | https://github.com/BerriAI/litellm | Compromised PyPI package |
| checkmarx/kics-github-action | https://github.com/checkmarx/kics-github-action | 35 tags hijacked |
| teampcp-docs-* (various) | GitHub orgs | Exfiltration repositories created |

### DMCA/Takedown Status
- **DMCA Status**: N/A - Malicious content, not IP violations
- **GitHub Response**: Removed malicious workflows, restored legitimate tags
- **npm Response**: Removed CanisterWorm packages
- **PyPI Response**: Quarantined litellm and telnyx packages

### CDN URLs / IOCs
| Indicator | Type | Status |
|-----------|------|--------|
| scan.aquasecurtiy[.]org | C2 Domain | ACTIVE - Monitor |
| 45.148.10.212 | C2 IP | ACTIVE |
| tdtqy-oyaaa-aaaae-af2dq-cai.raw.icp0[.]io | ICP Canister C2 | ACTIVE |
| checkmarx[.]zone | C2 Domain | ACTIVE |
| models.litellm[.]cloud | Exfiltration | ACTIVE |
| *.trycloudflare[.]com | Cloudflare Tunnels | ACTIVE |

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| Trivy malicious versions removed | COMPLETED | Mar 19, 2026 |
| npm CanisterWorm packages removed | COMPLETED | Mar 20, 2026 |
| LiteLLM PyPI quarantined | COMPLETED | Mar 24, 2026 |
| Telnyx PyPI quarantined | COMPLETED | Mar 27, 2026 |
| Checkmarx tags restored | COMPLETED | Mar 23, 2026 |

### News Article URLs
1. https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack
2. https://cycode.com/blog/lite-llm-supply-chain-attack/
3. https://codekeeper.co/ticker/teampcp-hacks-major-open-source-platforms
4. https://aimodelsmap.com/litellm-supply-chain-attack
5. https://www.aikido.dev/blog/telnyx-pypi-compromised-teampcp-canisterworm
6. https://mrcloudbook.com/teampcp-supply-chain-attack-telnyx-canisterworm-full-analysis-cve-2026-33634/
7. https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/
8. https://www.kaspersky.com/blog/critical-supply-chain-attack-trivy-litellm-checkmarx-teampcp/55510/
9. https://www.mend.io/blog/teampcp-supply-chain-series-part-2/
10. https://www.sans.org/blog/axios-npm-supply-chain-compromise-malicious-packages-remote-access-trojan

### Affected Packages Summary
| Package | Platform | Versions | Status |
|---------|----------|----------|--------|
| trivy | GitHub/Docker | v0.69.4 | REMOVED |
| trivy-action | GitHub Actions | 76 tags | RESTORED |
| litellm | PyPI | 1.82.7, 1.82.8 | QUARANTINED |
| telnyx | PyPI | 4.87.1, 4.87.2 | QUARANTINED |
| CanisterWorm | npm | 66+ packages | REMOVED |
| ast-results | OpenVSX | v2.53.0 | REMOVED |
| cx-dev-assist | OpenVSX | v1.7.0 | REMOVED |

---

## INCIDENT F: SHAI-HULUD NPM WORM
### Date: September 2025 (Wave 1), November 2025 (Wave 2)

### Overview
First-of-its-kind self-propagating npm worm that harvested credentials and automatically infected packages owned by compromised maintainers.

### GitHub Repository URLs
- **No specific analysis repositories** - Research published via security vendors
- **Affected organization repos**: PostHog, Postman, Zapier, AsyncAPI, ENS Domains

### DMCA/Takedown Status
- **DMCA Status**: N/A - Malware removal
- **npm Response**: Removed malicious packages within hours
- **GitHub Response**: Removed attacker-created exfiltration repositories

### Wayback Machine / Archive Snapshots
- **ReversingLabs Report**: https://www.reversinglabs.com/blog/new-shai-hulud-worm-spreads-what-to-know
- **CISA Alert**: Referenced in 2025 advisories

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| Wave 1 packages removed | COMPLETED | Sep 2025 |
| Wave 2 packages removed | COMPLETED | Nov 2025 |
| CISA advisory issued | COMPLETED | Sep 2025 |
| GitHub exfiltration repos removed | COMPLETED | Nov 2025 |

### News Article URLs
1. https://www.reversinglabs.com/blog/new-shai-hulud-worm-spreads-what-to-know
2. https://blog.postman.com/engineering/root-cause-analysis-shai-halud-2-0/
3. https://www.esentire.com/security-advisories/new-npm-supply-chain-attack-identified-second-wave-of-shai-hulud
4. https://orca.security/resources/blog/shai-hulud-npm-malware-wave-2/
5. https://www.reversinglabs.com/blog/another-shai-hulud-npm-worm-is-spreading-heres-what-you-need-to-know
6. https://www.grandlinux.com/en/blogs/nodejs-supply-chain-attack.html
7. https://corgea.com/blog/here-s-what-happening-the-last-72-hours-700-packages-compromised-in-major-supply-chain-breach-november-25-2025
8. https://breached.company/shai-hulud-2-0-the-devastating-npm-supply-chain-attack-threatening-developer-ecosystems/

### Compromised Packages (Wave 2 - 796 packages)
- @asyncapi/specs (1.4M weekly downloads)
- @ctrl/tinycolor (2.2M weekly downloads)
- @postman/tunnel-agent
- posthog-node, posthog-js
- @zapier/zapier-sdk
- @ensdomains/ens-validation

---

## INCIDENT G: AXIOS NPM HIJACK
### Date: March 31, 2026

### Overview
Attacker compromised npm account of lead axios maintainer (jasonsaayman) and published malicious versions (1.14.1, 0.30.4) containing a phantom dependency that installed cross-platform RAT.

### GitHub Repository URLs
| Repository | URL | Status |
|------------|-----|--------|
| axios/axios (Official) | https://github.com/axios/axios | CLEAN |
| gist.github.com/N3mes1s | https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6 | IOC Analysis |

### DMCA/Takedown Status
- **DMCA Status**: N/A - Attacker-controlled, not IP violation
- **npm Response**: Removed malicious versions within ~3 hours
- **Attacker Accounts**: jasonsaayman (suspended), nrwise (suspended)

### Wayback Machine / Archive Snapshots
- **N/A** - Incident duration too short for archival

### CDN URLs / IOCs
| Indicator | Type | Status |
|-----------|------|--------|
| sfrclak[.]com:8000 | C2 Server | ACTIVE |
| 142.11.206.73 | C2 IP | ACTIVE |
| plain-crypto-js@4.2.1 | Malicious Package | REMOVED |
| npm package archive | npm registry | SECURITY HOLD |

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| axios@1.14.1 removed | COMPLETED | Mar 31, 2026 |
| axios@0.30.4 removed | COMPLETED | Mar 31, 2026 |
| plain-crypto-js replaced with security stub | COMPLETED | Mar 31, 2026 |
| Attacker accounts suspended | COMPLETED | Mar 31, 2026 |

### News Article URLs
1. https://www.techzine.eu/news/security/140082/axios-npm-package-compromised-posing-a-new-supply-chain-threat/
2. https://snyk.io/blog/axios-npm-package-compromised-supply-chain-attack-delivers-cross-platform/
3. https://www.socradar.io/blog/axios-npm-supply-chain-attack-2026-ciso-guide/
4. https://www.endorlabs.com/learn/npm-axios-compromise
5. https://techcrunch.com/2026/03/31/hacker-hijacks-axios-open-source-project-used-by-millions-to-push-malware/
6. https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html
7. https://www.theregister.com/2026/03/31/axios_npm_backdoor_rat/
8. https://www.aikido.dev/blog/axios-npm-compromised-maintainer-hijacked-rat
9. https://www.huntress.com/blog/supply-chain-compromise-axios-npm-package

### Technical Indicators
- **Malicious versions**: axios@1.14.1, axios@0.30.4
- **Phantom dependency**: plain-crypto-js@4.2.1
- **C2 Domain**: sfrclak[.]com:8000/6202033
- **Attacker email**: ifstap@proton.me (jasonsaayman), nrwise@proton.me

---

## INCIDENT H: XAI/GROK API KEY EXPOSURE
### Date: March 2, 2025 (discovered); July 13, 2025 (second leak)

### Overview
xAI employee(s) accidentally exposed API keys on GitHub, granting access to 52-60+ unreleased LLMs including models fine-tuned on SpaceX, Tesla, and Twitter/X data.

### GitHub Repository URLs
- **Original leak**: Public repository (removed, name not disclosed)
- **Second leak (DOGE employee)**: agent.py repository (removed)

### DMCA/Takedown Status
- **DMCA Status**: N/A - Repository removed by owner
- **GitGuardian Response**: Automated alert sent March 2, 2025
- **xAI Response**: Key remained valid for ~2 months; revoked after escalation

### Wayback Machine / Archive Snapshots
- **Krebs on Security Report**: https://krebsonsecurity.com/2025/05/xai-dev-leaks-api-key-for-private-spacex-tesla-llms/
- **GitGuardian Blog**: https://blog.gitguardian.com/xai-secret-leak-disclosure/

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| First leak discovered | REPORTED | Mar 2, 2025 |
| First leak revoked | COMPLETED | Apr 30, 2025 |
| Second leak (DOGE) | REPORTED | Jul 13, 2025 |
| Second leak repository removed | COMPLETED | Jul 2025 |

### News Article URLs
1. https://krebsonsecurity.com/2025/05/xai-dev-leaks-api-key-for-private-spacex-tesla-llms/
2. https://blog.gitguardian.com/xai-secret-leak-disclosure/
3. https://threats.wiz.io/all-incidents/xai-leaked-api-key
4. https://www.rescana.com/post/xai-developer-s-api-key-leak-exposes-spacex-and-tesla-s-private-llms
5. https://cyberpress.org/xai-dev-accidentally-leaks/
6. https://www.techradar.com/pro/security/doge-employee-with-sensitive-database-access-leaks-private-xai-api-key
7. https://coastlinecyber.com/doge-denizen-marko-elez-leaked-api-key-for-xai/
8. https://www.flyingpenguin.com/krebs-on-xai-unsafe-for-months/

### Exposed Models
- grok-2.5V (unreleased)
- research-grok-2p5v-1018 (development)
- tweet-rejector (internal tool)
- grok-spacex-2024-11-04
- grok-tesla models
- grok-4-0709
- Total: 52-60+ models

---

## INCIDENT I: HUGGINGFACE TOKEN EXPOSURE
### Date: December 2023 (Lasso Security Research)

### Overview
Lasso Security researchers discovered 1,681 valid Hugging Face API tokens exposed on Hugging Face and GitHub, granting access to 723 organizations including Meta, Microsoft, Google, and VMware.

### GitHub Repository URLs
- **Lasso Security Research**: https://github.com/lasso-security (research organization)
- **Meta-Llama, Bloom, Pythia**: Official model repositories

### DMCA/Takedown Status
- **DMCA Status**: N/A - Research disclosure, not infringement
- **Hugging Face Response**: Invalidated exposed tokens, deprecated org_api tokens
- **Organization Response**: Meta, Google, Microsoft, VMware revoked tokens same day

### Wayback Machine / Archive Snapshots
- **Lasso Security Report**: https://www.lasso.security/blog/1500-huggingface-api-tokens-were-exposed-leaving-millions-of-meta-llama-bloom-and-pythia-users-for-supply-chain-attacks
- **Original research archived**: Available via web archive

### Remediation Status
| Item | Status | Date |
|------|--------|------|
| Exposed tokens invalidated | COMPLETED | Dec 2023 |
| org_api tokens deprecated | COMPLETED | Dec 2023 |
| Fine-grained tokens introduced | COMPLETED | 2024 |
| GitHub secret scanning partnership | ACTIVE | Ongoing |

### News Article URLs
1. https://www.lasso.security/blog/1500-huggingface-api-tokens-were-exposed-leaving-millions-of-meta-llama-bloom-and-pythia-users-for-supply-chain-attacks
2. https://www.theregister.com/2023/12/04/exposed_hugging_face_api_tokens/
3. https://www.securityweek.com/major-organizations-using-hugging-face-ai-tools-put-at-risk-by-leaked-api-tokens/
4. https://www.reversinglabs.com/blog/5-lessons-learned-from-the-huggingface-api-breach
5. https://entro.security/blog/6-infamous-cybersecurity-leaks-of-2023/
6. https://www.scworld.com/brief/exposed-hugging-face-api-tokens-could-compromise-major-orgs

### Statistics
- **1,681 valid tokens exposed**
- **723 organizations affected**
- **655 tokens with write permissions**
- **77 organizations with full repository control**
- **10,000+ private models accessible**
- **2,500+ datasets accessible**

---

## APPENDIX A: ACRONYMS AND DEFINITIONS

| Term | Definition |
|------|------------|
| CDN | Content Delivery Network |
| C2 | Command and Control |
| CMS | Content Management System |
| CVE | Common Vulnerabilities and Exposures |
| DMCA | Digital Millennium Copyright Act |
| IOC | Indicator of Compromise |
| npm | Node Package Manager |
| PyPI | Python Package Index |
| R2 | Cloudflare R2 Storage |
| RAT | Remote Access Trojan |

## APPENDIX B: METHODOLOGY

This audit was conducted using:
1. Public web search for reported incidents
2. GitHub repository enumeration
3. Security vendor research reports
4. News media coverage analysis
5. Official vendor responses and advisories

## APPENDIX C: LEGAL DISCLAIMER

This document is compiled for educational and security research purposes under fair use doctrine (17 U.S.C. Section 107). All information is sourced from publicly available materials. No access controls were circumvented. Repository listings do not constitute endorsement or encouragement of unauthorized distribution of proprietary code.

---

**END OF AUDIT REPORT**
**Classification: PUBLIC - EDUCATIONAL/RESEARCH**
**IEEE Code of Ethics Section 1.2 Compliance: ACKNOWLEDGED**
**NIST SP 800-61 Alignment: INCIDENT RESPONSE DOCUMENTATION**
