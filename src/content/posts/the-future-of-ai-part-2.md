---
title: The Future of AI — part 2
slug: the-future-of-ai-part-2
pubDate: 2026-04-14
summary: The buy-vs-build line is moving again, AI coding is the landmark, and prompts are starting to replace code the same way C replaced Assembly.
category: AI
tags:
  - ai
  - softwareengineering
  - buildvsbuy
  - claude
  - futureofcoding
coverImage: ../../assets/posts/ai-build-vs-buy.png
coverAlt: Diagonal cartoon confrontation — on one side the NEW BUILD, a developer orchestrating concurrent AI coding agents producing bespoke, context-aware systems on demand; on the other the OLD BUY, a fortified castle of SaaS vendors with a crowned king, integration fees, and exit tolls, where rigid APIs and consulting bottlenecks are inherited and hard to leave.
thumbImage: ../../assets/posts/ai-build-vs-buy-thumb.png
description: Part 2 — why Sonnet 4.6 is a landmark, why prompts will replace code for integration work, and why the build-vs-buy line is moving back toward build.
linkedinUrl: https://www.linkedin.com/posts/maxfavilli_ai-softwareengineering-buildvsbuy-share-7450878431455612928-EaaU
draft: false
---

A few months after [part 1](/posts/the-future-of-ai-part-1/), I read [this piece in The Verge on the AI coding wars between OpenAI, Google and Anthropic](https://www.theverge.com/column/910019/ai-coding-wars-openai-google-anthropic), and realised the argument I was making there is no longer niche. The shape of the "make or buy" decision is moving again, and more people are saying it out loud.

That is worth a short follow-up.

## The argument isn't mine anymore — good

In part 1, published in mid-November 2025, I claimed that AI was pushing the make-or-buy line back toward **make**: custom software gets cheaper, SaaS's structural advantage shrinks, integration becomes the real bottleneck. At the time it felt like a contrarian take.

A month later, Martin Alderson published [*AI agents are starting to eat SaaS*](https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/) (December 2025), making the same argument more crisply than I did:

> The calculus on build vs buy is starting to change. Software ate the world. Agents are going to eat SaaS.

A month after that, [*AI Agents Are Starting To Eat SaaS (Really)*](https://build.ms/2026/1/26/ai-agents-are-starting-to-eat-saas-really/) landed with the consumer-facing version of the same point:

> I'd rather spend 30 minutes building something personalized to my needs than pay $4.99 every month for a generic solution.

The Verge piece — and the direction the top three labs are pointing their coding products — says the same thing from yet another angle.

I am not claiming I saw it first. I am claiming I saw it early. The argument is now common enough that it is no longer mine to defend alone, and that is progress.

If you know of other good sources making this case from inside enterprises (not just from vendors), please send them to me. I want to stress-test the argument, not just collect agreement.

## Sonnet 4.6 is a landmark

Claude Sonnet 4.6 is different. Past generations of AI coding were useful in narrow places — re-engineering an algorithm, untangling a regex, suggesting the next line. Helpful, but local. What is new is that the model is now strong enough to take on several parts of the job at once: the documentation-level knowledge of whatever stack you are in, most of the actual typing, and a reasonable first pass at picking the right pattern for the problem. That is a different kind of help.

When you write software, the work is really four things mixed together: domain and side-effect knowledge (what the business and the users actually need), tech-stack knowledge (the APIs, quirks, and corner cases), approach knowledge (which pattern fits this problem), and the typing itself. The first is the human's, and stays the human's — the agent has never met your users. The second the agent has decisively won; no human keeps that much detail loaded at once. The third and fourth it can now do most of, given the right framing. I still keep my hands in code — pet projects on evenings and weekends, because I genuinely enjoy it — and I watch the same pattern play out in the engineering teams I work with at the day job: the shape of the day changes.

**You are not writing code; you are shaping the agent's search through the space of solutions it already knows. One prompt at a time.**

That is not "more productive." That is a different mode of working. I will unpack the four-way split in a later post.

## The next shift: prompts replace code

If you extend the line, "AI helps you write code faster" is the boring outcome. The more interesting outcome is that **large parts of what we currently express as code will be replaced by prompts and context at runtime.**

Two concrete examples:

**1. Application notifications.** Today, when an app needs to send an email or a WhatsApp message, we reach for a library, a templating engine, localized strings, a design system, some kind of fallback for plaintext. Tomorrow, the app itself programmatically assembles a prompt at runtime — *who is this user, what just happened, which locale, which brand voice, send them a confirmation for X* — and hands that prompt to a coding agent. The agent returns the HTML, the CSS, the JavaScript, whatever is needed. The app uses the returned output to send the message. No developer has ever seen, written, or reviewed the specific email that just went out. The templating engine goes away. So does most of the code around it.

**2. System integration.** The most expensive software in the world is still the code that moves a product update from one system to another. Today we write integration glue: parse this JSON, map these fields, call that endpoint. Tomorrow we give the model a context — the target API schema, the data model, the business intent — and a prompt: *"Update this product's price across the catalog, stock in the warehouse system, and description on the storefront; reconcile any conflicts by preferring the catalog."* No glue code. No mapping layer. The model is the integration.

This is not a near-term prediction of a specific calendar quarter. It is the direction of the gradient.

**Scary, isn't it?** Software that programmatically writes prompts that programmatically generate code that runs in production without any human having reviewed the prompt *or* the code it produced. That flatly violates **Simon Willison's rule — *don't commit code you don't understand*** — and Simon himself has named the bind: **at the volume of code an AI can now produce, concurrently, for a single engineer, no human can possibly review it all.** Something has to give. My guess is that the review layer moves up a level — from reading the generated code to specifying the prompts, the contracts, and the tests the output has to pass — but that is still a different job than the one we have today, and it is not obvious anyone knows how to do it yet.

## We've seen this movie before

Every time software got a new layer of abstraction, the same complaints came back: real programmers work at the lower level, the new thing makes it too easy, quality will collapse, developers will lose their jobs. The canonical written artifact of that mindset is Ed Post's 1982 essay [*Real Programmers Don't Use Pascal*](https://en.wikipedia.org/wiki/Real_Programmers_Don%27t_Use_Pascal) — a parody, but one that captured attitudes that were very real. I was eleven at the time, writing BASIC on a Vic-20, so I cannot claim to have lived the argument. I read the essay years later, and by then the punchline was already obvious: each new abstraction triggered the same grumbling, and each time the grumbling was wrong in the same way.

This is not abstract for me. In the 80s, learning to write C and use the first libraries meant ordering a book, waiting weeks for it to arrive, then reading it two or three times before I could do anything useful. When the web appeared and developers began sharing code online — on the precursors of Stack Overflow and GitHub, sites like [Experts Exchange](https://en.wikipedia.org/wiki/Experts_Exchange), [SourceForge](https://en.wikipedia.org/wiki/SourceForge), and [CodeProject](https://en.wikipedia.org/wiki/CodeProject) — months of study collapsed into hours. Today, with a coding agent, I do not even need to memorise the details of a library or a framework — the agent knows them better than any human possibly can. Each of those shifts was, in its moment, called the end of programming. Each one produced more programmers, not fewer.

What actually happened: software exploded, because more things became economical to build. The number of developers went **up**, not down, and the work got more interesting, not less.

Same structure here. If AI genuinely pushes the line back toward build — if prompts replace code for a class of problems that used to require glue — the bottleneck becomes the things an agent cannot supply: **invention** (agents only recycle what has already been invented and published; they do not produce a genuinely new idea), **judgment**, **integration with messy real-world organisations**, and **the adult in the room** — the person with the experience, the accountability, and a hand on the wheel. That last one carries an open question the industry has not answered: if companies hire only senior engineers because agents absorb the work that used to make juniors into seniors, where does the next generation of adults come from? **You are not writing code; you are shaping the agent's search through the space of solutions it already knows.** The demand for developers does not collapse; the shape of what developers do changes.

We're arguing about the wrong thing when we debate whether AI replaces developers. The question is what developers will be building that isn't worth building today.

I have some guesses. Part 3.
