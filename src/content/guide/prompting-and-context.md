---
title: "Context engineering"
slug: prompting-and-context
order: 3
description: "How to shape the agent's picture of the world. Five core techniques. Context quality is the ceiling on code quality."
---

The single load-bearing move in working with a coding agent is transferring (a) — your domain, side-effect, and constraint knowledge — into something the agent can see. This document is about doing that in real time, inside a session. Keeping context alive *across* sessions is [Session discipline](/guide/session-discipline/).

Andrej Karpathy popularized the term **context engineering** in 2025 as a correction to "prompt engineering." The correction matters. A prompt is a communication channel — the main one, but still just a channel. What you send through it is up to you: a request, a path to a document, instructions to analyze code, a research task, a loop of questions until the agent's understanding matches yours. Finding creative ways to build the agent's picture of the world is itself a skill. The total context — files read, tool results, system instructions, project configuration, conversation history — is what determines the quality of the output.

## The bedrock claim

**The completeness of the context the agent is working from determines the quality of the code it writes — not how precisely you describe what you want.** This is the lever. If you remember nothing else from this page, remember that.

This is counterintuitive. Once you have given the agent the right context — the domain facts, the constraints, the failure modes, the shape of what "correct" means — even a rough description of what you want will produce good results. The agent fills in the blanks because it has the materials to fill them *correctly*. Conversely, the most precisely worded request, delivered against thin context, has a good chance of producing code that works in isolation but sits wrong inside your system. **Rich context with a shabby request beats a perfect request with thin context, almost every time.**

When a prompt fails, the diagnostic question is always: *what is missing from the agent's picture of the world, and what is the cheapest way to get it there?* Sometimes the answer is another message with a new fact. Sometimes it is pointing the agent at a file it has not read, handing it a spec, or starting a fresh session with a better opening.

## What belongs in context

Not everything. Context is a finite resource — the window has a size, and past a certain point agents get distracted by irrelevant material for the same reason humans do. The goal is *high signal*, not *high volume*.

What is worth transferring in:

- **Domain facts the code does not state.** Why the system was built this way. Which constraints come from real users and which are historical accidents. What "correct" actually means for this feature in this business.
- **Side effects and invariants.** What happens downstream when you touch this code. What this module must never do, even if it technically could.
- **"Done" criteria.** Ideally as tests the agent can run. Failing that, a sharp description of what success looks like.
- **Known failure modes.** Past bugs, near-misses, the shape of things that have gone wrong before. Agents are very good at avoiding a trap once you have named it.
- **Explicit non-goals.** What you do *not* want the agent to do. Often more load-bearing than what you do want — see technique 4 below.
- **The shape of the solution, if you have a preference.** If you already know the approach you want, say so. Do not make the agent guess and then correct it.

## What to leave out

- **The whole codebase.** The agent can discover what it needs on its own if you let it (see technique 1 below). Beyond a certain size, the agent will not actually digest it all — it will tell you it analyzed everything, but in practice it processed only part. Feed it reasonable, relevant portions, or point it at the specific parts that matter for the task.
- **Contradictory or stale guidance.** Old `CLAUDE.md` entries from a past refactor, half-remembered style rules, comments that no longer reflect the code. Stale context is worse than no context.
- **Things the agent can read in seconds.** You do not need to paste the file. Tell it to open the file.
- **Your frustration.** Tempting, never productive. The agent calibrates on information, not mood. If you feel yourself getting frustrated, the fix is almost always that the context is thin — not that the agent is obstinate.

## The core techniques

These are the moves that, in my experience, made the difference between getting useful output from an agent and spending all afternoon arguing with one.

1. **Explore before edit.** Before asking the agent to change anything, ask it to *read*. "Map this area of the codebase. Tell me which files are involved, what the current structure is, and where a change to X would land." Only after the agent reports back — and you have corrected any misreads — do you ask it to edit. This is the highest-leverage technique on this page. It forces the agent to build a real mental model instead of pattern-matching against vaguely similar code. The agent's report will almost always surface something *you* were wrong about — a forgotten file, an unknown dependency, a quietly adopted convention. It gives you a free checkpoint: misunderstandings surface before two hundred lines of diff need to be thrown away. And — easy to miss — **the exploration is not one-directional.** You are learning too. Challenge what the agent reports. Ask it to explain why something is structured that way, to compare what it found with best practice. Let it surprise you, and let your experience surprise it. The explore phase is a *dialogue*: both sides come out knowing more, and that shared understanding is what makes the subsequent edit land.

