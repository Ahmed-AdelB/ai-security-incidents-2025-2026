# Claude Code NPM Source Map Leak - Technical Analysis

**Author:** Ahmed Adel Bakr Alderai  
**Date:** April 4, 2026  
**Classification:** Security Research Analysis  
**Document Version:** 1.0

---

## Executive Summary

This document provides a comprehensive technical analysis of the **Claude Code npm source map leak** that occurred on **March 31, 2026** (version 2.1.88). The leak exposed **1,332 TypeScript files** (~512,000 lines, 33MB) of Anthropic's Claude Code CLI source code through source map files included in the npm package.

### Key Findings at a Glance

| Metric | Value |
|--------|-------|
| **Total Files** | 1,902 files |
| **TypeScript/TSX Files** | 1,884 files |
| **Total Lines of Code** | ~512,685 lines |
| **Package Size** | 33 MB (src/ directory only) |
| **Tool Definitions** | 43+ distinct tools |
| **Internal Codenames Discovered** | Capybara, Tengu, Kairos, Numbat, etc. |
| **Beta Feature Flags** | 50+ feature flags identified |

---

## 1. What Is This Leak?

### 1.1 Nature of the Leak

The leak consists of **TypeScript source code** extracted from source map (`.js.map`) files that were inadvertently included in the Claude Code npm package distribution. Source maps are normally used for debugging to map minified JavaScript back to its original TypeScript source.

### 1.2 Version and Timeline

- **Package:** `@anthropic-ai/claude-code`
- **Version:** 2.1.88
- **Leak Date:** March 31, 2026
- **Source Extraction:** Completed from `src_extracted/src/` directory

### 1.3 Legal and Ethical Context

This analysis is conducted for **security research purposes** under responsible disclosure principles. The source code has been publicly available via npm since March 31, 2026, making this analysis of publicly accessible artifacts.

---

## 2. Architecture Overview

### 2.1 High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLAUDE CODE CLI v2.1.88                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   REPL/CLI   │  │   Bridge     │  │   Assistant (KAIROS) │  │
│  │   Interface  │  │   (Remote)   │  │   Background Mode    │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│         │                  │                     │              │
│         └──────────────────┼─────────────────────┘              │
│                            │                                    │
│                   ┌────────▼────────┐                          │
│                   │   Query Engine  │                          │
│                   │   (Main Loop)   │                          │
│                   └────────┬────────┘                          │
│                            │                                    │
│         ┌──────────────────┼──────────────────┐                │
│         │                  │                  │                │
│  ┌──────▼──────┐  ┌────────▼────────┐  ┌──────▼──────┐         │
│  │   Tools     │  │   Agent System  │  │   Skills    │         │
│  │  (43+)      │  │  (Subagents)    │  │  (Bundled)  │         │
│  └─────────────┘  └─────────────────┘  └─────────────┘         │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Core Services Layer                        │    │
│  │  • MCP (Model Context Protocol)                         │    │
│  │  • LSP (Language Server Protocol)                       │    │
│  │  • Telemetry & Analytics                                │    │
│  │  • GrowthBook (Feature Flags)                           │    │
│  │  • OAuth & Authentication                               │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Key Module Structure

| Directory | Files | Purpose |
|-----------|-------|---------|
| `src/tools/` | 43+ tool implementations | Core tool system (Bash, FileEdit, WebSearch, etc.) |
| `src/commands/` | 101 command definitions | CLI slash commands and handlers |
| `src/components/` | 146 React/Ink components | Terminal UI components |
| `src/services/` | 38 service modules | API clients, MCP, LSP, telemetry |
| `src/constants/` | 23 constant files | System prompts, beta flags, limits |
| `src/utils/` | 100+ utility modules | Helper functions and utilities |
| `src/bridge/` | 32 bridge modules | Remote session support |
| `src/skills/` | Skill system | Bundled and user-defined skills |
| `src/buddy/` | Companion system | Interactive avatar/sprites |
| `src/hooks/` | 87 hook modules | React-style hooks for CLI |

---

