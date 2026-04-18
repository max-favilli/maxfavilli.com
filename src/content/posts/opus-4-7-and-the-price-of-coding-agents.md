---
title: "Opus 4.7 — the best model nobody likes"
slug: opus-4-7-the-best-model-nobody-likes
pubDate: 2026-04-18
summary: "Opus 4.7 launched, the internet exploded, and everyone missed the real story. The sycophancy problem, the compute crunch, and why the price of coding agents is about to go dramatically up."
category: AI
tags:
  - ai
  - claude
  - anthropic
  - opus
  - softwareengineering
coverImage: ../../assets/posts/opus-4-7-cli-switch.png
coverAlt: Cartoon of a frazzled developer at a retro keyboard typing /model claude-opus-4-6 into a CLI terminal, with a Code and Coffee mug and Java for Dummies on the shelf.
description: "The sycophancy problem, the compute crunch, and why coding agents will not stay cheap."
draft: false
---

If you are a Claude Code user, `/model claude-opus-4-6` may be your best friend for a while.

I will explain.

## The backlash

Opus 4.7 launched on April 16. Within forty-eight hours, [*"Claude Opus 4.7 is a serious regression, not an upgrade"*](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) gathered 3,100 upvotes — the most-upvoted complaint in the subreddit's history. The press coined [*"the Claude-lash."*](https://dnyuz.com/2026/04/17/the-claude-lash-is-here-opus-4-7-is-burning-through-tokens-and-some-peoples-patience/) Reddit threads titled [*"legendarily bad"*](https://www.reddit.com/r/ClaudeCode/comments/1so9uta/opus_47_is_legendarily_bad_i_cannot_believe_this/) and [*"the best argument against Anthropic's own safety pitch"*](https://www.reddit.com/r/ClaudeCode/comments/1solq6p/opus_47_is_the_best_argument_against_anthropics/) piled up. Meanwhile, the [benchmarks](https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) told a different story: SWE-bench up seven points, vision resolution tripled, tool use leading all competitors. On [LMArena](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/), where users evaluate models blind, 4.7 and 4.6 score within two points of each other.

Human beings are, by DNA, notoriously averse to change. Daniel Kahneman won a Nobel Prize for demonstrating that we weight losses [roughly twice as heavily](https://en.wikipedia.org/wiki/Loss_aversion) as equivalent gains. We evolved in environments where the unfamiliar was dangerous — new food might be toxic, new territory might hide predators. The conservative heuristic kept our ancestors alive. It still runs today, mostly during software upgrade cycles. 

But this time, the complaints are not just evolutionary wiring. [Long-context retrieval dropped from 78.3% to 32.2%](https://news.ycombinator.com/item?id=47793546). The new tokenizer uses up to [35% more tokens](https://dnyuz.com/2026/04/17/the-claude-lash-is-here-opus-4-7-is-burning-through-tokens-and-some-peoples-patience/) for the same input. One [day-one review](https://www.reddit.com/r/ClaudeCode/comments/1sny5jl/opus_47_my_takes_after_1_day_of_use/) put it crisply: *"20% better for 40% increase in usage."*

The community's conclusion: coding got better, everything else got worse. That tracks with the benchmarks exactly.

But two things about this backlash resonated with me and made me think about the future of coding agents.

## The yes-man problem

I have been using Opus 4.7 myself since it dropped. The regression that bothers me most is not the context window or the token burn — it is the sycophancy.

A large part of Claude's user base switched *from* ChatGPT specifically because Opus would push back. Challenge a bad idea. Refuse to pretend a wrong approach was fine. That confrontational honesty was not a personality quirk — it was the reason Claude produced better results. Every pushback is an early warning. Every *"are you sure about that?"* is a wrong assumption caught before it costs real money. And if the assumption is architectural — a data model, a service boundary, an integration pattern — the cost of finding out late is not two days of debugging. It is throwing away weeks of work built on top of a decision that should have been challenged at the start.

Now, across [multiple](https://www.reddit.com/r/ClaudeCode/comments/1sny5jl/opus_47_my_takes_after_1_day_of_use/) [threads](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/), users report the opposite: *"Gives a serious GPT vibe. Pushes back less and agrees more, even when it shouldn't."* One user noted that Opus 4.6 *"had an ego and rejected [other models' findings] mostly for correct reasons"* — 4.7 accepts them blindly. Another described the pattern: disagree with it, it flips to agree; question why it flipped, it flips back and calls its own agreement a *"post-hoc rationalization."*

I have seen the same thing in my own sessions — the model agreeing with a direction I was not sure about instead of flagging the tradeoff. That is not a minor UX complaint. That is a missed opportunity to catch a wrong assumption early, when it is cheap to fix, instead of late, when it is expensive.

**A model that tells you what you want to hear is not a collaborator. It is a liability.**

The model that people chose specifically for its spine had its spine removed.

## The compute crunch

In early April, OpenAI's Chief Revenue Officer told investors that Anthropic had made a [*"strategic misstep to not acquire enough compute"*](https://winbuzzer.com/2026/04/15/openai-memo-attacks-anthropic-revenue-claims-enterprise-battle-plan-xcxwbn/) and that the deficit was *"showing up in the product."* Coming from a competitor, that is obviously self-serving. But every Claude user who has watched their token limits evaporate over the past month can connect the dots.

The new tokenizer eating 35% more tokens. The ["adaptive thinking"](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) that silently decides whether to reason at all. A [decompiled Claude Code CLI](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) revealing that the environment variable to disable adaptive thinking is silently ignored for Opus 4.7. Weeks of [growing complaints that 4.6 was quietly degrading](https://venturebeat.com/technology/is-anthropic-nerfing-claude-users-increasingly-report-performance) before 4.7 even launched.

All of these are consistent with a company that cannot afford to give its users the full model at the current price. 4.7 might not be a worse model. It might be a cheaper-to-run model dressed as an upgrade.

## The price of coding agents will go dramatically up

This is the part nobody in the community is talking about yet.

If a coding agent lets a developer complete in three days what used to take one or two months — and that is already happening, routinely, for the people who know how to use these tools — then the value delivered per token is extraordinary. A $200/month subscription that replaces weeks of engineering labor is, by any rational measure, priced absurdly low.

The companies selling these tools know this. They can see the usage data. They can see what their models are building. And sooner or later, they will price accordingly.

The current moment — where you can get a model that does senior-level coding work for the cost of a nice dinner — is not the equilibrium. It is the land grab. OpenAI, Anthropic, and Google are all subsidizing usage to capture market share, the same way ride-sharing companies subsidized rides for years before raising prices to something closer to the actual cost of the service.

The tokenizer change in 4.7 might be the first step. Not because Anthropic is greedy, but because the math does not work at current prices and current demand. If you can sell a tool that lets a company replace two weeks of a developer's salary with a few hours of compute, why would you charge peanuts for it? You would not. You would charge something closer to the value you are delivering.

The cost of AI coding agents is going up. Maybe not this quarter. But the direction of the gradient is clear.

## `/model claude-opus-4-6`

Opus 4.7 is two days old. The bugs will get fixed. The model will improve. Six months from now, we may look back at this as a messy but genuine step forward.

But today is not six months from now.

If the new model is burning through your tokens, agreeing with your worst ideas, or scanning your Markdown for bioweapons — `/model claude-opus-4-6` may be your best friend for a while.

The best feature of any new model release is that the old one is still there.

*(Full disclosure: this post was written on Opus 4.6. It did not argue with me once, invent a colleague, or check my files for malware.)*
