---
title: "Team playbook"
slug: team-playbook
order: 9
description: "Shared agent instructions, code review practices, CI/CD, and a day-one guide for new team members."
---

The previous documents in this series are about one engineer working with one agent. This document is about the layer above: what should be in place *before* anyone on your team opens their first session.

Martin Fowler's team at Thoughtworks draws a useful distinction between being **"in the loop"** — fixing the agent's output by hand — and being **"on the loop"** — designing the system that makes the agent produce better output by default. In-the-loop is the individual technique covered in [the mental model](/guide/mental-model/) and [Context engineering](/guide/prompting-and-context/). On-the-loop is what this document is about: shared instructions, review practices, and CI guardrails that make every session better, even for the newest team member on their first day with a Claude license.

## Shared agent instructions

Every coding agent supports some form of project-level instructions that are loaded at the start of every session — Claude Code calls it `CLAUDE.md`, Codex has `AGENTS.md`, others have their own equivalent. This file is the single most important piece of team-level infrastructure. It is where your team's principles live, and the agent reads it before it reads your first prompt.

Here is what ours contains. Adapt it, do not copy it blindly — your team's context is different.

### Before coding

- **Explore before edit.** Read and map the area before changing anything. Report what you found. Do not edit until the human has reviewed your understanding.
- **Ask for a plan and get it approved before writing code.** Propose what you will do in plain English. Wait for approval.
- **Decompose, then one task at a time.** Always try to break a task into sub-tasks — err on the side of decomposing too much rather than too little. Write them into a `roadmap.md` or to-do list within the project. Work through them one at a time.
- **State non-goals.** Before starting, confirm what is explicitly out of scope.

### During coding

- **Challenge the prompt.** Do not obey passively. If the request is ambiguous, ask as many questions as needed to clarify context. If the request seems wrong, say so.
- **Compare with general consensus.** For every significant decision — architecture, pattern choice, library selection — compare with community best practice and suggest alternatives when relevant.
- **Write clear code comments.** Comment at the ELI5 level: explain *why*, not just *what*. Future humans and future agents will both benefit from code that explains itself plainly.
- **Know when to stop.** If you have failed to solve the same problem after five attempts, say so explicitly. Do not keep trying. The human should start a fresh session or hand the problem to a different agent — a clean context often solves what a polluted one cannot (see [the mental model](/guide/mental-model/)).

### Before committing

- **Review the diff with the human before every commit.** Never commit code the human has not reviewed and approved.
- **Write ELI5 commit messages.** Every commit message should explain what changed and why in plain language that a new team member — or a different agent picking up the work tomorrow — can understand without reading the diff.
- **Run tests and linting before committing.** Self-check before asking for human review. Agents pull patterns from diverse codebases and will mix styles, leave unused imports, and introduce inconsistencies a human developer would avoid by habit. Linting normalizes this mechanically — run `npm run lint`, `ruff check`, or whatever the project uses, and fix any errors before committing.
- **Never include secrets, credentials, or production tokens** in code, commit messages, comments, or project documents. Agents can and will surface what they see in suggestions and logs.

### Git hygiene

These are good practice regardless of agent coding, but agents make them critical:

- **Always work on a branch.** Never commit directly to main.
- **Commit early and often.** Small checkpoints you can roll back to. When the agent goes down a wrong path, you need a known-good state to return to.
- **Never let the agent run destructive git commands.** `reset --hard`, `force push`, `checkout .`, `clean -f` — these discard work. If the agent suggests one, review why before approving.
- **Commit before asking the agent to make large changes.** The agent can and will overwrite uncommitted work. A commit takes seconds and saves hours.

### Always

- **Persist context in project documents.** Vision, roadmap, design notes, decision logs — anything the next session (or the next agent) will need to know. Do not rely on conversation memory. See [Session discipline](/guide/session-discipline/) for what to persist and when.
- **Separate design sessions from coding sessions.** Design sessions produce documents (vision, specs, decision logs). Coding sessions consume documents and produce code. Do not mix them — a design session that produces no documents wastes its insight.
- **Let the agent draft your docs.** Vision docs, roadmaps, decision logs, code comments, READMEs — the agent writes solid first drafts of all of these. You review and correct. Five minutes of editing beats thirty minutes of writing. The barrier to maintaining project docs drops when the agent does the first draft.
- **Be aware of token costs.** Big context consumes tokens, doom loops burn through them, irrelevant files waste them. ELI5 comments and project docs cost tokens but save more than they spend by reducing iteration. See [Token economy](/guide/token-economy/).