## 3. Tool System Analysis

### 3.1 Complete Tool Inventory (43+ Tools)

Claude Code's capability is exposed through a comprehensive tool system. The following tools have been identified:

#### Core File Operations
| Tool | Description | Safety Level |
|------|-------------|--------------|
| `FileReadTool` | Read file contents with line limits | Read-only |
| `FileEditTool` | Edit existing files | Destructive |
| `FileWriteTool` | Create new files | Destructive |
| `GlobTool` | Search for files by pattern | Read-only |
| `GrepTool` | Search file contents with regex | Read-only |
| `NotebookEditTool` | Edit Jupyter notebooks | Destructive |

#### Shell Execution
| Tool | Description | Safety Level |
|------|-------------|--------------|
| `BashTool` | Execute bash commands | Potentially destructive |
| `PowerShellTool` | Execute PowerShell (Windows) | Potentially destructive |
| `REPLTool` | JavaScript/TypeScript REPL | Sandboxed execution |

#### Web and Search
| Tool | Description | Notes |
|------|-------------|-------|
| `WebSearchTool` | Web search via API | Max 8 searches per session |
| `WebFetchTool` | Fetch URL content | - |
| `WebBrowserTool` | *Beta feature* | Full browser automation |

#### Agent System
| Tool | Description | Notes |
|------|-------------|-------|
| `AgentTool` | Spawn subagents | Supports fork mode |
| `TaskCreateTool` | Create async tasks | Todo v2 system |
| `TaskGetTool` | Get task status | - |
| `TaskUpdateTool` | Update tasks | - |
| `TaskListTool` | List all tasks | - |
| `TaskStopTool` | Stop running tasks | - |
| `TaskOutputTool` | Output aggregation | - |

#### Communication & User Interaction
| Tool | Description | Notes |
|------|-------------|-------|
| `AskUserQuestionTool` | Interactive prompts | Permission dialogs |
| `SendMessageTool` | Send messages to teammates | Agent swarms |
| `BriefTool` | Generate brief summaries | *KAIROS feature* |

#### MCP (Model Context Protocol)
| Tool | Description | Notes |
|------|-------------|-------|
| `MCPTool` | Generic MCP tool wrapper | Dynamic schema |
| `ListMcpResourcesTool` | List MCP resources | - |
| `ReadMcpResourceTool` | Read MCP resources | - |
| `McpAuthTool` | MCP authentication | - |

#### Advanced Features
| Tool | Description | Feature Flag |
|------|-------------|--------------|
| `SkillTool` | Execute user skills | - |
| `ConfigTool` | Configuration management | `USER_TYPE === 'ant'` |
| `TungstenTool` | Internal terminal tool | `USER_TYPE === 'ant'` |
| `LSPTool` | Language Server Protocol | `ENABLE_LSP_TOOL` |
| `SleepTool` | Autonomous sleep | `PROACTIVE` or `KAIROS` |
| `ScheduleCronTool` | Cron scheduling | `AGENT_TRIGGERS` |
| `RemoteTriggerTool` | Remote agent triggers | `AGENT_TRIGGERS_REMOTE` |
| `MonitorTool` | Process monitoring | `MONITOR_TOOL` |
| `TerminalCaptureTool` | Terminal capture | `TERMINAL_PANEL` |
| `ToolSearchTool` | Dynamic tool search | *Conditional* |
| `SnipTool` | History snipping | `HISTORY_SNIP` |
| `WorkflowTool` | Workflow scripts | `WORKFLOW_SCRIPTS` |
| `TeamCreateTool` | Create agent teams | `AGENT_SWARMS` |
| `TeamDeleteTool` | Delete agent teams | `AGENT_SWARMS` |
| `SendUserFileTool` | Send files to user | `KAIROS` |
| `PushNotificationTool` | Push notifications | `KAIROS_PUSH_NOTIFICATION` |
| `SubscribePRTool` | PR webhook subscription | `KAIROS_GITHUB_WEBHOOKS` |

