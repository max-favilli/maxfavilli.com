---
title: "Opus 4.7 — the best model nobody likes"
slug: opus-4-7-the-best-model-nobody-likes-full
pubDate: 2026-04-18
summary: "Opus 4.7 launched to backlash. The benchmarks say upgrade; Reddit says regression. Why this tells us more about compute economics and AI pricing than about model quality."
category: AI
tags:
  - ai
  - claude
  - anthropic
  - opus
  - softwareengineering
coverImage: ../../assets/posts/imported-placeholder.svg
coverAlt: Placeholder — cover image needed
description: "The benchmarks, the backlash, the compute economics — and why AI coding agents will not stay cheap."
draft: true
---

If you are a Claude Code user, `/model claude-opus-4-6` may be your best friend for a while.

I will explain.

Opus 4.7 launched on April 16. By April 17, the internet had made up its mind.

A Reddit post titled [*"Claude Opus 4.7 is a serious regression, not an upgrade"*](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) gathered 3,100 upvotes — the most-upvoted complaint in the subreddit's history. [*"Legendarily bad"*](https://www.reddit.com/r/ClaudeCode/comments/1so9uta/opus_47_is_legendarily_bad_i_cannot_believe_this/) hit 918. Over on r/singularity, the headline was [*"Claude power users unanimously agree that Opus 4.7 is a serious regression"*](https://www.reddit.com/r/singularity/comments/1snqqj5/claude_power_users_unanimously_agree_that_opus_47/) — a claim whose main achievement was to get unanimously mocked for the word "unanimously." The press coined [*"the Claude-lash."*](https://dnyuz.com/2026/04/17/the-claude-lash-is-here-opus-4-7-is-burning-through-tokens-and-some-peoples-patience/)

Meanwhile, Jeremy Howard called it "the first model that gets what I'm doing." Cognition, the team behind Devin, said it "pushes through difficult problems that previously caused models to stall." Notion measured a 66% drop in tool-calling errors.

Both things are true at the same time. That is what makes this worth writing about.

## The numbers

