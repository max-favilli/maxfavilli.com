---
title: "Examples"
slug: examples
order: 8
description: "Real-world examples illustrating the techniques from this guide."
---

Real-world examples illustrating the techniques from these docs. All from the same project: integrating a new scripting engine (Elwood) into an existing enterprise integration platform (Eagle).

## 1. Design session into coding session

**Illustrates:** [Session discipline](/guide/session-discipline/) — the two kinds of session.

I needed to add support for a new file type in a large, complex codebase. The change touched configuration loading, a core data transformation pipeline, dependency injection across four service hosts, and a bridge between two JSON libraries.

I did not start by asking the agent to code anything. I started a **design session** with one goal: produce documents.

The session went in two steps. First, I gave the agent a rough description of what I wanted — informal, not structured — and asked it to write a clean request document. The agent produced a 148-line structured spec (`elwood-integration-request.md`) that broke the work into two explicit phases: investigate and plan (Phase 1, no code), then implement (Phase 2, only after approval). It included non-goals, deliverables, and a detection rule for the new file type. I reviewed and refined it.

Then I told the agent to proceed with Phase 1. It explored the codebase, read the relevant docs, and produced a 338-line plan (`elwood-integration-plan.md`) containing: investigation findings, a proposed architecture with interface definitions, a file-by-file change list, an envelope-mapping table, error handling design, DI registration plan, and seven open questions it could not resolve without my input.

I answered the seven questions. Only then did the coding session begin.

**Why this mattered:** every decision and finding was captured in files on disk. If the session had compacted, or if I had switched to a different agent, the work would survive. The coding session started with a complete, reviewed plan — no re-exploration needed, no ambiguity about what to build.

The two documents took maybe 30 minutes of my time (mostly reviewing). They saved hours of the kind of back-and-forth where you realize mid-implementation that the agent misunderstood the architecture.

## 2. Explore before edit catches a wrong assumption

**Illustrates:** [Context engineering](/guide/prompting-and-context/) — technique 1, bidirectional learning.

In the same project, I had assumptions about how Eagle worked. Some were wrong.

I told the agent that the source-context information was "carried as something like a `SourceInfo` object, and/or a field on a `PayloadParseResult`." I was not sure of the details and said so. Instead of guessing and coding, the agent explored the codebase.

What it found:

- **There is no `SourceInfo` class.** What I was thinking of is a `JObject` — untyped JSON — populated from database stored procedures and metadata blobs. The name `SourceInfo` exists only as a property name on `PullPayloadResult`, not as a type.
- **Maps are stored in SQL, not on the filesystem.** I had not said otherwise explicitly, but the way I described the flow ("Eagle reads map files") implied files on disk. The agent found they are loaded from a `ConfigurationFiles` table, column `configurationContent`.
- **The core Parse method embeds context inline into the input data** (`$.payload.sourceInfo`, `$.payload.eventId`, etc.) — it is not passed as a separate parameter. This had significant design implications for how to bridge to the new scripting engine.
- **`EagleMap.Parse` throws `NotImplementedException` on failure** — a technical debt item I did not know about, which the agent flagged as "not ideal — worth addressing during this work."
- **A 27-day-old agent memory was wrong.** A previous session had recorded the file extension as `.elwood.yaml`, but investigation confirmed it should be `.elwood` for script files.
- **Only five call sites** for the Parse method — fewer than I expected. This lowered the complexity estimate from what I feared.

Every one of these discoveries changed the design. If the agent had skipped exploration and started coding based on my initial description, it would have built something that did not match the actual codebase. The explore phase cost a few minutes. It prevented hours of rework.

The dialogue was bidirectional. The agent learned how Eagle actually works. I learned things about my own codebase I had forgotten or never knew. We arrived at a shared understanding that was more accurate than either of us had alone.

## 3. Red-green loop on a greenfield feature

**Illustrates:** [Spec-driven coding](/guide/spec-driven-coding/) — the full spec-driven workflow.

*Awaiting a real example. To be added.*

## 4. Doom loop into fresh agent reset

**Illustrates:** [The mental model](/guide/mental-model/) — points 3 and 4 (doom loop and fresh eyes).

*Awaiting a real example. To be added.*

## 5. Non-goals saving the day

**Illustrates:** [Context engineering](/guide/prompting-and-context/) — technique 4.

In the Eagle/Elwood integration, the request document included an explicit non-goals section:

> - No changes to the structure of `RootConfiguration` beyond what is strictly required.
> - No migration of existing `.json` maps to `.elwood`.
> - No changes to the Elwood project itself — Eagle is a *consumer* of Elwood here.
> - No performance work on top of the baseline integration.

When the agent produced its plan, it respected every one of these. Without the non-goals, the agent would likely have proposed restructuring `RootConfiguration` to make the new file type a first-class concept, added a migration path for existing maps, and possibly suggested changes to Elwood itself. All of that would have ballooned the scope from a medium-complexity change to a multi-week project.

The non-goals also cascaded into the open questions. When the agent asked "should this new format be supported in `Output.Mapfile`, `Source.Metadata`, `Soap.Body`, and other configuration fields?" — the answer was "start with `Source.Configuration` only, defer the rest to a subsequent phase." That single scoping decision cut the number of affected code paths roughly in half.

**The pattern:** non-goals are not just guardrails for the agent. They are a forcing function for you to make scoping decisions *before* implementation, when they are cheap. Without the non-goals section, I would have had to make these same decisions mid-coding, one by one, as the agent proposed each expansion. That is a slower and more error-prone way to scope.

## 6. Shabby request with rich context beats a precise request

**Illustrates:** [Context engineering](/guide/prompting-and-context/) — the bedrock claim.

My original prompt to the agent was rough. Here it is, lightly edited:

> I need to evaluate and plan the complexity of a change, and eventually implement it. In `IntermediateDataModel.cs` there's a number of methods named Parse, they all take as input an EagleMap, those maps are used to transform an input document into a json output. EagleMap contains a file which in Eagle is referred by name in a RootConfiguration... I want to make Eagle support a new file type... you need to understand how Eagle works...

Not a polished request. Grammatically rough. Vague in places ("a number of methods," "something else"). But it carried **rich context**: specific file paths, the relationship between configuration and map files, how the processing pipeline works, what Elwood is, where its docs live, and what the desired end state is.

The agent turned this into a structured, 148-line request document with clear sections, a detection rule, explicit non-goals, and a two-phase work breakdown. Then it turned that into a 338-line plan with interface definitions, an envelope-mapping table, and a file-by-file change list.

**The counterpoint:** imagine a carefully worded prompt — "Please implement a strategy pattern to abstract the map-file parsing in `IntermediateDataModel.cs`, supporting both JSON and a new script format" — but with no file paths, no explanation of the processing pipeline, no context about what Elwood is, no mention of `PullPayloadResult` or the envelope. The agent would produce something generic and architecturally plausible but disconnected from how Eagle actually works.

The shabby request with rich context produced a plan tailored to the real codebase. A precise request with thin context would have produced a textbook answer to the wrong problem.

## 7. Cross-tool handoff

**Illustrates:** [Session discipline](/guide/session-discipline/) — cross-tool portability.

*Awaiting a real example. To be added.*
