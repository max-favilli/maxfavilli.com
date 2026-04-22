---
title: "Token economy"
slug: token-economy
order: 7
description: "Where tokens go, what is worth spending them on, and why ELI5 comments pay for themselves."
---

Every interaction with a coding agent costs tokens. Tokens are how the model measures text — roughly one token per four characters, or about 750 words per 1,000 tokens. Code tokenizes less efficiently than prose because of special characters, indentation, and syntax: expect 30-40% more tokens for the same amount of information compared to plain English.

This matters because your context window is finite, and because tokens cost money. Understanding where tokens go helps you make better trade-offs.

## Where tokens go

In a typical coding session, tokens are spent on:

- **The system prompt and project configuration.** CLAUDE.md, tool definitions, session setup. This is fixed overhead — it is there whether you use it or not.
- **Files the agent reads.** Every file the agent opens goes into the context window. A large file costs more tokens than a small one.
- **The conversation history.** Every message you send and every response the agent gives accumulates. Long conversations cost more per turn than short ones because the entire history is re-processed at each step.
- **Tool calls and results.** When the agent runs a command, reads a file, or searches the codebase, both the call and the result consume tokens.
- **The agent's own output.** Code it writes, explanations it gives, plans it proposes.

## The real token sinks

Not all token spending is equal. Some is investment, some is waste.

**Investments (spend freely):**
- Reading the right files before editing. Costs a few hundred tokens, saves thousands by avoiding wrong turns.
- Writing and reading project docs (vision, roadmap, specs). Costs tokens once, pays back every session.
- Running tests. A test run result is cheap and tells the agent exactly what to fix.
- ELI5 code comments. More on this below.

**Waste (avoid):**
- **Doom loops.** By far the largest token sink. The agent tries, fails, tries again, invents APIs, tries again — each iteration costs tokens and the context grows with every failed attempt. Five rounds of a doom loop can cost more than the entire rest of the session. Recognize it early, stop, reset.
- **Loading irrelevant context.** Dumping the whole codebase, reading files that have nothing to do with the task, pasting documentation "just in case." Every irrelevant token displaces a relevant one.
- **Long unfocused conversations.** A session that wanders across five topics without committing or checkpointing accumulates a massive conversation history. The agent re-processes all of it on every turn. Keep sessions focused, commit and update docs frequently, start fresh when the topic changes.

## Do ELI5 comments cost more tokens?

Yes. A well-commented file is roughly 30-40% more tokens than an uncommented one.

It is worth it. Here is why:

- **Comments are "invest once, read forever."** You write them once. Every future session where the agent reads that file benefits. The alternative — explaining the code via prompts every time — costs more tokens total because you repeat yourself.
- **Plain English is more token-efficient than code per unit of information.** A comment explaining a function is fewer tokens per insight than reverse-engineering the same insight from the code.
- **Correct understanding on the first read saves iteration tokens.** An uncommented file might save 200 tokens on the read but cost 2,000 in back-and-forth because the agent misunderstood the intent.

The same logic applies to clear commit messages, decision logs, and spec files. These are all load-bearing tokens — they carry information that prevents more expensive token spending downstream.

## Why design-first saves tokens

Every time you send a message, the entire conversation history is re-sent to the model. The system prompt and tool definitions get cached (90% discount), but your messages are processed fresh every turn. The cost curve is effectively quadratic: each turn is more expensive than the last because the context is bigger.

This is why designing and coding in one long continuous session is expensive. A 20-turn design conversation means by turn 20, the agent re-processes all 20 previous exchanges. Then coding starts, and every coding turn *still* carries all 20 design exchanges. You are paying for your design conversation on every single coding turn.

The design-first approach from [Session discipline](/guide/session-discipline/) breaks this cycle. You run the design session, persist the result to a plan document on disk, then start a **fresh** coding session. The coding session's context is:

- System prompt + tools + CLAUDE.md → cached, 90% discount
- The plan document → read once, maybe 2,500 tokens
- Your message ("implement this") → 50 tokens

Instead of dragging 25,000 tokens of design conversation through every coding turn, you have a 2,500-token document read once into a clean context. The savings compound: the longer the coding session runs, the more you save by not carrying the design history.

### How to make it even cheaper

**Front-load context in fewer messages.** During the design session, prefer one well-structured message with all your context over 10 short exchanges. Each exchange adds two messages to the history that gets re-sent on every subsequent turn.

**Persist decisions during the design session, not after.** As soon as a decision crystallizes, write it to the file. In subsequent turns, say "see the plan in `plan.md`" instead of re-explaining. This keeps the live conversation smaller.

**Start a genuinely fresh session for implementation.** Do not continue the design session into coding. Close it, open new. Maximum cache efficiency.

**Make the plan document concise.** The agent reads the whole thing into context. A 300-line plan is better than a 1,000-line plan carrying the same information. Saint-Exupéry applies to token economy directly.

**Respect the 5-minute cache TTL.** If you pause to think for more than 5 minutes, the cache goes cold and the next turn pays for a full cache rewrite. Either keep turns flowing (each hit resets the timer), or accept the cold start and make the next turn count.

**Use roadmap.md instead of conversation memory.** The "what's next" information lives in a file (~200 tokens to re-read) rather than in conversation history (which grows and never shrinks until compaction).

**ELI5 comments are a token investment.** A well-commented file costs 30-40% more tokens to read. But the agent understands it on the first read instead of needing follow-up questions — 200 extra tokens on comments save 2,000 tokens of back-and-forth.

## The Saint-Exupéry rule, applied

The ideal context is not the one where you added everything — it is the one where you cannot remove anything without losing something the agent needs.

Apply this to token spending: every token in the context window should be load-bearing. If it is not helping the agent produce better output, it is displacing something that would. Comments, specs, and project docs are load-bearing. Irrelevant files, stale conversation history, and doom loop residue are not.

You do not need to count tokens manually. But developing an intuition for what is signal and what is noise — and having the discipline to keep the context clean — is what separates productive agent users from people who hit rate limits and wonder why.

The less tokens you burn, the longer the fun.
