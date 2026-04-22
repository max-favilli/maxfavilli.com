---
title: "Session discipline"
slug: session-discipline
order: 5
description: "Design sessions vs. coding sessions. Persisting context. Fighting compaction. Cross-tool portability."
---

A coding agent has no memory between sessions. When the conversation ends, everything in it is gone. Within a long session, it is not much better — context windows get compacted to make room, and whatever the agent "knew" an hour ago may have been silently dropped. Switch tools — Claude to Codex or back — and you start from zero.

This is the single most common source of wasted time in agent coding. Not bad prompts, not wrong code — *lost context*. Twenty minutes building a shared understanding, then the session breaks or compacts, and the next one starts from zero.

This document is about how to stop losing that work.

## The two kinds of session

Not every session has the same goal. I separate my work into two kinds:

**Design sessions** produce *documents*. You and the agent explore the problem space, discuss approaches, compare with best practice, sketch architectures, and write down decisions. The output is not code — it is a vision doc, a roadmap, a spec, a decision log, a list of constraints. The goal is to get (a) and (c) out of your head and into files that any agent can read.

**Coding sessions** consume *documents and produce code*. You point the agent at the spec, the roadmap, the design notes. The agent reads them, builds context from them, and starts implementing. The goal is to execute (d) against a well-defined plan.

The separation matters because the failure modes are different. A design session that produces no documents has wasted its insight — the insight vanishes on compaction. A coding session that starts without documents has no foundation — the agent makes assumptions you cannot see or correct.

## What to persist and where

**If it matters, write it to a file.** Conversation memory is volatile. Files on disk are permanent.

Documents worth maintaining:

- **Vision / goals.** One page. What are we building and why. What does success look like. This is the highest-level (a) — the thing that should not change between sessions.
- **Roadmap / task list.** What remains to be done, in what order, with what dependencies. Updated at the end of every session. This is the document the next session reads first.
- **Specs.** One per feature or task, as described in [Spec-driven coding](/guide/spec-driven-coding/). The most actionable form of persistent context — any agent can pick one up and start coding against it.
- **Decision log.** Why we chose X over Y. The agent will re-propose Y in a future session if the reasoning is not written down. One line per decision is enough: "Chose Postgres over DynamoDB because we need transactions across tables."
- **CLAUDE.md / AGENTS.md.** Project-level instructions the agent reads automatically at session start. Style conventions, tech stack, non-goals, team principles (see [Team playbook](/guide/team-playbook/)). This is context that does not belong in any single spec but applies to every session.

This looks like a lot of writing. It is not — because **the agent can draft most of it for you.** Ask it to write the vision doc from your description. Ask it to generate a roadmap from the spec. Ask it to summarize a session's decisions into the decision log. You review and correct — five minutes of editing versus thirty of writing from scratch. The same applies to code comments, READMEs, and API docs. Developers hate writing documentation; agents do not. Use this.

You do not need all of these on day one. Start with the roadmap and one spec. Add the others as the project grows.

## The session lifecycle

A practical rhythm that has worked for me:

**Starting a session:**
1. Point the agent at the project docs. "Read `roadmap.md`, `vision.md`, and the CLAUDE.md. Tell me what you understand about where we are."
2. Correct any misunderstandings. This takes two minutes and saves twenty.
3. Pick the next task from the roadmap.

**During a session:**
4. Work normally — explore, plan, code, review, commit.
5. When a decision is made that future sessions will need to know, write it down *now*, not later. Add it to the decision log or update the relevant spec. If you wait until the end of the session, you will forget.

**Ending a session:**
6. Update the roadmap. Mark what was done, note what is next, flag anything blocked.
7. If the session produced insights that are not captured in any document — a constraint you discovered, a gotcha you hit, an approach that did not work — write them down. One sentence each is enough.
8. Commit the updated docs alongside the code.

The discipline is doing this every time. Five minutes at the start, five at the end. Every future session starts warm instead of cold.

## Fighting compaction

Even within a session, context gets compacted. The window fills up, older messages get summarized or dropped, detail disappears.

You cannot prevent this. You can make it hurt less:

- **Persist early.** The moment a design decision or key insight crystallizes, write it to a file. Do not wait. If the conversation compacts before you persist, the insight is gone.
- **Refer to files, not memory.** "See the constraints in `spec-auth.md`" is compaction-proof. "Remember what we discussed about the auth constraints" is not — the agent may no longer remember.
- **Keep the working context small.** One task at a time. Finish it, commit, update docs, then move on. A session that tries to hold five tasks in its head simultaneously is a session that will lose three of them to compaction.
- **When you notice drift, re-anchor.** Ask the agent to re-read the relevant doc. This is cheap and immediate — the doc is on disk, the agent can reload it in seconds.

## Cross-tool portability

Follow the practices above and something valuable happens for free: **your project state becomes tool-agnostic.**

Roadmap, specs, decision log — all markdown. None depend on Claude Code's memory or Codex's conversation history. Any agent that can read files picks up where the last one left off.

This is why the "fresh agent reset" from [the mental model](/guide/mental-model/) works. Hand a stuck problem to a different agent, it reads the project docs, builds context in minutes, starts with a clean perspective. Without persistent docs, switching means re-explaining everything — so in practice you never switch, even when you should.

Write your project docs as if the next agent has never seen your codebase, your conversation, or your tool. It probably has not.

People will tell you that plugins (Jira MCP, Confluence MCP, claude-mem) can replace this doc-writing practice. They cannot — plugins are pipes, not sources. The full analysis is in [Tooling](/guide/tooling/).

## What this connects to

- **[Context engineering](/guide/prompting-and-context/)** — session discipline is context engineering across time. The real-time practice keeps one session productive; the persistence practice keeps all sessions connected.
- **[Spec-driven coding](/guide/spec-driven-coding/)** — specs are the most actionable form of persistent context.
- **[Team playbook](/guide/team-playbook/)** — the shared CLAUDE.md is the team-level version of session discipline.

If you only remember one sentence from this page: **conversation is volatile, files are permanent — anything the next session needs to know belongs in a file, not in your memory or the agent's.**
