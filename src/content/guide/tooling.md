---
title: "Tooling"
slug: tooling
order: 6
description: "CLI vs. IDE extensions. Plugins vs. project docs. MCP integrations, Superpowers, and what they actually replace."
---

This is not a tool tutorial. The official docs for Claude Code, Codex CLI, and Cursor are better at that and stay current. This document covers the choices and trade-offs that the official docs do not.

## CLI vs. IDE extensions

I use Claude Code CLI and Codex CLI. I tried the VS Code extensions for Claude and Gemini Pro and stopped — they were unreliable, stopped working mid-session, and behaved unpredictably.

That may change. Extensions improve fast. But the CLI has a structural advantage: it is a terminal session. You see exactly what the agent sees, what it runs, and what it changes. There is no layer of IDE abstraction between you and the agent. When something goes wrong, you know where to look.

If your team already uses an IDE extension and it works, keep using it. The techniques in these docs are tool-agnostic. But if you are starting from scratch, start with the CLI.

## Plugins and MCP: what they do and do not replace

People will tell you that plugins can replace the doc-writing practice described in [Session discipline](/guide/session-discipline/). This is worth examining carefully.

### MCP integrations (Jira, Linear, Confluence)

MCP (Model Context Protocol) lets the agent connect to external tools. A Jira MCP reads your tickets. A Confluence MCP reads your wiki. A Linear MCP manages your issues.

These are useful — especially if your team already tracks work in these tools. Having the agent read a Jira ticket directly instead of you copy-pasting the description into the prompt saves time.

But they are **pipes, not sources**. The Jira MCP reads tickets somebody wrote. The Confluence MCP reads docs somebody wrote. No plugin generates (a) — your domain knowledge, your business constraints, your reasoning for why you chose X over Y. That comes from your head and still needs to land somewhere the agent can read.

Plugins give the agent access to information that already exists. Your project docs create the information that does not exist anywhere else.

Use plugins as a supplement. Do not mistake task management (Jira tickets) for context engineering (vision, decisions, constraints).

### claude-mem

[claude-mem](https://github.com/thedotmack/claude-mem) is a popular Claude Code plugin (89K+ GitHub stars) that automatically captures everything Claude does during sessions — file reads, tool calls, changes — compresses them with AI, and injects relevant observations back into future sessions.

It solves a real problem: the cold-start when you open a new session and the agent knows nothing about what happened yesterday.

**What it does well:**
- Captures session activity automatically — you do not have to remember to write things down.
- Makes past observations searchable across sessions.
- Reduces the "where were we?" friction.

**What it does not do:**
- It captures *what happened*, not *why*. It records that you chose Postgres but not that you chose it because compliance requires cross-table transactions. The reasoning — the (a) — is not in the activity log.
- It is Claude-Code-specific. Switch to Codex or another tool and claude-mem's observations stay behind. Your markdown docs come with you.
- The compression is lossy. An AI summarizes what happened, and summaries lose detail. A decision log entry you wrote yourself is exact.

**Think of it this way:** claude-mem is a dashcam — it records the drive automatically, useful for reviewing what happened. Your project docs are the navigation plan — they say where you are going and why. No dashcam generates a navigation plan.

**Recommendation:** try it. It is a good safety net that catches things you forgot to document. But it supplements the doc-writing practice, it does not replace it. And if cross-tool portability matters to you (it matters to me), the markdown files are still the foundation.

### Codebase indexing (claude-context, Context7)

These plugins index your codebase so the agent can search it semantically rather than reading files one by one. They speed up the "explore before edit" phase.

Useful for large codebases. But they help with (b) — navigating the tech stack — not with (a). The codebase does not contain why you made the decisions you made.

## Workflow frameworks: Superpowers

[Superpowers](https://github.com/obra/superpowers) (by Jesse Vincent / Prime Radiant) is a composable skill framework for coding agents. It installs into Claude Code, Codex CLI, Cursor, and others as a set of enforced skills — not suggestions the agent might follow, but workflows it must check before acting.

It is worth knowing about because **it arrived at the same practices described in these docs, independently, from a different starting point.** Superpowers treats the agent as "an enthusiastic junior engineer with no judgment and no project context" and prescribes a seven-phase process: brainstorming, git worktrees, writing plans, subagent-driven development, mandatory TDD, code review, and branch finalization. If that list sounds familiar, it should.

### How Superpowers maps to these docs

- **Brainstorming + Writing Plans** = your design sessions producing documents ([Session discipline](/guide/session-discipline/)). Superpowers decomposes plans into 2-5 minute tasks with exact file paths and verification steps — the same decompose-then-execute pattern from [Context engineering](/guide/prompting-and-context/) and [Spec-driven coding](/guide/spec-driven-coding/).
- **Mandatory TDD** = spec-driven coding with test cases as the spec's teeth ([Spec-driven coding](/guide/spec-driven-coding/)). Red-green-refactor, enforced as a skill, not a suggestion.
- **Subagent-driven development** = fresh-agent reset ([the mental model](/guide/mental-model/) point 4), but as the *default* execution model rather than an escape from doom loops. Every task gets a fresh agent with a clean context. Two-stage review (spec compliance, then code quality) before accepting the work back.
- **Code review and verification** = the review gates in the [team playbook](/guide/team-playbook/). Superpowers adds a structured severity system — critical issues block progress, minor issues get logged.
- **Git worktrees** = the git hygiene principles from the [team playbook](/guide/team-playbook/), formalized as isolated development branches with verified clean test baselines.

### What Superpowers adds

The key contribution is **enforcement**. Your CLAUDE.md is prose the agent *should* follow. Superpowers encodes each technique as a skill the agent *must* activate. The difference is the same as between a coding standard document and a linter rule: one relies on discipline, the other is mechanical.

Superpowers also normalizes subagent orchestration — dispatching parallel fresh agents per task — which goes further than the fresh-agent reset described in [the mental model](/guide/mental-model/). Instead of reaching for a clean context only when stuck, you start every task with one.

### What Superpowers does not cover

Superpowers is process without theory. It prescribes *what* to do but not *why* it works. The (a)(b)(c)(d) framework ([the mental model](/guide/mental-model/)), context engineering as a discipline ([Context engineering](/guide/prompting-and-context/)), the [token economy](/guide/token-economy/), and the "shabby request with rich context" insight have no equivalent in Superpowers. It assumes you already understand *why* the agent needs structure — it just gives you the structure.

**This is why these docs and Superpowers are complementary, not competing.** Read the mental model to understand why these techniques work. Install Superpowers to enforce them mechanically. The theory tells you when to deviate from the process; the process keeps you honest when you are tempted to skip steps.

### The convergence signal

Superpowers is one more data point in a pattern. Fowler's team at Thoughtworks arrived at "in the loop / on the loop." Willison arrived at red-green TDD for agents. Beck arrived at "more consequential decisions per hour." Vincent arrived at composable enforced skills. **When independent practitioners converge on the same practices from different starting points, the practices are probably load-bearing.** The specifics of each framework differ; the underlying shape is the same.

## Choosing tools

The honest summary:

| What you need | What helps |
|---|---|
| Domain context, decisions, constraints | Your project docs (markdown files) |
| Task tracking integration | Jira/Linear MCP |
| Session memory within Claude Code | claude-mem |
| Fast codebase navigation | Codebase indexing MCP |
| Style and convention enforcement | Linting + CLAUDE.md |
| Workflow enforcement (design → plan → TDD → review) | Superpowers skills framework |

Start with the docs. Add plugins when you hit a specific friction point they solve. Do not install everything on day one — each plugin is another thing to configure, maintain, and debug when it breaks.