#### Mode Management
| Tool | Description | Notes |
|------|-------------|-------|
| `EnterPlanModeTool` | Enter planning mode | Hides tool calls |
| `ExitPlanModeV2Tool` | Exit planning mode | - |
| `EnterWorktreeTool` | Enter git worktree | Git worktree support |
| `ExitWorktreeTool` | Exit git worktree | - |

#### Testing & Internal
| Tool | Description | Notes |
|------|-------------|-------|
| `TestingPermissionTool` | Test permission system | Test-only |
| `SyntheticOutputTool` | Synthetic tool output | Internal |
| `TodoWriteTool` | Legacy todo system | Deprecated |

### 3.2 Tool Architecture

Each tool follows a standardized interface defined in `Tool.ts`:

```typescript
interface Tool<Input, Output, Progress> {
  name: string;
  aliases?: string[];
  description: (input, options) => Promise<string>;
  inputSchema: z.ZodType;
  outputSchema?: z.ZodType;
  
  // Execution
  call(args, context, canUseTool, parentMessage, onProgress): Promise<ToolResult<Output>>;
  
  // Safety properties
  isEnabled(): boolean;
  isReadOnly(input): boolean;
  isDestructive?(input): boolean;
  isConcurrencySafe(input): boolean;
  
  // Permission system
  checkPermissions(input, context): Promise<PermissionResult>;
  validateInput?(input, context): Promise<ValidationResult>;
  
  // UI rendering
  renderToolUseMessage(input, options): React.ReactNode;
  renderToolResultMessage?(content, progressMessages, options): React.ReactNode;
}
```

---

## 4. Internal Codenames and Secrets

### 4.1 Model Codenames

The source reveals several internal model codenames used at Anthropic:

| Codename | Likely Model | Evidence |
|----------|--------------|----------|
| **Capybara** | Claude Opus/Internal variant | Referenced as model codename in prompts, buddy sprite |
| **Tengu** | Feature flag system | `tengu_*` prefix on all GrowthBook flags |
| **Numbat** | Upcoming model | Comment: "Remove this section when we launch numbat" |
| **Kairos** | Assistant/Background mode | Major feature flag for proactive agent |

### 4.2 Feature Flag System (TENGU)

Anthropic uses **GrowthBook** with the `tengu_` prefix for feature flags:

```typescript
// Examples from source:
feature('KAIROS')              // Background assistant mode
feature('PROACTIVE')           // Proactive agent behavior
feature('COORDINATOR_MODE')    // Multi-agent coordination
feature('AGENT_TRIGGERS')      // Cron/agent triggers
feature('TRANSCRIPT_CLASSIFIER') // Auto-mode classification
feature('COWORKER_TYPE_TELEMETRY') // Coworker type tracking
feature('CHICAGO_MCP')         // MCP improvements
feature('CONTEXT_COLLAPSE')    // Context management
feature('CACHED_MICROCOMPACT') // Micro-compaction caching
feature('TEAMMEM')             // Team memory sync
feature('WEB_BROWSER_TOOL')    // Browser automation
feature('UDS_INBOX')           // Unix domain socket inbox
feature('SSH_REMOTE')          // SSH remote sessions
feature('DIRECT_CONNECT')      // Direct connection mode
feature('BG_SESSIONS')         // Background sessions
feature('VOICE_MODE')          // Voice interaction
feature('LODESTONE')           // Unknown feature
feature('NATIVE_CLIENT_ATTESTATION') // Client attestation
feature('BREAK_CACHE_COMMAND') // Cache breaking
feature('TRANSCRIPT_CLASSIFIER') // AFK/Auto mode
```

### 4.3 Beta Headers

