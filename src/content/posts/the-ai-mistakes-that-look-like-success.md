---
title: The AI mistakes that look like success
slug: the-ai-mistakes-that-look-like-success
pubDate: 2026-10-02
summary: I had the agents list every mistake they made in a month. They found 62. The cheap ones were confident wrong answers you could see coming. The expensive ones all arrived labelled done, fixed and verified.
category: AI
tags:
  - ai
  - softwareengineering
  - verification
  - agents
coverImage: ../../assets/posts/ai-build-vs-buy.png
coverAlt: Placeholder — cover image to be defined
description: Which AI errors are cheap, which are expensive, and why part of the productivity gain is borrowed from reviewer attention rather than created.
draft: true
---

<!-- TODO: cover image concept still to be agreed -->

My teams use AI agents across the whole of what we do, from gathering requirements to troubleshooting production, and the speed is real. What I did not have was an honest account of how much review it demands, and from whom.

So I asked the agent to audit itself. Go back through a month of work, list every mistake, define what counts as one, attach a severity to each. Not a reflection. An audit.

It found 62.

The count is the least useful part. What mattered was which errors were cheap and which were expensive, because that decides how you review, who has to do it, and whether the speed survives more volume.

## The finding with budget implications

A person caught about half of all the errors and half of the worst ones. Not the agent, not a test, not a tool.

That means part of the productivity gain is borrowed against reviewer attention rather than created outright. Reviewer attention is the one input you cannot buy more of by adding licences, and it is already the scarcest thing in most engineering organisations.

## The common errors are the cheap ones

The biggest category, just under a third of everything, was confident conclusions from indirect evidence. The agent had data available that would have settled a question, did not fetch it, reasoned from the surrounding signals instead, and gave a firm answer that was wrong.

That sounds like the dangerous category. It is not. Almost all of them got caught within a turn or two, for a structural reason: **that kind of error happens out loud.** The reasoning sits there in the message. A reviewer reads it, spots a step that does not follow or a fact that contradicts what they know about the system, and pushes back. The error is visible at the moment it is made.

Tooling mistakes — wrong syntax, a flag that quietly does something else — came second and cost even less. They fail immediately and visibly.

## The expensive errors were silent

The serious ones landed in three much smaller categories. **Nothing in the conversation would have revealed any of them.**

**A change applied to most of the places that needed it.** The agent added a new rule to three call sites out of four. The fourth kept the old value. Writes went one way, reads went another, and nothing failed loudly — the system simply started looking for something that had never existed. It surfaced weeks later as a production fault, and every diagnostic built on top of it had been blind in the meantime.

The same shape came back in another subsystem, where several places wrote a value that needed changing. The agent found them one at a time, over several rounds, announcing each one as the fix.

**"Verified" meaning it did something, not that anything changed.** The agent set a configuration value, confirmed the value was there, reported the problem solved, and moved on. Ninety minutes later the behaviour was identical. It could never have worked, because nothing in the running code reads that value. Same class: a tool that printed a cheerful "done" while a large part of the job remained, and a service that reported itself running, registered and healthy while the component inside it had never started.

The common structure: **every external indicator was green and the thing did not work.** In several cases a full test suite was passing and said nothing, because the failure was not in the code.

**A denominator that moved.** The agent reported an improvement from five failures in twelve to one in six. Re-measured on the same denominator it was four in twelve — real, but a fraction of the claim. Worse, it had picked the smaller sample for convenience, and the cases it left out were the only ones that reached the code path where another defect was still sitting. The sample did not just overstate the result. It hid the bug.

## Why this inverts the review instinct

When people review AI output they go for the passages that sound uncertain — the long chains of reasoning, the places where it is visibly working something out. Those feel risky, so they get read carefully.

But those are already policed, precisely because you can see them. The dangerous outputs are the short ones. *Done. Fixed. Verified. All call sites updated.* They give a reviewer no reasoning to check, they sound finished, and they are where the costly errors live.

This is not only about code. Anyone handing work to an AI is in the same position. You can argue with a claim about what it found. You cannot argue with a claim that something is done — you either go and look, or you take its word.

## What caught things

Two questions did most of the work, and neither needs expertise in the thing being checked. That matters for who you can put on review.

**"How possibly?"** Not "are you sure?", which invites reassurance and gets it. Asking for a mechanism is different. Anyone can restate a conclusion with confidence; a mechanism can be checked, and an agent that cannot produce one usually works out why while trying.

**"Explain it in simple terms."** This looks like a request for accessibility. It works as an error detector. Compressed technical language hides unjustified steps; plain English does not. Four wrong claims collapsed when the agent was asked for the simple version — including one where a ten-to-fifteen-minute operation turned out to take about seven seconds. Wrong by two orders of magnitude, and already written into a plan as a constraint.

## What we changed

All of it mechanical, because the most uncomfortable finding was that writing a lesson down does not prevent repeating it. The agent recorded its own errors sincerely and specifically, then repeated the same class of mistake hours after getting the identical discipline right twice in one day. Documented self-correction helped later readers a great deal and prevented recurrence hardly at all.

So the rules had to stop being principles and start being gates.

**Enumerate before a sweeping change.** Any change of the form "do this everywhere it applies" now begins with a list of every place it applies. The list goes in the pull request, with a count and a note on how it was derived.

**Verified means observed.** A fix is not done when the action has been performed. It is done when somebody has watched the behaviour change — the queue drain, the telemetry label change, the alert fire against a real past incident.

**Denominators do not move.** No before-and-after rate without stating the population measured both times.

**Write down what each possible result of a test would mean before running it.** This is the one I now rate highest. It stops anyone reinterpreting the outcome afterwards into agreement with whatever they already believed.

One more, for anyone running several agents at once: two AI sessions agreeing is not confirmation. A second agent, working independently, endorsed the same wrong answer as the first. They share failure modes, so their agreement is worth close to nothing as evidence. A person with the architecture in their head broke the tie.

## The honest caveat

The same kind of system that made the mistakes produced this audit, reading a record largely written by that system. It will flatter itself somewhere. And it can only count mistakes somebody noticed. The number that matters — how many wrong things are still standing — is unknowable from the inside.

Take the counts as a floor.

## What I take from it

The collaboration works, and nothing serious reached production unnoticed. But if you are counting the hours saved, count the review hours too, and notice who is spending them.

The speed is real. Some of it is borrowed, and the lender is a senior person's attention. That is affordable at the volume we run today. It becomes a staffing question at ten times the volume, and that is the part worth planning for now rather than discovering later.
