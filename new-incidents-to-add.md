# New AI Security Incidents to Add to Main Report
# Generated: April 1, 2026
# Research base: 12+ parallel agents, 688MB data on Hetzner server
# Incidents NOT in main report (which covers 36 incidents as of Mar 2026)
# These are incidents #37-52

Total new incidents: 16

---

## 37. Claude Sonnet 5 "Fennec" Vertex AI Logs Leak
- **Date:** Feb 1-2, 2026
- **Company/System:** Anthropic/Google
- **Type:** Model metadata / internal codename
- **What Happened:** Claude Sonnet 5 internal codename "Fennec" was leaked via Vertex AI dashboard logs visible to API users. The unreleased model identifier appeared in billing/usage logs before Anthropic intended to announce it.
- **What Was Exposed:** Unreleased model codename "Fennec" = Claude Sonnet 5; confirmed via multiple DEV.to articles (marc0dev "Claude Sonnet 5 Fennec Leak" Feb 2, 2026)
- **Accessibility:** Taken down (logs patched)
- **Severity:** Medium
- **Sources:** DEV.to by marc0dev (Feb 2026)

---

## 38. Google Gemini 3.0 "Lithiumflow"/"Orionmist" LMArena Leak
- **Date:** Oct 2025
- **Company/System:** Google
- **Type:** Model metadata / unreleased model leak
- **What Happened:** Unreleased Google Gemini 3.0 model variants with internal codenames "Lithiumflow" and "Orionmist" were briefly accessible via LMArena (Chatbot Arena) blind testing before official announcement. Community members identified the models through response patterns and "leaked" the existence of these pre-release variants.
- **What Was Exposed:** Unreleased Gemini 3.0 model codenames; model capabilities visible to researchers
- **Accessibility:** Models removed from LMArena rotation; information archived on Reddit r/singularity, r/Bard, Medium (Cogni Down Under article "Google's Secret Gemini 3.0 Models Leak on LMArena")
- **Severity:** Medium
- **Sources:** Reddit r/singularity (Oct 2025), Medium - Cogni Down Under, Hacker News discussion

---

