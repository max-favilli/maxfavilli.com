---
title: "A mental model for working with a coding agent"
slug: mental-model
order: 2
description: "The (a)(b)(c)(d) framework: what the human brings vs. what the agent brings. Everything else assumes this model."
---

You need a shared picture of what a coding agent is good at, what it is not, and where the human fits. Everything else in these docs assumes the model below.

A terminology note. The popular term is *vibe coding*, coined by Andrej Karpathy in early 2025. In its original sense it meant something much looser — "fully give in to the vibes, forget the code even exists." Simon Willison drew the distinction early and well. The better term for what these docs describe is **agentic engineering**.

## How a coding agent sees the world

A coding agent has no brain between turns. It has a **context window** — a fixed-size buffer of text (measured in tokens) that holds everything the agent can see at any given moment: the system prompt, project instructions (CLAUDE.md), every message you have sent, every response it gave, every tool call and result. This is the agent's entire reality. There is no hidden state, no background understanding, no memory beyond what fits in this window.

When you send a message, the agent re-reads the entire context window from the top. The new message goes at the bottom. The agent produces a response. That response gets appended. The window grows. Every turn is more expensive than the last because there is more to re-read — the cost curve is effectively quadratic.

When the window fills up, something has to give. The agent's runtime **compacts** the history: older messages get silently summarized, compressed into shorter representations, detail discarded. You cannot prevent this. You can only delay it (shorter sessions, smaller context) and mitigate it (persist decisions to files before they get compacted). Compaction is lossy — specific decisions become vague summaries, nuance disappears, things get dropped entirely.

**There is no separate memory system.** "The agent remembers" means "the agent reads a file at session start." Cross-session memory in tools like Claude Code works through three layers — all of them files loaded into the context window:

- **CLAUDE.md** — project-level instructions, loaded every session. Your team playbook, conventions, constraints. In Claude Code: `./CLAUDE.md` or `.claude/CLAUDE.md` at the project root.
- **Memory files** — stored on disk, loaded into context at session start. The agent "remembers" who you are and how you work because it reads files that say so. In Claude Code: `~/.claude/projects/<project>/memory/`.
- **User-level settings** — personal preferences that apply across all projects. In Claude Code: `~/.claude/CLAUDE.md`.

*(These paths are for Claude Code as of mid-2026. Other tools use equivalent mechanisms under different paths. Check the official docs for your tool.)*

Every one of these costs tokens. Every one competes for space in the same finite window. The more you load, the less room there is for the actual work.

This is why everything in these docs keeps coming back to the same point: **conversation is volatile, files are permanent.** The context window is the only thing the agent has. Compaction will shrink it. Sessions will end. The agent will forget everything that was not written to a file. Understanding this mechanic is the foundation for everything that follows.

## What coding is made of

What I do as a software engineer splits into four things:

- **(a) Domain and side-effect knowledge.** What the business needs. What the user does. How this system has broken before. What happens three weeks from now if we choose option X over option Y. The accumulated scar tissue of having shipped software.
- **(b) Tech stack knowledge.** The APIs, the language features, the framework quirks, the build tools, the standard library corners. The stuff you would look up in documentation if you had infinite patience.
- **(c) Approach knowledge.** Patterns, architectures, idiomatic solutions, the occasional clever trick. Knowing that this class of problem is usually solved with a queue, or a state machine, or a well-placed index.
- **(d) The actual typing.** Writing the code, running it, reading the error, fixing it, running it again, until it works and the tests pass.

Every non-trivial task is a mix of these four. The question is: who does which part?

## Who does what

Here is the division that has worked for me.

**(a) is the human's job, and only the human's job.** A coding agent has never met your users, never been paged at 3am, never sat in the meeting where the head of sales explained why this feature matters. It can *simulate* domain awareness if you describe it, but cannot generate it. If (a) is missing from the conversation, it is missing from the final code.

**(b) is where the agent beats any human, and it is not close.** Claude has digested essentially all public documentation, example code, and discussions about every mainstream tech stack. No human keeps that much detail loaded at once. If you are fighting a library you use twice a year, the agent will out-remember you on the first try. Accept this. Stop trying to compete on (b). The caveat: it is confidently wrong often enough that you still verify — it will happily invent an API that looks like one that should exist. But it starts ahead of you, and that matters.