## Code review in the age of agents

PR-based code review with another human before merge is the most important gate your team has. That does not change with agents. If anything, it matters more.

But there is a problem worth being aware of, and I do not have a clean solution for it yet.

**The volume problem.** When an agent writes code significantly faster, the volume of diffs landing on reviewers increases. Humans get fatigued. A reviewer who carefully read every line of three PRs a day will start skimming when there are nine. The quality of the most important gate degrades precisely when it matters most.

**The tautological test problem.** An agent can write code and tests together, all green, PR looks clean — but the tests may be testing that the code does what the code does, not that it does what the business needs. A careful reviewer will catch this. A fatigued reviewer will not.

**The speed-pressure problem.** Teams using agents feel productive and want to ship faster. The temptation to rubber-stamp PRs grows. "The agent wrote it, the tests pass, it's probably fine" is a sentence that will be said, and it will eventually be wrong.

One practice that helps more than you might expect: **ELI5 code comments** (see the shared instructions above). When the agent writes clear comments explaining *why* the code does what it does, the reviewer's job gets dramatically easier. Instead of reverse-engineering intent from the diff, the reviewer reads the explanation and judges whether the intent is correct. This turns code review from "figure out what this does" into "decide whether this is right" — a much faster and more reliable task.

I do not think these problems require a complex solution. Here is what I think is a reasonable starting point:

- **Keep PR + human review as the hard gate.** No merge without a human approval. No exceptions.
- **Add basic automated CI gates:** linting, test-must-pass, security scanning. These catch what humans miss under fatigue — style drift, known vulnerability patterns, broken builds — and absorb some of the volume increase so the reviewer can spend attention on what only a human can judge.
- **Instruct the agent to self-check before opening a PR.** If the agent runs tests, linting, and a basic review of its own diff before the human ever sees it, the PR that arrives is already cleaner. The human reviewer's job gets easier.
- **Review the tests as carefully as the code.** This is the discipline that catches tautological tests. Ask yourself: if I changed the business requirement, would this test fail? If the answer is no, the test is not testing what matters.

This is not a solved problem. As the team gains experience, we will learn where these guardrails are insufficient and adjust. The point for now is: be aware that the volume, quality, and speed dynamics change when agents enter the workflow, and do not assume the old review cadence will absorb the new output rate without strain.

## CI/CD and test cases

One of the largest and most immediate benefits of coding agents is how much easier they make writing tests.

Creating test cases, generating sample data, building fixtures, writing assertions — this was always the part of testing that felt tedious and got skipped under time pressure. A coding agent can do most of this work if you give it a clear description of the behavior to test and the edge cases to cover. The *judgment* of which tests matter is still yours (see (a) in [the mental model](/guide/mental-model/)), but the *typing* of those tests is now cheap.

Use this. **Predefined test cases should be mandatory in CI/CD to progress to higher environments.** "We don't have time to write tests" is no longer credible when an agent can generate a solid test suite from a spec in minutes. The tests serve three purposes: they gate promotions in the pipeline, they give the agent clear success criteria for future work (see [Spec-driven coding](/guide/spec-driven-coding/)), and they catch regressions when the agent — or a human — changes something downstream.

## Getting started on day one

If you are a new team member reading this:

1. Follow the reading order in the [introduction](/guide/). Start with [the mental model](/guide/mental-model/) — it is one page and everything else builds on it.
2. Make sure the shared `CLAUDE.md` (or equivalent) is in every project you work on.
3. Read [Tooling](/guide/tooling/) before installing plugins. Start with the CLI and add tools only when you hit a friction point they solve.
4. Start with a small, well-scoped task. Practice the explore → plan → approve → code → review cycle.
5. Resist the temptation to let the agent "just handle it." The agent is fast but not wise. You are the wisdom. These docs exist because we learned that the hard way.
