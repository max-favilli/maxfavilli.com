---
title: "Agentic Engineering: a practical guide"
slug: introduction
order: 1
description: "Field notes from a senior engineer on working with AI coding agents. What works, what does not, why."
---

Field notes from a senior software engineer on working with AI coding agents. What works, what does not, why.

Based on several months of daily work with Claude Code and Codex CLI. Written for experienced developers who are about to start using coding agents and want to skip the expensive lessons. The techniques are tool-agnostic — they work with any agent that can read files and write code.

## Setup

Install your tool of choice. These docs do not cover that — the official docs do it better and stay current:

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [OpenAI Codex CLI](https://github.com/openai/codex)

Then start reading below.

## Reading order

Each document builds on the previous one.

1. **[A mental model for working with a coding agent](/guide/mental-model/)** — The (a)(b)(c)(d) framework: what the human brings vs. what the agent brings. Everything else assumes this model.
2. **[Context engineering](/guide/prompting-and-context/)** — How to shape the agent's picture of the world. Five core techniques. The bedrock claim: context quality is the ceiling on code quality.
3. **[Spec-driven coding](/guide/spec-driven-coding/)** — Hand off implementation cleanly: a spec plus test cases. When it works, when it does not.
4. **[Session discipline](/guide/session-discipline/)** — Design sessions vs. coding sessions. Persisting context. Fighting compaction. Cross-tool portability.
5. **[Tooling](/guide/tooling/)** — CLI vs. IDE extensions. Plugins vs. project docs. claude-mem, MCP integrations, and what they actually replace (and do not).
6. **[Token economy](/guide/token-economy/)** — Where tokens go, what is worth spending them on, and why ELI5 comments pay for themselves.
7. **[Team playbook](/guide/team-playbook/)** — Shared agent instructions, code review practices, CI/CD, git hygiene, and a day-one guide for new team members.

## What changes and what does not

The tools ship updates weekly. Features appear, change, disappear. Do not memorize tool-specific workflows.

The techniques in these documents are stable. They are grounded in how the models work and how software engineering works. Neither changes on a weekly release cycle. Learn the principles, adapt them to whatever tool you are using today.
