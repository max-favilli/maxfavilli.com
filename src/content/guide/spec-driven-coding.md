---
title: "Spec-driven coding"
slug: spec-driven-coding
order: 4
description: "Hand off implementation cleanly: a spec plus test cases. When it works, when it does not."
---

In [the mental model](/guide/mental-model/) I described (d) — the actual typing — as the part where the agent is almost fully autonomous, given the right inputs. This document is about what "the right inputs" looks like in practice.

The core idea is simple: **write down what needs to exist and how to verify it, then let the agent build it.** A spec and a set of test cases. The agent handles implementation, debugging, and iteration. You handle judgment — is this spec the right thing to build, and do these tests actually prove it works?

This is [context engineering](/guide/prompting-and-context/) taken to its logical endpoint: instead of feeding context incrementally through a conversation, you package it into documents the agent can consume whole.

## What a good spec contains

A spec is not a requirements document written for a project manager. It is written for the agent — concise, concrete, decidable. Everything the agent needs to start coding, nothing it does not.

- **What the thing does.** One paragraph. If you cannot describe it in one paragraph, you have not decomposed enough (see technique 3 in [Context engineering](/guide/prompting-and-context/)).
- **Inputs and outputs.** What goes in, what comes out, what types, what formats. Be explicit — the agent will not guess the same defaults you would.
- **Edge cases and error handling.** What happens when input is empty, malformed, missing, enormous? If you do not specify, the agent will make a choice. It may not be your choice.
- **Constraints.** "Must not add new dependencies." "Must work with Node 18." "Must not break the existing API contract." These are the non-goals from [Context engineering](/guide/prompting-and-context/), made permanent.
- **What "done" looks like.** Ideally: a list of test cases to pass. Failing that: a sharp description of the observable behavior when the feature is working correctly.

## Test cases are the spec's teeth

A spec without test cases is a wish. A spec with test cases is a contract.

When you give the agent both a description and a set of tests, something powerful happens: the agent has an objective, mechanical way to know whether it has succeeded. It can run the tests, read the failures, fix the code, run again — the full (d) loop — without asking you anything. This is where the agent's autonomy is highest and your involvement is lowest.

Writing test cases used to be the tedious part that got skipped under time pressure. With an agent, it is cheap. Give the agent the spec and ask it to *generate* the test cases first, before writing any implementation. Review the tests — this is where your (a) matters most: are these the right tests? Do they cover the edge cases that matter to the business, not just the edge cases that are obvious from the code? Once the tests are right, let the agent implement against them.

This is Simon Willison's **red-green pattern** applied to agent coding: start with failing tests (red), let the agent make them pass (green). The tests are the guardrail that keeps (d) on track without constant human steering.

## The spec as a persistence mechanism

A written spec has a benefit beyond guiding the current session: it survives.

When the conversation compacts, the spec file is still on disk. When you switch from Claude to Codex, the spec file is still on disk. When a colleague picks up the work next week, the spec file is still on disk. Unlike a conversation, a spec does not decay, get compacted, or vanish when you close the terminal.

This makes spec-driven coding a natural complement to the [session discipline](/guide/session-discipline/). The spec is one of the project documents you persist to fight compaction — but it is also the most *actionable* one, because any agent can pick it up and start coding against it immediately.

## When spec-driven works best

- **Greenfield, well-scoped features.** A new API endpoint, a new utility function, a data transformation pipeline. Clear inputs, clear outputs, clear tests.
- **Bug fixes with a reproducible case.** The failing test *is* the spec. "This test should pass and currently does not. Fix it."
- **Refactors with behavior preservation.** "The existing tests must continue to pass. Change the implementation to use X instead of Y."

## When it works less well

- **Exploratory work where you do not yet know what you want.** If you cannot write the spec, you are not ready for (d) yet — you are still in (a) and (c) territory. That is fine. Use a design session (see [Session discipline](/guide/session-discipline/)) to figure out what the spec should say, then come back.
- **Large cross-cutting changes.** A spec that touches fifteen files and three subsystems is too big. Decompose it into smaller specs, each with its own tests.
- **Legacy code with no existing tests.** The agent's autonomy on (d) depends on a feedback loop — run, fail, fix, run. Without tests, there is no loop, just guessing. Write the tests first (the agent can help), then use them as the spec for the change.

## A practical workflow

1. **Write the spec.** One markdown file. What it does, inputs/outputs, constraints, edge cases.
2. **Generate test cases from the spec.** Ask the agent to write them. Review — are these the *right* tests?
3. **Let the agent implement.** Point it at the spec and the tests. Let it run the red-green loop.
4. **Review the diff.** The spec tells you what to check: does the implementation match the description? Do the tests pass? Did the agent stay within the constraints?
5. **Commit the spec alongside the code.** The spec is documentation. Future you, future agents, and future colleagues will thank you.

## What this connects to

- **Context engineering** — a spec is a high-density context package. Everything the agent needs, nothing it does not.
- **Session discipline** — specs persist across sessions. They are one of the key documents that fight compaction.
- **Team playbook** — predefined test cases in CI/CD ([Team playbook](/guide/team-playbook/)) are the organizational-level version of spec-driven coding.

If you only remember one sentence from this page: **a spec with test cases turns the agent from a collaborator you have to steer into an executor you can trust to run.**
