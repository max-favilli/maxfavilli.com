---
title: Anthropic IPO — is it a buy?
slug: anthropic-ipo-is-it-a-buy
pubDate: 2026-09-30
summary: George Noble calls it the most dangerous deal of his 45-year career. I read him regularly and I think he is wrong here. The evidence rests on a document nobody can open, and what can be checked cuts both ways.
category: Investing
tags:
  - ai
  - anthropic
  - ipo
  - investing
coverImage: ../../assets/posts/anthropic-ipo.png
coverAlt: Two-panel editorial cartoon. On the left, a stock exchange listing ceremony — an executive rings a brass bell at a podium amid confetti, cheering bankers and a share price line climbing on the screen behind. On the right, a quiet Chinese research lab with server racks, a national flag on the wall, the Shanghai skyline at dusk through the window, and three engineers working at their monitors while a small wall screen shows the ceremony none of them is watching.
thumbImage: ../../assets/posts/anthropic-ipo-thumb.png
description: The loudest bear case on the year's biggest listing. What holds up, what does not, and what business payment data actually shows.
linkedinUrl: https://www.linkedin.com/posts/maxfavilli_ai-anthropic-investing-share-7511328763280855040-OiFc
draft: false
---

The listing is expected before the end of the year. George Noble calls it the most dangerous deal of his forty-five-year career. I read him regularly and I disagree.

## The document nobody can read