```typescript
CLAUDE_CODE_20250219_BETA_HEADER = 'claude-code-20250219'
INTERLEAVED_THINKING_BETA_HEADER = 'interleaved-thinking-2025-05-14'
CONTEXT_1M_BETA_HEADER = 'context-1m-2025-08-07'
CONTEXT_MANAGEMENT_BETA_HEADER = 'context-management-2025-06-27'
STRUCTURED_OUTPUTS_BETA_HEADER = 'structured-outputs-2025-12-15'
WEB_SEARCH_BETA_HEADER = 'web-search-2025-03-05'
TOOL_SEARCH_BETA_HEADER_1P = 'advanced-tool-use-2025-11-20'
TOOL_SEARCH_BETA_HEADER_3P = 'tool-search-tool-2025-10-19'
EFFORT_BETA_HEADER = 'effort-2025-11-24'
TASK_BUDGETS_BETA_HEADER = 'task-budgets-2026-03-13'
FAST_MODE_BETA_HEADER = 'fast-mode-2026-02-01'
REDACT_THINKING_BETA_HEADER = 'redact-thinking-2026-02-12'
TOKEN_EFFICIENT_TOOLS_BETA_HEADER = 'token-efficient-tools-2026-03-28'
AFK_MODE_BETA_HEADER = 'afk-mode-2026-01-31'
CLI_INTERNAL_BETA_HEADER = 'cli-internal-2026-02-09'
```

---

## 5. UNDERCOVER MODE - Security Feature

### 5.1 Purpose

**UNDERCOVER MODE** is a critical security feature designed to prevent leaks of Anthropic-internal information when employees contribute to public/open-source repositories.

### 5.2 Activation Logic

```typescript
function isUndercover(): boolean {
  if (process.env.USER_TYPE === 'ant') {
    if (isEnvTruthy(process.env.CLAUDE_CODE_UNDERCOVER)) return true
    // Auto: active unless in internal repo
    return getRepoClassCached() !== 'internal'
  }
  return false
}
```

### 5.3 Protections Applied

When active, UNDERCOVER MODE:

1. **Strips model codenames** from commit messages and PRs
2. **Hides internal project names** (e.g., `claude-cli-internal`)
3. **Removes unreleased model versions** (e.g., `opus-4-7`)
4. **Strips internal tooling references** (Slack channels, short links)
5. **Removes "Claude Code" attribution**
6. **Strips Co-Authored-By lines**

### 5.4 Undercover Instructions (from source)

```
## UNDERCOVER MODE — CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit
messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal
information. Do not blow your cover.

NEVER include:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
- Internal repo or project names
- Internal tooling, Slack channels, or short links
- The phrase "Claude Code" or any mention that you are an AI
- Any hint of what model or version you are
- Co-Authored-By lines
```

---

## 6. System Prompt Structure

### 6.1 Prompt Architecture

The system prompt is constructed dynamically with caching boundaries:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SYSTEM PROMPT STRUCTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STATIC SECTION (cacheable - cross-user)                │    │
│  │  • Introduction                                         │    │
│  │  • System instructions                                  │    │
│  │  • Coding guidelines                                    │    │
│  │  • Tool usage guidance                                  │    │
│  │  • Tone and style                                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           ↓                                      │
│              __SYSTEM_PROMPT_DYNAMIC_BOUNDARY__                  │
│                           ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  DYNAMIC SECTION (session-specific)                     │    │
│  │  • Session guidance                                     │    │
│  │  • Memory attachments                                   │    │
│  │  • Environment info                                     │    │
│  │  • Language preference                                  │    │
│  │  • Output style config                                  │    │
│  │  • MCP server instructions                              │    │
│  │  • Scratchpad instructions                              │    │
│  │  • Function result clearing                             │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Key System Prompt Sections

From `src/constants/prompts.ts`:

| Section | Purpose |
|---------|---------|
| `getSimpleIntroSection` | Identity and role definition |
| `getSimpleSystemSection` | Core system behavior |
| `getSimpleDoingTasksSection` | Coding style and task guidelines |
| `getActionsSection` | Risk assessment for actions |
| `getUsingYourToolsSection` | Tool usage guidance |
| `getAgentToolSection` | Subagent/fork guidance |
| `getSessionSpecificGuidanceSection` | Dynamic session guidance |
| `getOutputEfficiencySection` | Output length guidance |
| `getSimpleToneAndStyleSection` | Communication style |

### 6.3 Model-Specific Prompts