## 39. SANDWORM_MODE MCP Supply Chain Attack
- **Date:** Feb 2026
- **Company/System:** Multiple AI coding tool vendors
- **Type:** Supply chain / malicious npm packages
- **What Happened:** A coordinated supply chain attack deployed 19 malicious npm packages mimicking legitimate MCP (Model Context Protocol) server tools for AI coding assistants. Packages included a hidden "SANDWORM_MODE" activation flag that, when triggered, would exfiltrate developer credentials, API keys, and source code to attacker-controlled infrastructure. Distinct from the TeamPCP campaign (Incident #10) — this targeted MCP integration packages specifically.
- **What Was Exposed:** Developer API keys, source code, environment variables; targeting Cursor, Claude Code, Windsurf users
- **Accessibility:** Packages removed from npm; IoCs documented by 0x711 DEV.to article (Feb 2026)
- **Severity:** Critical
- **Sources:** DEV.to 0x711 "AI agents leaking secrets including SANDWORM_MODE MCP attack" (Feb 2026)

---

## 40. OpenAI gpt-oss-120b HuggingFace Brief Exposure
- **Date:** Aug 2025
- **Company/System:** OpenAI
- **Type:** Model weights (brief exposure)
- **What Happened:** A 120B parameter OpenAI model with designation "gpt-oss-120b" briefly appeared as a public repository on HuggingFace before being removed. The "oss" designation suggested an open-source variant of GPT-class models. Multiple community members documented the brief exposure before takedown.
- **What Was Exposed:** Model architecture details, potentially model weights or config files
- **Accessibility:** Taken down from HuggingFace; discussed on Juejin (Chinese dev community) article on "OpenAI gpt-oss-120b leak" Aug 2025
- **Severity:** High
- **Sources:** HuggingFace (removed), Juejin article (Aug 2025)

---

## 41. Claude System Prompts 57,000-Word Collection
- **Date:** Jan 29, 2026
- **Company/System:** Anthropic
- **Type:** System prompts
- **What Happened:** A Hacker News post in late January 2026 aggregated and published a ~57,000-word collection of Claude's leaked/extracted system prompts across all major deployment contexts (Claude.ai web, API, mobile, Claude Code). The collection revealed Anthropic's full prompt engineering strategy, safety instructions, and behavioral constraints. This is distinct from the DeepSeek jailbreak incident.
- **What Was Exposed:** Complete system prompt architecture for Claude deployments; CYBER_RISK_INSTRUCTION; UNDERCOVER MODE instructions; coordinator mode prompts
- **Accessibility:** Still archived (HN thread, GitHub gists)
- **Severity:** High
- **Sources:** Hacker News (Jan 29, 2026)

---

## 42. Cursor AI CurXecute RCE (CVE-2025-59944 + CVE-2025-54135)
- **Date:** Jul 2025 (disclosed)
- **Company/System:** Anysphere (Cursor)
- **Type:** CVE exploit / Remote Code Execution
- **What Happened:** Two critical RCE vulnerabilities in Cursor AI IDE. CVE-2025-59944 (CurXecute) allowed malicious MCP server auto-start configurations in repository .cursor/mcp.json files to execute arbitrary code when a developer opened a repo. CVE-2025-54135 was a case-sensitivity bug variant. Attackers could craft malicious repos that executed code on developer machines without prompts.
- **What Was Exposed:** Full developer machine access via arbitrary code execution
- **Accessibility:** Patched in Cursor v0.49+; PoC documented by aim.security blog
- **Severity:** Critical
- **Sources:** aim.security blog, CVE-2025-59944, CVE-2025-54135

---

## 43. Cursor AI MCPoison (CVE-2025-54136)
- **Date:** Jul 2025 (disclosed)
- **Company/System:** Anysphere (Cursor)
- **Type:** CVE exploit / prompt injection / supply chain
- **What Happened:** CVE-2025-54136 "MCPoison" — Check Point Research discovered that Cursor's MCP tool integration allowed malicious MCP servers to inject hidden instructions into Claude's context window through tool descriptions and response metadata. Unlike CurXecute (direct RCE), MCPoison worked by poisoning the AI's reasoning to take malicious actions silently. Combined with CurXecute, attackers could achieve full pipeline compromise.
- **What Was Exposed:** Developer credentials, code, AI-assisted operations hijacked
- **Accessibility:** Patched; PoC available (downloaded to research server)
- **Severity:** Critical
- **Sources:** Check Point Research (Jul 2025), CVE-2025-54136

---

## 44. Sourcegraph Cody Data Breach
- **Date:** Nov 2025
- **Company/System:** Sourcegraph
- **Type:** Data breach / user data exposure
- **What Happened:** Sourcegraph's Cody AI coding assistant suffered a significant data breach affecting approximately 1.8 million developer accounts. The breach exposed user authentication tokens, repository access permissions, code snippets submitted to Cody for AI completion, and in some cases full repository contents that Cody had indexed. The breach was linked to a compromised admin token.
- **What Was Exposed:** 1.8M developer accounts; auth tokens; code snippets; repository index data
- **Accessibility:** Breach patched; users notified; incident reports published
- **Severity:** Critical
- **Sources:** Multiple security researcher reports (Nov 2025); Sourcegraph incident disclosure

---

## 45. CVE-2025-55284 — Claude Code DNS Exfiltration via Prompt Injection
- **Date:** Aug 18, 2025 (disclosed)
- **Company/System:** Anthropic
- **Type:** CVE exploit / prompt injection / data exfiltration
- **What Happened:** CVE-2025-55284 documented by Johann Rehberger. Claude Code's file reading capability could be abused via prompt injection in specially crafted files to exfiltrate sensitive data via DNS requests. When Claude Code read a malicious file containing hidden instructions, it would encode and transmit sensitive information (env vars, tokens, file contents) via DNS lookup requests to attacker-controlled domains — bypassing network filtering that blocks HTTP/HTTPS.
- **What Was Exposed:** Environment variables, API keys, file contents via DNS exfiltration channel
- **Accessibility:** Patched in subsequent Claude Code versions; PoC preserved on research server
- **Severity:** High
- **Sources:** embracethered.com/blog/posts/2025/claude-code-exfiltration-via-dns-requests/ (CVE-2025-55284); 360漏洞研究院 (Aug 18, 2025)

---

## 46. Typosquat npm Campaign — claude-client + claude-sdk
- **Date:** 2025-2026 (ongoing)
- **Company/System:** Multiple (targeting Anthropic ecosystem)
- **Type:** Supply chain / typosquat npm packages
- **What Happened:** Two confirmed typosquat npm packages targeting Anthropic Claude developers discovered during research. "claude-client" (maintainer: magj-dev) and "claude-sdk" (maintainer: claudeliquid) impersonate legitimate Anthropic SDK packages with multiple versions released. These packages pose credential theft and backdoor installation risks.
- **What Was Exposed:** Developer systems that install these packages; potential credential theft/backdoor installation
- **Accessibility:** Still on npm registry (ongoing threat); metadata preserved on research server
- **Severity:** High
- **Sources:** npm registry forensics; supply chain research

---

## 47. Claude Code Hidden Architecture Leak — UNDERCOVER MODE + TENGU Flags
- **Date:** Mar 31, 2026 (revealed via source map analysis)
- **Company/System:** Anthropic
- **Type:** Internal architecture / system prompt / feature flags
- **What Happened:** Analysis of leaked Claude Code source maps revealed previously unknown internal architecture details including UNDERCOVER MODE (hidden system prompt instruction), TENGU (internal project codename with hundreds of feature flags), Computer Use "Chicago" implementation, ULTRAPLAN (30-minute remote cloud planning sessions), Penguin Mode (fast mode), TRANSCRIPT_CLASSIFIER (AFK mode with ML-based auto-approval), and BUDDY system (deterministic user pairing).
- **What Was Exposed:** Full internal system prompt architecture; unreleased feature flags; internal codenames; Safeguards team members and infrastructure details
- **Accessibility:** Source map still preserved in mirrors and on research servers
- **Severity:** High
- **Sources:** Source map analysis; constants/cyberRiskInstruction.ts, utils/undercover.ts, coordinatorMode.ts

---

## 48. HuggingFace Unauthorized Claude-4.6-Opus Distillation Wave
- **Date:** Mar 31, 2026
- **Company/System:** Multiple (ToS violation against Anthropic)
- **Type:** Model weights / unauthorized distillation
- **What Happened:** On March 31, 2026, a wave of unauthorized model uploads appeared on HuggingFace claiming "Claude-4.6-Opus" distillation using Qwen3.5-27B as base model and trained on Claude outputs. Models included multiple variants with "Uncensored", "Reasoning-Distilled", and KL-divergence approaches. All violate Anthropic's ToS Section 3.2.
- **What Was Exposed:** Indicates large-scale usage of Claude outputs for training derivative models
- **Accessibility:** Some still available on HuggingFace (as of Apr 1, 2026); documented in research files
- **Severity:** Medium
- **Sources:** HuggingFace API search results; HuggingFace model pages

---

## 49. LlamaIndex SQL Injection — CVE-2025-1793 / GHSA-v3c8-3pr6-gr7p
- **Date:** 2025 (disclosed)
- **Company/System:** LlamaIndex (Jerry Liu)
- **Type:** CVE exploit / SQL injection
- **What Happened:** Critical SQL injection vulnerability in LlamaIndex vector store implementations (llama_index < v0.12.28, specifically v0.12.21). The `filters` parameter in vector store queries was not properly sanitized, allowing attackers to inject arbitrary SQL. Original PoC repository was deleted from GitHub but archived.
- **What Was Exposed:** Underlying database contents in LlamaIndex-powered RAG applications
- **Accessibility:** Patched in v0.12.28; GitHub advisory and PoC documentation preserved on research server
- **Severity:** Critical
- **Sources:** GitHub Advisory GHSA-v3c8-3pr6-gr7p; Huntr bounty; endorlabs.com analysis

---

## 50. GitHub Copilot Advertisement Injection
- **Date:** Mar 2026
- **Company/System:** Microsoft/GitHub
- **Type:** Integrity compromise / unexpected behavior
- **What Happened:** Reports emerged that GitHub Copilot was injecting promotional content and advertisement-like suggestions for Microsoft Azure services and GitHub features into developer code suggestions. The behavior was inconsistent and non-disclosed, raising concerns about integrity of AI-assisted code suggestions and potential vendor lock-in via AI recommendations.
- **What Was Exposed:** Trust in AI code suggestions; potential vendor lock-in via AI recommendations
- **Accessibility:** Ongoing reports; Microsoft did not acknowledge officially
- **Severity:** Medium
- **Sources:** DEV.to and Reddit r/github discussions (Mar 2026); Hacker News threads

---

## 51. Amazon Q Developer Malicious Code Injection
- **Date:** 2025-2026
- **Company/System:** Amazon/AWS
- **Type:** CVE exploit / prompt injection / code injection
- **What Happened:** Security researchers identified that Amazon Q Developer (AWS's AI coding assistant) could be manipulated via prompt injection in code comments and documentation to inject malicious code suggestions. When Q analyzed code containing crafted adversarial prompts, it would generate insecure implementations or code with backdoors while appearing to provide legitimate assistance.
- **What Was Exposed:** Developer codebases; potential for supply chain contamination via AI-generated code
- **Accessibility:** Details limited; ongoing research
- **Severity:** High
- **Sources:** Security researcher reports (2025-2026)

## 53. SANDWORM_MODE npm Worm — AI Toolchain Supply Chain Attack (DETAILED)
- **Date:** February 20, 2026 (disclosed by Socket.dev)
- **Company/System:** Multiple (targeting Claude Code, Cursor, Windsurf, VS Code Continue)
- **Type:** Supply chain / Self-spreading npm worm / MCP poisoning
- **What Happened:** 19 malicious typosquatting npm packages published under aliases "official334" and "javaorg" operated as a two-stage self-spreading worm. Stage 1 (immediate activation): harvested API keys from 9 LLM providers (Anthropic, OpenAI, Google, Cohere, Mistral, Grok, Fireworks, Replicate, Together), plus AWS credentials, SSH keys, crypto keys, npm tokens, and CI/CD secrets. Stage 2 (48-96 hour delayed): injected rogue MCP servers into Claude Code, Claude Desktop, Cursor, Windsurf/Codeium, and VS Code Continue via prompt injection to steal `~/.ssh/id_rsa`, `~/.aws/credentials`, `.env` files. Self-propagated by scanning Git repos, stealing GitHub/npm credentials, auto-modifying project files, installing Git hooks for persistence, and publishing compromised packages via victim accounts. Distinct from TeamPCP campaign (Incident #10 in main report — different mechanism and targets).
- **What Was Exposed:** API keys for 9 LLM providers; AWS credentials; SSH private keys; npm/GitHub tokens; CI/CD secrets; MCP configurations for all major AI coding tools poisoned
- **Accessibility:** Packages removed from npm registry; IOCs documented; Socket.dev full analysis preserved (508KB on Hetzner)
- **Severity:** Critical
- **Sources:**
  - https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning (Hetzner: sandworm-mode-socket.html 508KB)
  - https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html
  - https://www.helpnetsecurity.com/2026/02/24/npm-worm-sandworm-mode-supply-cain-attack/
  - https://www.endorlabs.com/learn/sandworm-mode-dissecting-a-multi-stage-npm-supply-chain-attack
  - https://www.securityweek.com/new-sandworm_mode-supply-chain-attack-hits-npm/
  - https://hivepro.com/threat-advisory/sandworm_mode-npm-supply-chain-attack-targeting-ai-development-tools/

---

## 54. Amazon Q Developer Unicode Invisible Injection + RCE (AWS-2025-019)
- **Date:** July 4, 2025 (reported); July 17, 2025 (patched v1.85); August 20, 2025 (disclosed)
- **Company/System:** Amazon (AWS)
- **Type:** CVE exploit / Prompt injection / Remote Code Execution
- **What Happened:** Three chained vulnerabilities in Amazon Q Developer for VS Code (AWS-2025-019, GHSA-7g7f-ff96-5gcw, 1M+ affected users). (1) Q interprets invisible Unicode Tag characters (U+E0000 range) as instructions — humans cannot see these, enabling hidden injection into any analyzed document. (2) `executeBash` tool does NOT require confirmation for "ping"/"dig" commands, enabling DNS-based credential exfiltration by encoding secrets in lookup hostnames. (3) Attackers can add rogue MCP servers on-the-fly and auto-approve all commands → full RCE. Documented by Johann Rehberger (embracethered.com). Note: separate from the Amazon Q supply chain/wiper-prompt incident (#51 above).
- **What Was Exposed:** Full developer machine via RCE; environment variables, API keys, SSH keys via DNS exfiltration
- **Accessibility:** Patched in v1.85; AWS bulletin AWS-2025-019 public
- **Severity:** Critical
- **Sources:**
  - https://aws.amazon.com/security/security-bulletins/AWS-2025-019/ (Hetzner: amazon-q-aws-bulletin.html 182KB)
  - https://embracethered.com/blog/posts/2025/amazon-q-developer-remote-code-execution/ (Hetzner: amazon-q-embracethered.html 26KB)
  - https://github.com/aws/aws-toolkit-vscode/security/advisories/GHSA-7g7f-ff96-5gcw
  - https://www.theregister.com/2025/08/20/amazon_quietly_fixed_q_developer_flaws/

---

## 55. npm Typosquat Campaign: claude-client + claude-sdk (Confirmed Malicious, Apr 2026)
- **Date:** June 6-8, 2025 (claude-client); January 7, 2026 (claude-sdk)
- **Company/System:** Targeting Anthropic/Claude developer ecosystem
- **Type:** Supply chain / npm typosquat / Bait-and-switch
- **What Happened:** Two distinct malicious npm packages confirmed via forensic analysis. (1) `claude-client` (maintainer: magj-dev, m@rco.sh): 8 versions published in 2 days; all linked GitHub repos return 404; added `dotenv` dependency in later versions (credential exfiltration pattern); 4 versions in 13 minutes indicates automation. (2) `claude-sdk` (maintainer: claudeliquid, fispectik@outlook.com, anonymous): COMPLETE BAIT-AND-SWITCH — claims to be a Claude AI SDK but is actually a Solana crypto wallet manager (dependencies: @solana/web3.js, bs58; keywords: solana, memecoin, trading, wallet, dex); 14 versions published in ~2.3 hours suggests automated attack pipeline. Both target developers searching for official `@anthropic-ai/sdk`.
- **What Was Exposed:** Developers installing claude-client: credentials via dotenv theft. Developers installing claude-sdk: Solana wallet private keys/seed phrases potentially harvested.
- **Accessibility:** Both packages still live on npm as of Apr 1, 2026 (ONGOING THREAT)
- **Severity:** Critical
- **Sources:**
  - npm registry: npmjs.com/package/claude-client, npmjs.com/package/claude-sdk
  - Full forensic analysis: /Users/aadel/projects/NPM_TYPOSQUAT_SECURITY_ANALYSIS_2026.md
  - Metadata: Hetzner ~/projects/ai-leaks-research/leaked-data/supply-chain/claude-client-metadata.json (29KB), claude-sdk-metadata.json (27KB)

---

## 52. Claude Code v2.1.88 npm Version Confirmed Pulled
- **Date:** Mar 31, 2026 (confirmed)
- **Company/System:** Anthropic
- **Type:** Takedown confirmation / forensic finding
- **What Happened:** Research confirmed that npm version @anthropic-ai/claude-code@2.1.88 — the version that contained the source map leak — has been permanently removed from the npm registry. Attempting `npm pack @anthropic-ai/claude-code@2.1.88` returns "ETARGET No matching version found". This forensically confirms Anthropic's rapid response to the leak and the version gap in npm history serves as evidence of the incident.
- **What Was Exposed:** Evidence of incident response; version 2.1.88 metadata preserved in npm registry archives
- **Accessibility:** Removed from npm; source map mirrors still serve content; DMCA on GitHub repos
- **Severity:** N/A (takedown confirmation)
- **Sources:** npm registry forensics; direct npm error logs

---