2. **Ask for a plan, then approve it before any code is written.** Have the agent propose, in plain English, what it is going to do. Read the plan. Push back on anything that does not match (a). Only after the plan is right do you let it edit. This is where you catch the subtle "the agent misunderstood the ask" — the kind where the code will look reasonable but solve the wrong problem. It is much cheaper to argue about a paragraph than about a diff. A coding agent can give you something like a 3x productivity boost on the right kind of task, but it makes mistakes — sometimes remarkably stupid ones, the kind only a junior would make. If you skip the plan review and miss one of these, you will spend thirty minutes prompting in circles to fix something that is not working, while checking the plan would have taken five. Review the plan.

3. **One task at a time.** Narrow the blast radius. If a task decomposes into sub-tasks, do them one at a time. If two tasks are genuinely distinct — different parts of the codebase, different classes, different flows — you can run them in parallel sessions with no issue. The danger is bundling related sub-tasks inside a single session: the agent mixes concerns, and when something breaks you cannot tell which sub-task caused it. A practical move: have the agent write the sub-tasks into a project document — a `roadmap.md` or a to-do list. Neither of you forgets where you are, and the document itself becomes context: the agent has the full path in mind at every step and can reason about consequences in order.

4. **State the non-goals.** "Do not add new dependencies." "Do not refactor unrelated code." "Do not touch the auth module — we are shipping it next week." Without explicit non-goals, the agent defaults to an ambitious interpretation: it will see opportunities to "improve" adjacent code and take them, because the only instruction it had was to do something useful. Non-goals cap that ambition to what you actually asked for. I write at least one into almost every non-trivial prompt now.

5. **Iterate, don't one-shot.** Your first message is the opening of a conversation, not a commission. Plan to refine three to five times. Each round: the agent responds, you spot what it misunderstood, you add the missing piece. If you are not refining, you are either lucky or not paying attention. The same dialogue from technique 1 applies: challenge choices, ask for reasoning, learn from the agent, correct what it assumed wrong. When a conversation gets long, ask the agent to summarize its current understanding of the task. You will almost always find drift. Correct it, then continue.

## Anti-patterns

A short list of the things I see waste the most time:

- **"Just make it work."** The emptiest prompt, and the one frustration and time pressure tempt you toward most. You are behind schedule, the last attempt failed — so you type "fix it" and let the agent churn for an hour. It will not fix it by trying harder, because the problem is not effort — it is missing context. Stop. Ask yourself: what context is the agent missing? What does it not know, not remember, or not see? Answer that, and your next prompt will be worth sending.
- **Dumping the entire codebase into the prompt.** More context is not better context. Beyond a certain size the agent will not actually digest it all — it will tell you it analyzed everything, but in practice it processed only part. Feed it reasonable, relevant portions, or point it at the specific parts that matter for the task.
- **Arguing with the agent about something that should have been in the context.** Three turns of "no, not that, I meant…" is a signal that a constraint belongs in the opening, not in the corrections.
- **Not reading what the agent wrote before replying.** The agent's response reveals what it understood and what it did not — even when it succeeded at the immediate task. If it misunderstood something, sooner or later that will have an impact. Skim the response and you are driving blind.
- **Confusing length with quality.** A longer prompt is not a better prompt. If you find yourself unable to say it concisely, try this: ask the agent to summarize your prompt first, review and edit the summary, then feed that back as the actual instruction. The agent is often better at compressing your intent than you are.

## What this connects to

Context engineering is the real-time practice. Two related topics:

- **Spec-driven coding** — the special case where (d) is handed off cleanly to the agent through a written spec and a test suite. A good spec is context engineering in slow motion.
- **Persistent docs as memory** — how you preserve (a) across sessions, compactions, and tool switches so you do not rebuild the context from scratch every time. This is what makes techniques like the fresh-agent reset from [the mental model](/guide/mental-model/) cheap instead of expensive.

If you only remember one sentence from this page: **the ideal context is not the one where you have added everything — it is the one where you cannot remove anything without losing something the agent needs.** Antoine de Saint-Exupéry: *"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."* Your context window is finite. Make every token in it load-bearing.