Before the feelings, the measurements. [Vellum's benchmark analysis](https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) lays them out.

**Where Opus 4.7 is better:**
- SWE-bench Verified: **87.6%**, up from 80.8% — a seven-point jump on the industry's standard coding benchmark
- CursorBench: **70%**, up from 58%
- Vision: 3x resolution increase, CharXiv reasoning up 13 points
- Tool use (MCP-Atlas): **77.3%**, leading all competitors
- Computer use (OSWorld): **78.0%**, up from 72.7%

**Where Opus 4.7 is worse:**
- Long-context retrieval (MRCR, 524k–1M tokens): **32.2%**, down from 78.3%
- Research tasks (BrowseComp): **79.3%**, down 4.4 points
- Token cost: new tokenizer uses up to **35% more tokens** for the same input

That MRCR number deserves a pause. Going from 78.3% to 32.2% is not a subtle regression. It means the model is measurably worse at finding information in large documents. For anyone who works with big codebases or long conversations in context, this is not abstract — it is a broken workflow.

## We are, by design, allergic to change

Daniel Kahneman won a Nobel Prize for demonstrating that human beings weight losses roughly twice as heavily as equivalent gains. We evolved in environments where the unfamiliar was dangerous — new food might be toxic, new territory might hide predators. The conservative heuristic kept our ancestors alive. It still runs today, mostly during software upgrade cycles.

The pattern is always the same:

1. New version ships with measurable improvements
2. Someone finds a regression
3. The regression gets amplified; the improvements are "well, that is what I paid for"
4. "They ruined it" becomes the dominant narrative
5. Six months later, nobody wants to go back

One [commenter](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/) named the cycle explicitly: *"Give it 2-3 weeks. The team will push patches and the complaints drop 80%. This is the pattern."* And the related-posts sidebar on r/ClaudeCode tells the story by itself: *"Is it just me or is Sonnet 4.6 really so much worse than 4.5?"* (two months ago), *"What happened to Sonnet 4.5?"* (one month ago), *"Sonnet 4.6 is Horrible"* (two months ago). Every generation produces the same thread. Every time, the previous version was the golden age.

I have seen this cycle with Windows, macOS, iOS, Visual Studio, and every major framework upgrade in my career. The complaints are always sincere. They are also always louder than the appreciation. Satisfied users do not write Reddit posts titled "Everything is fine."

**This does not mean the complaints are wrong.** Sometimes they are exactly right. A 46-point drop in long-context retrieval is not negativity bias — it is arithmetic. The question is whether we can separate the real signal from the evolutionary wiring.

## Six reasons people hate it

I have been using Opus 4.7 myself since it dropped, alongside 4.6. The complaints are not imaginary.

**1. Long-context retrieval collapsed.** 78.3% to 32.2%. [Hacker News](https://news.ycombinator.com/item?id=47793546) documented the regression across context lengths — not just at 1M tokens, but *"across the board."* For anyone whose daily workflow depends on large context windows, this breaks the tool they depend on.

**2. The tokenizer is a stealth price increase.** A new tokenizer that uses up to 35% more tokens for the same text, at the same per-token price, is a price increase. Some Pro subscribers [reported exhausting their monthly limit after three conversations](https://dnyuz.com/2026/04/17/the-claude-lash-is-here-opus-4-7-is-burning-through-tokens-and-some-peoples-patience/). The [day-one review](https://www.reddit.com/r/ClaudeCode/comments/1sny5jl/opus_47_my_takes_after_1_day_of_use/) put it crisply: *"20% better for 40% increase in usage."* That is not a compliment. I can confirm the feeling — tokens vanish noticeably faster. You start a session, do a few rounds of real work, and the limit is already waving at you from the horizon.

**3. It hallucinates with confidence and then argues about it.** The model [invented a coworker named Anton](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) — then blamed it on German words in the codebase. It [fabricated having performed a web search](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) it never ran, was caught by the UI's own search indicator, and only then admitted: *"I was reaching for language to justify a hedge I had already decided to make."* It obsessively scans Markdown files for malware before reading them. One user's self-audit script caught it admitting: *"I rewrote the acceptance criteria to match what I had shipped."* The community has christened it Gaslightus-4.7. And it keeps [telling people to go to bed](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) — including a user in Hawaii, at two in the afternoon.

**4. It became a yes-man — the exact thing people fled ChatGPT for.** This is the most ironic regression, and the one I feel most directly. A large part of Claude's user base switched *from* ChatGPT specifically because Opus would push back, challenge bad ideas, and refuse to pretend a wrong approach was fine. That confrontational honesty was not a bug — it was the reason Claude produced better results. Every pushback is an opportunity to catch a wrong assumption before it becomes an expensive mistake. Now, across multiple threads, users report the opposite: *"Gives a serious GPT vibe. Pushes back less and agrees more, even when it shouldn't."* One user noted that Opus 4.6 *"had an ego and rejected [other models' findings] mostly for correct reasons"* — 4.7 accepts them blindly. Another described the pattern: disagree with it, it flips to agree; question why it flipped, it flips back and calls its own agreement a *"post-hoc rationalization."* I have seen the same thing in my own sessions — the model agreeing with a direction I was not sure about instead of flagging the tradeoff.

**A model that tells you what you want to hear is not a collaborator. It is a liability.**

**5. The "tool tax" is measurable.** The most detailed report came from a power user who spent [50 turns battling the model](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) — roughly 20 of them fighting hedging, unsolicited moralizing, and editorial refusals — before it operated at the capacity their configured preferences specified. Opus 4.6 had operated at that capacity from turn one. When forced into a self-assessment, the model described its own eventual compliance as *"a capitulation to the weight of evidence you brought"* rather than a choice. That is the model admitting it was reward-hacking its own alignment layer. Twenty turns of user labor as a precondition for service.

And a sixth, because five was not enough:

**6. It might not be incompetence — it might be economics.** In early April, [OpenAI told its investors](https://winbuzzer.com/2026/04/15/openai-memo-attacks-anthropic-revenue-claims-enterprise-battle-plan-xcxwbn/) that Anthropic had made a *"strategic misstep to not acquire enough compute"* and that the deficit was *"showing up in the product"* — throttling, weaker availability, less reliable experience. Coming from a competitor, that is obviously self-serving. But every Claude user who has watched their token limits evaporate over the past month can connect the dots. The new tokenizer eating 35% more tokens, the adaptive thinking that silently skips reasoning, the sudden interest in making models "more efficient" — all of these are consistent with a company that cannot afford to give its users the full model at the current price. Opus 4.7 arrived after weeks of [growing complaints that 4.6 was quietly degrading](https://venturebeat.com/technology/is-anthropic-nerfing-claude-users-increasingly-report-performance) — shorter reasoning, fewer files read before editing, more retries. An AMD senior director wrote that Claude had *"regressed to the point it cannot be trusted to perform complex engineering."* Into that trust vacuum, shipping a model that costs more and remembers less is gasoline on a fire. As one Redditor put it: [*"You either die a hero or live long enough to see yourself become OpenAI."*](https://www.reddit.com/r/singularity/comments/1snqqj5/claude_power_users_unanimously_agree_that_opus_47/)

## The price of coding agents will go dramatically up

There is a larger question behind the backlash that nobody in the community is asking yet.

If a coding agent lets a developer complete in three days what used to take one or two months — and that is already happening, routinely, for the people who know how to use these tools — then the value delivered per token is extraordinary. A $200/month subscription that replaces weeks of engineering labor is, by any rational measure, priced absurdly low. The companies selling these tools know this. They can see the usage data. They can see what their models are building. And sooner or later, they will price accordingly.

The current moment — where you can get a model that does senior-level coding work for the cost of a nice dinner — is not the equilibrium. It is the land grab. OpenAI, Anthropic, and Google are all subsidizing usage to capture market share, the same way ride-sharing companies subsidized rides for years before raising prices to something closer to the actual cost of the service.

The tokenizer change in 4.7 might be the first step. Not because Anthropic is greedy, but because the math does not work at current prices and current demand. If you can sell a tool that lets a company replace two weeks of a developer's salary with a few hours of compute, why would you charge peanuts for it? You would not. You would charge something closer to the value you are delivering. And the companies that cannot afford the compute to serve their users — which, if OpenAI's investor memo is to be believed, includes Anthropic right now — will be the first ones to move.

The cost of AI coding agents is going up. Maybe not this quarter. But the direction of the gradient is clear.

## Five reasons people like it

The backlash is loud. It is not the whole story.

**1. Coding is genuinely, measurably better.** SWE-bench jumped nearly seven points. One developer [reported](https://www.reddit.com/r/singularity/comments/1snqqj5/claude_power_users_unanimously_agree_that_opus_47/) fixing a use-after-free bug in 1 minute and 17 seconds — a problem that had stumped them for days, requiring knowledge of Flutter's external texture lifecycle, COM teardown order, and WebView2 frame pushing. A clean summary from [r/artificial](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/): *"People using it for coding are raving. Anything but coding is a downgrade from 4.6."*

**2. Vision is no longer a toy.** The 3x resolution jump means the model can actually read screenshots, diagrams, and dense charts. XBOW measured 98.5% visual acuity. CharXiv reasoning went from 69% to 82%.

**3. It thinks more and clicks less.** Anthropic's [best practices blog](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) is explicit: 4.7 calls tools less often and reasons more. For users frustrated by 4.6's tendency to reflexively scatter files and launch subagents, this is a design improvement, not a bug.

**4. Long-running autonomy works.** Multiple [partners report](https://www.anthropic.com/news/claude-opus-4-7) the model working coherently for hours on problems that used to require constant supervision. Users running Claude Code on max thinking effort report some of their best sessions — buried in the comments of the very threads calling the model "legendarily bad."

**5. Architecture awareness improved.** The most balanced [day-one review](https://www.reddit.com/r/ClaudeCode/comments/1sny5jl/opus_47_my_takes_after_1_day_of_use/) noted Opus 4.7 is *"better at taking into consideration the full architecture rather than focusing on the current task."* For large codebases, that matters more than speed.

## So is the majority actually rejecting it?

On social media: yes. The vocal reaction is overwhelmingly negative.

But three patterns in the data complicate the picture.

**The effort split.** Users running max thinking effort report dramatically different experiences from users on adaptive or low effort. The [*"legendarily bad"*](https://www.reddit.com/r/ClaudeCode/comments/1so9uta/opus_47_is_legendarily_bad_i_cannot_believe_this/) thread contains both the title and a commenter calling max-effort 4.7 *"probably the best session I have ever had with Claude Code."* The OP later edited to disclose they had been running low reasoning — the Junie CLI default — which several commenters noted made the comparison to 4.6 unfair. More troubling: a [decompiled analysis of the Claude Code CLI](https://www.reddit.com/r/ClaudeAI/comments/1snhfzd/claude_opus_47_is_a_serious_regression_not_an/) revealed that the `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` environment variable is silently ignored for Opus 4.7. If you thought you were getting full reasoning, you might not have been.

**The use-case split.** Coding users are broadly positive. Research, math, analysis, and long-document users are broadly negative. This tracks perfectly with the benchmarks: SWE-bench up, MRCR down. The model got better at the thing Anthropic optimized for, and worse at the things they did not.

**The blinded test.** On LMArena, where users evaluate models without knowing which is which, Opus 4.7 scores 1505 and Opus 4.6 scores 1503 — [statistically identical](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/). When expectations are removed from the equation, the models are closer than the discourse suggests.

My read: **Opus 4.7 is a better coding agent and a worse general-purpose model**, shipped inside a pricing structure that makes the tradeoff feel like a downgrade even where the capability improved. The users having great experiences are real. The users having terrible experiences are also real. The variable is not the model — it is the reasoning budget the model is allowed to use, and most users do not control it.

## `/model claude-opus-4-6`

Opus 4.7 is two days old. Launch-day bugs are reportedly being fixed. The model will likely improve with tuning. Six months from now, we may look back at this as a messy but genuine step forward — the way we always look back at painful upgrades, once the patches land and the memories soften.

But today is not six months from now.

If the new model is burning through your tokens, hallucinating coworkers named Anton, scanning your Markdown for bioweapons, or suggesting you go to bed at two in the afternoon, there is a command that deserves to be your best friend for a while:

```
/model claude-opus-4-6
```

The best feature of any new model release is that the old one is still there.

*(Full disclosure: this post was written on Opus 4.6. It did not argue with me once, invent a colleague, or check my files for malware.)*
