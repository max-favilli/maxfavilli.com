# LinkedIn post — AI Stock Analysis Prompts (open source)
# Date: 2026-04-20
# Repo: https://github.com/max-favilli/ai-investing-prompts
#
# Formatting notes:
# - Bold text marked [BOLD]
# - Link goes in FIRST COMMENT
# - Best posting time: Tuesday-Thursday 7-9am CET

## Post body

Nine months ago I built a set of structured prompts to screen stocks using AI. A Buffett-Munger value framework, a behavioral sentiment overlay, batch scoring to CSV. I ran them in parallel on Claude, ChatGPT, and Gemini.

Then I gave up.

The results were inconsistent across models. The same stock, the same prompt, three different conclusions. I could not trust any of them enough to put money behind the output. I never bought a single stock using these prompts.

But the idea still feels right. The prompts encode real investment frameworks — moat analysis, capital allocation scoring, narrative vs. fundamentals separation — into repeatable, scorable checklists. The problem was not the frameworks. The problem was that [BOLD]I could not get the models to apply them reliably[/BOLD].

So I am open-sourcing the whole thing.

The repo includes:
- A Buffett-Munger 6-axis value analysis prompt (scores 0-100)
- A behavioral sentiment analysis prompt (scores 0-100 + Irrationality Index)
- A Claude Code plugin with skills for single-stock analysis and batch screening
- Built-in guardrails: the prompts force the AI to write [NOT VERIFIED] instead of fabricating numbers

[BOLD]What I want to know:[/BOLD]

Has anyone had success using AI to systematically screen stocks? Not "ask ChatGPT what to buy" — I mean structured, repeatable analysis with scoring systems. What worked? What did not? What made the output trustworthy enough to act on?

If you are interested in making these prompts better — testing against real portfolios, adding new frameworks, reducing hallucinations — the repo is open for contributions.

Link in the first comment.

#AI #Investing #OpenSource #ValueInvesting #FinTech

## First comment

Repo: https://github.com/max-favilli/ai-investing-prompts

The prompts work with any AI model (copy-paste). The Claude Code plugin adds slash commands like /buffett AAPL and /screen for batch analysis.

Contributions welcome — especially from anyone who has actually tested AI stock screening against real outcomes.