**(c) is where the agent is strong but cannot operate alone.** The agent knows a hundred patterns and a thousand approaches. What it lacks is the vision to pick the right one for your situation — because the right one depends on (a). Left to itself, an agent asked to "just make it work" will produce something that works in isolation but sits awkwardly inside your system. The agent has the ingredients for (c); the human supplies the recipe.

**(d) is where the agent is almost fully autonomous, given the right inputs.** Hand it a clear description and a set of tests to pass, and it will do ninety-something percent of the coding itself, including the debugging loop. This is the part of the job where I now do the least typing — and where I used to do the most. This works best on greenfield, well-scoped code; in tangled legacy systems, describing (d) precisely is itself hard work, and the agent's autonomy shrinks accordingly. And then there is the doom loop — but I will get to that.

## The senior engineer's real job

Put those together and the senior engineer's role shifts. The typing goes away. As Martin Fowler's team at Thoughtworks puts it, *"the most important work happens before any code is written."* What replaces the typing:

1. **Hold the vision.** Decide what should exist and why. That is (a) talking to (c).
2. **Steer the agent through (b) and (c) with iterative prompting.** You are not writing code; you are shaping the agent's search through the space of solutions it already knows. This is inherently iterative — one prompt is rarely enough. Each round moves the solution closer to something that respects (a).
3. **Know when to stop the agent.** The failure mode is what the community now calls the **doom loop**: the agent fixes one error, introduces another, fixes that, reintroduces the first, and burns tokens on an orbit it cannot escape. After the fifth failed attempt, it starts inventing library functions and API signatures that do not exist, just to satisfy the shape of your request. When you recognize this pattern, *do not prompt your way out of it.* Stop. The fix is almost never "one more prompt" — it is upstream: something is missing from (a), or the spec for (d) is too vague. One technique that works before you reach the full reset: **ask the agent to add temporary logging** — console output, log file entries, debug traces — then run the code, read the logs together, and let the actual runtime behavior tell you both what is happening. The agent is often guessing at state; logs replace guessing with evidence. Fix the bug, then remove the temporary logging. This breaks the doom loop more often than you would expect, because it gives the agent new information instead of recycling the same failed context. Recognizing when to try this — and when even this is not enough and you need a full reset — is one of the most valuable skills in the new workflow.
4. **Reset with a fresh context — or a fresh agent.** Do not simply rewind a few turns and push on. Open the next attempt in a *fresh* session, or better, hand the problem to a different agent entirely — Claude looking at what Codex got stuck on, or the other way around. The longer an agent digs into a failed path, the more its context is polluted by accumulated wrong turns. This is the agent version of the *fresh eyes* effect you have experienced yourself: you stare at a bug for an hour, a colleague glances at it for thirty seconds and spots what you missed. A clean context works on agents for the same reason it works on people — they, too, get lost in their own recent thoughts.
5. **Specify (d) precisely enough that the agent can run.** A clear description plus test cases. If the agent is thrashing on (d), the fix is almost always upstream: your description was vague, or the tests did not pin down the behavior you actually wanted.
6. **Review every diff.** The agent speeds up typing, not judgment. Simon Willison states the rule well: *"Never commit any code to a repository if you couldn't explain exactly what it does to somebody else."* If you cannot review what the agent wrote, you cannot ship it. Full stop.

## What this means for the rest of these docs

The following files make this division of labor work in practice. Kent Beck frames the goal well: *"more consequential decisions per hour."* Two topics are load-bearing enough to name here:

- **Context engineering** is the discipline of transferring (a) into the agent's working memory — the domain, the constraints, the side-effects the agent cannot see from the code alone. The more of (a) the agent sees, the less steering you need and the further (c) gets before it drifts. This is not "write a longer prompt." It is a practice, and it gets its own document.
- **Persistent docs as memory.** You now know the context window is volatile — compaction will shrink it, sessions will end, tools will change. If (a) exists only in the current conversation, you will lose it. The remedy: persist (a) into project documents that any agent can re-read at the start of any session. This gets its own document.

Beyond those two: spec-driven coding is how you hand off (d) cleanly; tooling is the plumbing; and the [team playbook](/guide/team-playbook/) is the organizational-level counterpart — designing the guardrails that make every session better by default.

If you only remember one sentence from this page: **you are not writing code; you are shaping the agent's search through the space of solutions it already knows.** Your value was never in the typing. It was in knowing which search to shape, and why. That part is now more important, not less.
