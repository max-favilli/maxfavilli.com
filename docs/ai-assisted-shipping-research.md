# What one part-time director shipped in 10 days with a coding agent — research notes

<!-- RESEARCH NOTES — not the final post. Written by the Eagle session on 2026-09-16 at Max's request,
     from measurements taken in that session. Numbers are reproducible with the commands below. -->

## The claim to build on

Max Favilli — Director of IT (Senior Manager IT DevOps), coding in a fraction of his working time,
not full time — shipped **~16,000 lines across six repositories in the 10 days to 2026-09-16**,
working with a coding agent (Claude Code) in long-running sessions.

Classic industry benchmarks put a full-time professional developer at roughly 10–50 *delivered* lines
per day, i.e. **~100–500 lines in 10 working days**. The gap is more than an order of magnitude — and
that is before accounting for the part-time constraint.

## The measurement

Commits authored by Max on the main branch (or the pushed working branch where the repo has no main
yet), merges excluded, `package-lock.json` excluded. Window: 2026-09-06 → 2026-09-16.

| repo | what it is | commits | lines added | lines removed |
|---|---|---|---|---|
| Eagle | integration platform (C#/.NET, Azure) — the day job | 61 | 11,787 | 1,455 |
| hr-wolfpack | myWolfpack intranet PoC (Next.js + WordPress), on `develop` | 7 | 3,390 | 260 |
| shopify-hr-jobs | Shopify app | 1 | 313 | 37 |
| shopify-redirects | Shopify app | 5 | 305 | 50 |
| claude-training | internal training material | 2 | 86 | 10 |
| maxfavilli.com | this blog | 3 | 75 | 20 |
| **total** | | **79** | **15,956** | **1,832** |

Eagle's 11,787 added lines split as: **docs +7,328 · C# source +3,394 · tests +647 · pipelines +258 ·
other +160**. 44 of the 79 commits carry a `Co-Authored-By: Claude` trailer.

Excluded on purpose: 29,347 lines of `package-lock.json` in hr-wolfpack (generated). Two other repos
(Elwood, EagleFrontend) had no commits in the window.

Reproduce (per repo):

```
git log --since="10 days ago" --author="Favilli" --no-merges --numstat --pretty=tformat: origin/main \
  | awk 'NF==3 && $1!="-" && $3 !~ /package-lock\.json$/ {a+=$1; d+=$2} END {print a, d}'
```

## What "shipped" meant in Eagle (not just lines)

The lines went to production, not to a branch. In the same 10 days the Eagle work included, all
merged and deployed through the normal approval-gated pipeline:

- a replay/automated-testing capability for the integration platform (new `ReplayService`, run/corpus/
  JUnit endpoints, a third "test lane" of Azure apps, a pipeline stage that runs a corpus of real past
  events against new code);
- a production two-lane cutover runbook and its execution;
- several root-caused production defects (an end-of-processing marker silent for weeks, a stored
  procedure shipped after the code that needed it, a dead notification failing green deploys);
- five retired Azure Function Apps and two stale Event Grid subscriptions deleted after verification;
- stored-procedure changes applied to DEV/QA/PROD;
- three Jira tickets opened and closed with root causes written up.

The **docs share (62% of Eagle's added lines)** is not padding: it is changelog entries per PR, a
runbook, plans, a retrospective on the agent's own mistakes, and an "Eagle internals" reference the
agent is required to read and correct. Code that ships to a regulated production system needs that
writing; a solo developer rarely produces it.

## The benchmarks — and where they come from

Stated from training data, not freshly searched; the sources are old and there is no good current
equivalent. Verify before quoting hard numbers.

- Brooks, *The Mythical Man-Month* (1975): ~10 delivered lines/day for systems software, all phases
  included.
- McConnell, *Code Complete* (2nd ed., 2004): roughly 10–50 delivered lines/day industry-wide on large
  projects; small projects run higher.
- COCOMO-era data lands in the same band: a few hundred to ~1,000 lines per developer-month.

Those figures count *delivered production code over the whole lifecycle* — design, test, debugging,
documentation time all divided into the line count. Ten working days → ~100–500 lines.

## How to frame it honestly (the tension with the existing draft)

The site already has a draft — `measuring-ai-productivity-wrong.md` — whose thesis is that **lines,
PRs and tickets are effort proxies and the wrong metric**. A post that headlines "I shipped 16k lines"
contradicts it unless it says why the number is being used:

1. **It is a scale signal, not a productivity metric.** The point is not 16k vs 300; it is that a
   part-time IT director produced the *volume of a small team*, with production deployments, tests and
   documentation attached. The order-of-magnitude gap is what makes the effort-based benchmarks
   obsolete — the same argument the earlier post makes from the outside, now from the inside.
2. **Say what the lines are.** 62% documentation, 21% source, 4% tests. A skeptic will assume
   generated boilerplate; the breakdown answers that before it is asked.
3. **Say what they cost.** The same 10 days produced a retrospective of the agent's own mistakes
   (wrong claims verified and retracted, a false "205 tests passed", a PR raised against the wrong
   branch). The volume came with a review burden, and the developer's job became reading, challenging
   and verifying. That is the honest version of "part-time".
4. **Do not claim a ratio.** "50× a senior developer" is not supportable: the benchmarks measure
   full lifecycles of human typing on other kinds of systems. Quote the raw numbers and the
   benchmarks side by side and let the reader do the arithmetic.

## What the Eagle session cannot vouch for

- Hours actually spent coding in the window — Max's own estimate is needed ("a fraction of my time").
- Whether the six repos are the complete set (the count covers local clones under
  `C:\GitAzureDevOpsRepos`; Azure DevOps was checked only for the hr-wolfpack project, which has one repo).
- Lines are as counted by `git numstat`; renames and reformatting inflate them like everywhere else.
