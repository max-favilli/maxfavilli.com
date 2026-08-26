---
title: We are measuring AI productivity wrong
slug: measuring-ai-productivity-wrong
pubDate: 2026-09-08
summary: The studies say AI makes developers 10% faster, or even slower. My experience says weeks became half a day. Both are true — because the studies measure effort, and the change is in outcomes.
category: AI
tags:
  - ai
  - softwareengineering
  - productivity
  - metrics
coverImage: ../../assets/posts/ai-build-vs-buy.png
coverAlt: A cartoon researcher measuring a rocket launch with a bicycle speedometer, clipboard in hand, while the rocket lifts off in the background.
description: METR says slower, DX says 10% not 10x. But PR counts and task timers measure effort, not outcomes — and the market pricing software work has already moved on.
draft: true
---

<!-- TODO: replace placeholder cover image -->

The measured evidence on AI coding productivity is underwhelming. METR ran a randomized controlled trial and found experienced open-source developers were about 20% *slower* with AI tools — while believing they were faster. DX tracked telemetry across ~400 engineering organizations and found AI usage up 65% but pull-request throughput up only 7.76%. Their headline: "10%, not 10x."

My experience, after thirty years in software and the last two working daily with coding agents, is that we ship in half a day what used to take weeks. The teams I work with at the day job see the same.

Somebody must be wrong. I don't think anybody is. I think the studies measure the wrong thing.

## What the studies actually measure

Look at the instruments. DX counts merged pull requests per engineer. METR timed developers on ~2-hour tasks — experienced maintainers working on their own large, mature repositories, code they know intimately. The survey evidence (Fastly's, showing seniors ship AI code at 2.5x the rate of juniors) is self-reported adoption share, not measured output.

Pull requests, lines of code, tickets closed — these are effort proxies. They measure motion, not outcomes. Every engineering manager knows different developers produce wildly different code for the same result; the same is true with and without AI. If an agent lets one developer deliver a working product in two days instead of six weeks, PR throughput might not move at all. The unit of delivery changed, not the count.

And METR's design is close to the worst case for AI: small tasks, deep tacit knowledge already in the developer's head, legacy code. That is precisely where the DORA data says AI helps least — around 10% on complex legacy work, versus 35–40% on greenfield. The thing my half-day stories describe — senior engineers steering agents through greenfield, product-level delivery — no study has measured at all.

## The market already voted

Here is the evidence I find more persuasive than any telemetry: the industry that sells software effort is abandoning effort as a unit of billing. Cognizant reports 47% of sales on outcome-based contracts. ExlService is at 36% and targeting the mid-40s. Grid Dynamics, Globant, Endava — the whole system-integrator sector is repricing from time-and-materials to outcomes.

Consultancies do not walk away from billable hours out of generosity. They do it when the hour stops being a defensible unit of value. The market that prices software work has concluded effort no longer tracks value — while researchers are still counting PRs.

## Honest closing

My half-day stories are anecdotes, and I hold them to the same standard as anyone else's. The studies are not wrong; they are careful measurements of a layer where the change is small. But every regime change looks like this at the start: the averages move slowly while the frontier moves fast, and the instruments built for the old regime keep reporting that nothing much is happening.

If you want to know whether software development changed, don't count the pull requests. Count what shipped.
