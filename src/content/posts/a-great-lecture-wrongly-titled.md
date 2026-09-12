---
title: A great lecture, wrongly titled
slug: a-great-lecture-wrongly-titled
pubDate: 2026-09-09
summary: I watched a Stanford lecture called "Prompting Is Dead in 6 Months." Nobody in it says that. Half of what I remembered wasn't in it either. The lecture itself explains why — and it's worth your time.
category: AI
tags:
  - ai
  - softwareengineering
  - andrewng
  - accuracy
  - careers
coverImage: ../../assets/posts/ai-build-vs-buy.png
coverAlt: Editorial cartoon of a lecture hall where the speaker's projected slide shows a plain graph, while a giant flashy marquee over the stage announces a completely different, more dramatic title, and the audience photographs the marquee instead of the slide.
description: A Stanford lecture circulating under a fabricated title, a chart I remembered that was never shown — and the real argument underneath, properly credited.
draft: true
---

<!-- TODO: replace placeholder cover image -->

I recently watched a Stanford lecture on YouTube titled "Prompting Is Dead in 6 Months. Andrew Ng, Stanford." I found it true and inspiring, and I wanted to write about it. So I pulled the transcript to get the quotes right.

Nobody in the lecture says prompting is dead. Not once, not in any wording. The title is the re-uploader's invention. And Andrew Ng speaks for sixteen minutes of the hundred and three; the rest is Lawrence Moroney — the former Google AI lead who taught half the world TensorFlow, now at ARM. Most of what impressed me came from a man whose name isn't in the title.

It gets worse. I remembered Ng showing a chart about AI coding capability doubling every few months. I asked for it from the transcript. There is no chart, and no doubling claim. My memory had stitched a famous result from elsewhere into a lecture that never mentioned it.

Moroney, in the part of the lecture nobody credits him for, explains exactly what happened to me: "The currency of social media is engagement. Accuracy is not the currency." I'm a careful reader with thirty years in this industry, and the packaging still wrote itself into my memory. That's the mechanism, demonstrated on the person writing this post.

So here is the lecture, accurately.

## What Ng actually says

Two things worth anchoring.

"AI coding made building software much cheaper and faster — but that ironically shifts the bottleneck to deciding what to build." He sees the engineer-to-PM ratio, traditionally four or eight to one, trending toward two to one — in some teams one to one. When a clear spec becomes working code almost for free, writing the clear spec is the job.

"The cost of failure is much lower than before: you waste a weekend but learn something." His advice to students is simply to build — the number of ideas in the world exceeds the number of people who can build them, and the price of finding out is now a weekend.

(Both quotes lightly cleaned from the auto-captions; the substance is his.)

## The doubling that is real

The chart I misremembered exists — it just belongs to [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), not this lecture. Their measurement: the length of tasks AI agents can complete autonomously with 50% reliability, measured by how long they take human professionals, has been doubling roughly every seven months for six years. Extrapolated, systems handle week-long human tasks within a decade. Extrapolations deserve skepticism, but this is a measured six-year trend, not a demo. It's the quantified version of what Ng describes qualitatively: his favorite coding tool changes every three to six months, and being half a generation behind means being noticeably less productive.

## What Moroney actually says

The unbilled 87 minutes hold the most useful material. Generated code makes skilled engineers more valuable, not less: "Code is cheap now. Finished code, engineered code is not cheap." The worst technical debt is delivering code nobody understands. An AI bubble is likely coming — there is always a bubble — and, as after the dot-com crash, the companies built on fundamentals will thrive on the other side of it.

Watch the lecture. Just know what you're watching: not Ng declaring prompting dead, but two people making a quieter argument — the constraint has moved from writing code to knowing what to build and finishing it properly. The fake title got you to click. The accuracy is the part worth keeping.
