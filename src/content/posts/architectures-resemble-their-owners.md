---
title: Architectures are like dogs — they resemble their owners
slug: architectures-resemble-their-owners
pubDate: 2026-09-29
summary: Conway observed that systems copy the communication structure of the organisation that builds them. The corollary is that when you draw team boundaries, you are choosing an architecture.
category: IT
tags:
  - architecture
  - conwayslaw
  - itleadership
  - teams
coverImage: ../../assets/posts/conway-dog.jpg
coverAlt: Editorial cartoon set in an office. A man stands at a whiteboard drawing a software architecture diagram of boxes and arrows, part of which unmistakably forms the head and pointed ears of a dog. A scruffy dog lies asleep on the floor beneath the board. A second man, seated at the table with a notepad, has turned round in his chair to stare at the real dog with a baffled expression.
thumbImage: ../../assets/posts/conway-dog-thumb.jpg
description: Conway's Law, who actually said it, and why the org chart is an architectural decision you are making whether you intend to or not.
draft: false
---

In April 1968 Melvin Conway published [an article in *Datamation*](https://www.melconway.com/Home/Committees_Paper.html) containing one sentence that has outlived everything else in it:

> Any organization that designs a system... will inevitably produce a design whose structure is a copy of the organization's communication structure.

[Fred Brooks](https://en.wikipedia.org/wiki/Fred_Brooks) quoted it in [*The Mythical Man-Month*](https://en.wikipedia.org/wiki/The_Mythical_Man-Month) and gave it the name it still carries. That is the book I have re-read more than any other in this trade, so I can vouch for it — and [Martin Fowler](https://martinfowler.com/bliki/ConwaysLaw.html) vouches for it too, which counts for considerably more.

So Conway found it and Brooks made it famous, which is why half the industry attributes it to the wrong man.

The observation is usually read as a warning. Three teams will give you three modules, with the seams falling exactly where the meetings didn't happen. Split a team across two time zones and an interface will appear between them, whether or not the domain called for one. You can see it in any system old enough to have survived a reorg: the architecture is a fossil record of who used to talk to whom.

The useful part is the corollary. If structure follows communication whether you intend it or not, then the org chart is an architectural document. [Jonny LeRoy and Matt Simons](https://jonnyleroy.com/2011/02/03/dealing-with-creaky-legacy-platforms/) named this the inverse Conway maneuver in 2010: stop drawing the architecture you want and start drawing the teams that would produce it.

Which is the part that matters if you run an IT function rather than design systems for a living. Nobody asks for your architectural opinion when they restructure a department. But you will get an architecture out of it regardless, and it will resemble the new reporting lines with uncomfortable fidelity — the same way a dog, given enough years, comes to resemble its owner.

Choose the team. The architecture follows.