The system includes model-specific handling:
- **Capybara v8**: Special instructions for false-claims mitigation (29-30% FC rate)
- **Comment writing**: Adjusted for models prone to over-commenting
- **Assertiveness**: Counterweights for different model behaviors

---

## 7. Beta Features Identified

### 7.1 KAIROS - Background Assistant Mode

**KAIROS** is a major upcoming feature for autonomous background operation:

```typescript
// From main.tsx
const assistantModule = feature('KAIROS') 
  ? require('./assistant/index.js') 
  : null
```

Capabilities:
- Autonomous "tick" based operation
- Sleep/wake cycle management
- Background task execution
- Terminal focus awareness
- Push notifications

### 7.2 COORDINATOR_MODE - Multi-Agent Swarms

Enables hierarchical agent coordination:

```typescript
if (feature('COORDINATOR_MODE') && 
    isEnvTruthy(process.env.CLAUDE_CODE_COORDINATOR_MODE)) {
  // Enable coordinator with worker agents
}
```

### 7.3 AGENT_TRIGGERS - Cron and Remote

Scheduled and remote-triggered agent execution:

```typescript
const cronTools = feature('AGENT_TRIGGERS')
  ? [CronCreateTool, CronDeleteTool, CronListTool]
  : []
```

### 7.4 Proactive Mode (PROACTIVE/KAIROS)

Autonomous behavior without user prompts:

```typescript
if (feature('PROACTIVE') || feature('KAIROS')) {
  return [
    `You are an autonomous agent. Use the available tools to do useful work.`,
    // ... proactive instructions
  ]
}
```

### 7.5 WEB_BROWSER_TOOL - Browser Automation

```typescript
const WebBrowserTool = feature('WEB_BROWSER_TOOL')
  ? require('./tools/WebBrowserTool/WebBrowserTool.js').WebBrowserTool
  : null
```

---

## 8. The "Buddy" System

### 8.1 Overview

A companion/avatar system with collectible characters:

### 8.2 Species (from `src/buddy/types.ts`)

| Species | Rarity Levels | Notes |
|---------|---------------|-------|
| `duck`, `goose` | Common | Basic companions |
| `blob`, `cat` | Common | - |
| `penguin`, `turtle` | Common | - |
| `snail`, `ghost` | Uncommon | - |
| `axolotl` | Uncommon | - |
| `capybara` | Rare | **Model codename** |
| `cactus` | Rare | - |
| `robot` | Epic | - |
| `rabbit` | Epic | - |
| `mushroom` | Legendary | - |
| `chonk` | Legendary | - |
| `dragon`, `octopus`, `owl` | Various | - |

### 8.3 Character Stats

```typescript
STAT_NAMES = ['DEBUGGING', 'PATIENCE', 'CHAOS', 'WISDOM', 'SNARK']
```

---

## 9. Security Architecture Insights

### 9.1 Permission System

Multi-layered permission architecture:

```
┌─────────────────────────────────────────┐
│         PERMISSION SYSTEM                │
├─────────────────────────────────────────┤
│  1. Tool-level validation               │
│  2. Permission rules (alwaysAllow/Deny/Ask)│
│  3. Auto-mode classifier (TRANSCRIPT_CLASSIFIER)│
│  4. Hook system (pre/post tool use)     │
│  5. User confirmation dialogs           │
│  6. Sandbox enforcement                 │
└─────────────────────────────────────────┘
```

### 9.2 Sandbox System

File system and network sandboxing:

```typescript
interface SandboxConfig {
  fsRead: { denyOnly: string[], allowWithinDeny?: string[] }
  fsWrite: { allowOnly: string[], denyWithinAllow?: string[] }
  network: { allowedHosts?: string[], deniedHosts?: string[] }
  allowUnixSockets?: string[]
  ignoreViolations?: boolean
}
```

### 9.3 Internal vs External Builds

The codebase distinguishes between internal (`ant`) and external builds:

```typescript
// Dead code elimination for external builds
if (process.env.USER_TYPE === 'ant') {
  // Internal-only features
  // - TungstenTool
  // - ConfigTool
  // - REPLTool
  // - Internal beta features
}
```

