---
title: Europe didn't buy the hardware
slug: europe-didnt-buy-the-hardware
pubDate: 2026-10-01
summary: I argued before that Europe's innovation gap is about risk and capital rather than regulation. Here is what that bought. Europe holds 5% of the world's AI compute and not one site in the global frontier list.
category: IT
tags:
  - ai
  - europe
  - infrastructure
  - compute
coverImage: ../../assets/posts/ai-build-vs-buy.png
coverAlt: Placeholder — cover concept to be agreed
description: The regulation story does not survive the evidence. Europe built datacentres and did not build AI datacentres, and its flagship answer is 4% of its own forecast.
draft: true
---

<!-- TODO: cover image concept still to be agreed -->

I wrote a while ago that [Europe's innovation gap is a risk problem](/posts/europe-innovation-gap-is-a-risk-problem/) — that regulation is the easy answer, and the real causes are cultural, about appetite for failure and the capital that follows it.

I went looking for what that bought, in physical terms. The answer is sharper than I expected, and it is not the one most people give.

## Europe built datacentres. It did not build AI datacentres.

These are two different numbers and almost everyone conflates them.

On general datacentre capacity Europe is behind but respectable: about 11 GW running against 43 GW in the Americas, and roughly 15% of the world's datacentre electricity consumption. That is the number people quote when they want to say Europe is in the game.

On **AI** compute specifically, the EU holds **5%** of the world total. The United States holds **78%**.

That figure comes from Bruegel. It also comes, independently and by a different method, from Epoch AI and from a US Federal Reserve research note — one measures gigawatts of AI datacentre power, another measures aggregate cluster performance, and they land within a point of each other. When three groups counting different things agree, the number is real.

Epoch maintains a public register of the world's frontier AI datacentres. It lists 93 sites. **Not one of them is in Europe.**

## The scale, stated plainly

JUPITER, in Jülich, is Europe's flagship supercomputer and a genuine engineering achievement. It runs about 24,000 accelerators.

One xAI site in Memphis runs roughly 550,000, and is aiming at 1.2 million by the end of this year.

Europe's entire publicly owned high-performance computing estate is about an order of magnitude smaller than a single American company's single building.

The reason is not mysterious. Amazon, Alphabet, Microsoft and Meta have told their investors they will spend something like **$700 billion of capital this calendar year**. Europe's announced AI infrastructure commitments come to roughly €40 billion, spread across the next two to eight years. Amazon's guidance for one year is about five hundred times what Europe's largest independent cloud provider spends annually.

## The regulation story does not survive the evidence

I believed this one too, so I want to be precise about why it fails.

The Centre for the Governance of AI took 375 large language model releases between 2018 and 2026 and checked which ones reached the EU late or never. About 11% were delayed or withheld. Their conclusion on cause is unambiguous: **no strong evidence that the EU AI Act caused delays or non-releases.** The regulation that did cause them is GDPR, which has been in force since 2018.

Of the fourteen models that have held the top capability position since 2023, exactly one arrived late in Europe, and only in its web app — the programming interface launched at the same time as in America. In the first five months of 2026 there were no delays at all. The report's own closing observation is that American export controls are now a larger barrier to European access than European law.

And the €31 billion compliance cost everyone cites is disputed by the researchers whose analysis it was built on, who said it "grossly exaggerates the cost of the AI Act."

Then there is the arithmetic. American private investment in AI last year was **$285.9 billion**. Europe's was **$20.9 billion**. Even the inflated compliance figure works out at around €6 billion a year against a gap of some $265 billion a year. Regulation cannot carry an explanation that size. Draghi reached the same conclusion in his competitiveness report and put capital markets first.

## The answer Europe has announced is a rounding error

The headline response is the AI Gigafactories, backed by a €200 billion InvestAI programme. Two things about that.

The €200 billion is not new money. The Commission's own announcement says the funding will come from existing EU programmes.

And Bruegel costed the gigafactories against Europe's own forecasts: they come to about **4% of projected EU compute capacity in 2031**, ranking thirty-seventh out of 101 planned European facilities by power draw. Seventy-six of those 101 are being built entirely with private money. The flagship public programme is a rounding error against the private build-out already happening.

The specification has quietly moved, too. In February 2025 each gigafactory was to have "around 100,000 of the latest chips." The tender published last July asks instead that each match Europe's most powerful existing AI factory — which is JUPITER, at 24,000. The call closes next month, awards come in 2027, and the earliest realistic operation is late 2028. The Commission has signed letters of intent with AMD, Nvidia and Qualcomm, so Europe's sovereign compute will run on American silicon by design.

## The two who tried

Aleph Alpha was Germany's national champion. It stopped training frontier models in September 2024 — its founder told Bloomberg that "just having a European LLM is not sufficient as a business model" — lost him as managing director a year later, cut staff in January, and was bought by the Canadian company Cohere in April. The merger completed a fortnight ago.

Silo AI ran the most successful European programme for training models on publicly owned European machines. It was acquired by AMD. Its old blog posts now redirect to amd.com.

Both organisations that trained serious models on European hardware are now inside North American companies.

## The asset that doesn't help

Europe does hold one genuine chokehold. ASML is the only company on earth that makes the extreme ultraviolet lithography machines required to manufacture advanced chips — €32.7 billion of sales last year, and nobody else is close.

Every leading-edge AI chip in the world passes through a machine Europe makes, and Europe has 5% of the compute those chips produce. The strongest card in the European hand is not a card in this game.

## Where I sit in this

I run an IT function in Europe. I build on an American model, through American tooling, on American cloud infrastructure, and I recently wrote a post arguing that buying into one of those American companies looks reasonable.

That is the loop. European money goes into European companies, which spend it on American compute, which funds the next generation of American models, which European companies then pay to use. Every part of that is a rational local decision and the aggregate is a structural transfer.

The regulation argument is comfortable because it implies a fix that costs nothing: repeal something. The compute number implies the opposite, which is why it gets quoted less.