[His case](https://georgenoble.substack.com/p/this-anthropic-ipo-is-the-most-dangerous) opens with Anthropic's prospectus, which he says warns that the models could resist being shut down and could hide or manipulate information.

Around 80 of the draft's 261 pages are risk factors. That section exists to list every conceivable hazard so the company cannot later be sued for omitting one.

There is no public prospectus. Anthropic submitted its draft confidentially on 1 June 2026 and nothing has appeared on EDGAR — no ticker, no price, no date. What exists is a leaked copy, [reported by Reuters and others on 28 September](https://fortune.com/2026/09/29/anthropic-ipo-s-1-prospectus-income-statement/). That is what he is quoting, and what I am quoting.

## Where he is right

**Customer concentration.** A quarter of 2025 revenue came from two customers, reported as GitHub and Cursor. GitHub belongs to Microsoft, OpenAI's largest backer. Cursor's parent is being bought by SpaceX, which owns xAI. Both are owned by competitors, and both pick a model per request — leaving Claude is a routing change, not a migration.

**Compute commitments.** Hundreds of billions of dollars over a decade, most of it payable whether the demand arrives or not.

## Where he is not

**"Only one in five American businesses use AI."** Ramp, which tracks what US businesses actually pay for, [found 43.5% of them paying Anthropic in July](https://ramp.com/data/ai-index-august-2026). Its sample skews more technical than the economy does, by its own admission, so read that as generous — but it is one vendor, not the whole category.

**"No customers"** contradicts his own concentration argument, and the figures settle it: revenue of about $4.6 billion across 2025, $11.5 billion in the second quarter of 2026 alone, and an annualised run rate of $65 billion by the end of July.

**The 25% is a 2025 snapshot** — a share of that $4.6 billion year, not of the $11.5 billion quarter. The business excluding those two customers grew more than elevenfold over the same period.

## This is not SpaceX 2.0

His parallel is his own SpaceX call — index inclusion forcing tracker funds to buy, retail arriving last. He was right about that, and the mechanics are real.

But look at what the case against SpaceX actually was. Four days before it listed, [Steve Eisman told CNBC](https://finance.yahoo.com/markets/stocks/articles/spacex-heads-nasdaq-steve-eisman-194203558.html) he was not a fan, that "the probability of asteroid mining happening anytime soon is pretty low," and that "the entire company is being bet on AI in terms of its future, not on space and not on Starlink." Morningstar put fair value at roughly half the offer. A Danish pension fund excluded the stock outright as grossly overvalued.

That was an argument about whether the business justifying the price existed at all. Anthropic is being criticised for the reverse: the revenue is real, measurable and growing, and the worry is what might happen to it — two customers, fixed commitments. Those are risks to a company that exists. Asteroid mining is not.

The index mechanics are the same in both deals. What is being priced is not.

## What I see from where I sit

A contact inside a card issuer told me the spike in businesses paying Anthropic this year was large enough to set their fraud detection off — thousands of companies starting to pay the same vendor at once looks, to a fraud model, like something has gone wrong. Nothing had. It was demand.

That is the part the bear case has to explain away: not a forecast, not a narrative, but cleared payments.

## Why I think the growth continues

I build software, and what has happened to that work in two years is not an improvement. It is a change of kind.

The last shift of this size was punch cards to high-level languages — roughly twenty years of it. This one arrived inside a couple of release cycles, and it is still moving: coding is one of the areas where the models are visibly getting better, quarter on quarter.

OpenAI is the obvious comparison, and the numbers are less one-sided than the narrative suggests: it went from roughly $25 billion to nearly $70 billion over a comparable stretch, which leaves it ahead in absolute terms. The difference is the slope. Anthropic more than quadrupled in five months from well behind, and the two were level around $30 billion each in April. If that slope holds the lead changes hands; if it does not, the bull case is much weaker than it looks.

Most of the market has not noticed yet, and the spending figures further down make that plain. This is not saturation. It is the very beginning of a curve. And when a tool makes skilled people several times more productive, the vendor eventually gets to price against the value rather than against the competition.

## The risk that actually worries me

It is not the customers. It is Chinese open-weight models.

If something free and self-hosted reaches the frontier on coding, Anthropic's pricing power goes with it, and no customer-concentration analysis matters much after that. Teams there have already shown serious algorithmic efficiency under constraint.

Two things sit in the way.

Training a model at this level means tens of thousands of chips wired together and working as one machine, and a hundred thousand of them is now normal. US export rules keep the best of those chips out of China.

The harder part is that the chips have to talk to each other constantly while they train, and that conversation is the bottleneck. Over three years the models have grown around 240 times bigger and the clusters ten times larger, while the speed at which chips exchange data has only doubled. Chinese teams have become very good at working around this in software. Software can compensate for slower wires, but not forever.

The second thing is language. The dense technical writing these models learn to reason from — research papers, documentation, code — is overwhelmingly in English.

Neither is permanent. Both are why I think the threat is real and slower than it looks.

It is also narrower than it sounds. A model costs much the same to keep running whether one person is using it or a thousand, so a company serving itself pays far more per answer than a provider serving millions. Self-hosting a frontier model is usually worse value than simply buying the tokens. What open weights really enable is a cheap provider undercutting everyone on hosted inference — the [price war Steve Eisman keeps pointing at](https://247wallst.com/investing/2026/08/04/id-be-petrified-steve-eisman-says-cheap-chinese-ai-models-could-wreck-openai-and-anthropics-valuations/) — not your IT department cancelling its subscription.

## The part that argues against me

Honesty requires the other half of that data. In [the same Ramp figures](https://ramp.com/data/ai-index-august-2026), the top 1% of firms spend a median of $7,400 per employee on AI. The median firm spends $11.95. Twelve dollars.

So adoption is real, paid, and extremely narrow. If you think the median company eventually looks like the top 1%, the growth is ahead. If you think the top 1% is what a bubble looks like from inside, Noble's concentration argument is the one that matters. That is the actual disagreement, and it is not settled by either of us asserting it.

## So, is it a buy?

There is a case, and it is not a complicated one. Business revenue went from $14 billion annualised in February to $65 billion in July. Anthropic passed OpenAI on the share of US businesses paying for it. The price of Opus has held across three model generations while the models got substantially better, which is what pricing power looks like from outside — though a planned Sonnet increase was cancelled in September, so the pressure is already there. And the median firm still spends twelve dollars a head, which is a market barely started rather than one running out of room.

Against all that sits China, and I take it seriously rather than as a talking point.

But nobody can answer the question yet, including Noble, because there is no price, no share count and no public filing to read. What we have is a leaked draft, a valuation nobody has confirmed, and two genuinely worrying facts about customer concentration and fixed compute obligations.

When the S-1 is filed publicly I will read the customer concentration disclosure, the compute commitments and the revenue split first. Until then, anyone telling you this is the most dangerous deal of their career — or the opportunity of the decade — is telling you what they already believed, not what they know.