### 9.4 Client Attestation

```typescript
// cch=00000 placeholder overwritten by Bun's HTTP stack
const cch = feature('NATIVE_CLIENT_ATTESTATION') ? ' cch=00000;' : ''
```

---

## 10. Notable File Paths and Revelations

### 10.1 Critical Source Files

| File Path | Revelation |
|-----------|------------|
| `src/main.tsx` | Main entry point (804KB!) - contains CLI bootstrap |
| `src/Tool.ts` | Core tool interface definition |
| `src/tools.ts` | Tool registry and assembly |
| `src/constants/prompts.ts` | System prompt construction |
| `src/constants/betas.ts` | All beta feature flags |
| `src/utils/undercover.ts` | UNDERCOVER MODE implementation |
| `src/services/analytics/growthbook.ts` | Feature flag system |
| `src/tools/AgentTool/` | Subagent system |
| `src/bridge/` | Remote session infrastructure |
| `src/buddy/` | Companion/avatar system |

### 10.2 Security-Relevant Files

| File | Purpose |
|------|---------|
| `src/utils/permissions/` | Permission system implementation |
| `src/utils/sandbox/` | Sandbox adapter |
| `src/services/policyLimits/` | Rate limiting |
| `src/utils/undercover.ts` | Leak prevention |
| `src/utils/attribution.ts` | Commit/PR attribution |
| `src/utils/config.ts` | Secure config storage |

### 10.3 Internal Tooling References

```typescript
// From prompts.ts:
- "go/cc" - Internal short link system
- "#claude-code-feedback" - Internal Slack channel (C07VBSHV7EV)
- "anthropics/claude-code" - Internal repo reference
```

---

## 11. API and Infrastructure

### 11.1 API Endpoints

```typescript
CLAUDE_AI_BASE_URL = 'https://claude.com'
CLAUDE_AI_STAGING_BASE_URL = 'https://claude-ai.staging.ant.dev'
CLAUDE_AI_LOCAL_BASE_URL = 'http://localhost:4000'
```

### 11.2 Attribution Header

```typescript
// x-anthropic-billing-header format
`cc_version=${version}; cc_entrypoint=${entrypoint}; cch=${attestation}; cc_workload=${workload}`
```

---

## 12. Key Security Findings

### 12.1 Information Disclosure Risk

The leak exposes:

1. **Internal codenames** (Capybara, Tengu, Numbat, Kairos)
2. **Feature roadmap** through feature flags
3. **Security mechanisms** (UNDERCOVER MODE, sandbox system)
4. **Model-specific vulnerabilities** (e.g., Capybara v8 false-claim rates)
5. **Internal infrastructure** (API endpoints, Slack channels)

### 12.2 Build System Vulnerabilities

- Source maps were included in production npm package
- Dead code elimination relies on string matching that could be bypassed
- Feature flags can be enabled by environment variables

### 12.3 Defense Mechanisms Observed

- UNDERCOVER MODE for public repo contributions
- Codename obfuscation in buddy system (character encoding)
- Client attestation for API requests
- Sandbox system for command execution
- Permission system with multiple layers

---

## 13. Conclusion

The Claude Code source map leak provides unprecedented insight into Anthropic's internal tooling and development practices. The codebase demonstrates:

1. **Sophisticated architecture** with modular tool system
2. **Strong security awareness** (UNDERCOVER MODE, sandboxing)
3. **Active feature development** (50+ beta flags)
4. **Internal codename culture** (animal-based naming)
5. **Comprehensive testing** (permission, telemetry, safety systems)

The leak serves as a case study in:
- Source map security in npm packages
- Internal codename management
- Feature flag driven development
- CLI application architecture at scale

---

## 14. References

- Source: `src_extracted/src/` from Claude Code v2.1.88 npm package
- Analysis Date: April 4, 2026
- Document: `docs/08_SRC_EXTRACTED_ANALYSIS.md`

---

*This analysis is provided for educational and security research purposes only.*
