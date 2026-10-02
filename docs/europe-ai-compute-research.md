# Europe's AI position — verified research notes

<!-- RESEARCH NOTES, not the post. Three agents, 30 Sept 2026. Several widely-repeated
     claims were REFUTED — see the bottom section before reusing anything. -->

## Compute (the core finding)

- EU **2.07 GW** of AI compute = **5%** of world. US **35.28 GW** = **78%**. China 4.95 GW = 11%.
  Bruegel Policy Brief 18/2026 — https://www.bruegel.org/policy-brief/how-can-europe-address-its-pressing-ai-compute-infrastructure-shortfall
- Corroborated independently, different metrics, same answer:
  US Federal Reserve FEDS Note (Oct 2025): US 74%, China 14%, **EU 4.8%** — https://www.federalreserve.gov/econres/notes/feds-notes/the-state-of-ai-competition-in-advanced-economies-20251006.html
  Epoch AI: US ~75% of global AI supercomputer performance — https://epoch.ai/blog/trends-in-ai-supercomputers
- **General** datacentre capacity, by contrast: Americas 43.4 GW operational vs EMEA 11.4 GW; pipeline 191.3 GW vs 12.1 GW (Cushman & Wakefield, May 2026) — https://www.cushmanwakefield.com/en/germany/news/2026/05/global-data-center-market-comparison
- Datacentre electricity: US 45%, China 25%, **Europe 15%** (IEA) — https://www.iea.org/reports/energy-and-ai/executive-summary
- **Epoch's Frontier Data Centers Hub tracks 93 sites. No European site appears.** Top five all US: xAI Colossus 2 (1,112k H100-eq), Microsoft Fairwater Atlanta (769k), Amazon/Anthropic New Carlisle (686k), Google Pryor North (637k), Meta Prometheus (600k) — https://epoch.ai/data/ai-data-centers
- JUPITER (Jülich), Europe's flagship: **~24,000 GH200**. xAI Memphis: ~550,000 GPUs, targeting 1.21M by end-2026.
- Hyperscaler 2026 guided capex: Amazon ~$200bn, Alphabet $195–205bn, Microsoft ~$175bn, Meta $130–145bn ≈ **$700–725bn in one year**, vs ~€40bn of European pledges over 2–8 years.

## Europe's own answer

- **AI Gigafactories = ~4% of projected EU 2031 compute**, 37th of 101 planned EU facilities ≥10 MW by power. 76 of the 101 are fully privately financed (Bruegel).
- Feb 2025 InvestAI promised "around 100,000 chips" per gigafactory. The **July 2026 tender made it relative** — match Europe's most powerful AI factory (JUPITER, ~24k), with 3× at phase 2. Call closes 12 Nov 2026, awards early 2027, operation **late 2028 at earliest**. Commission signed letters of intent with **AMD, Nvidia and Qualcomm** — American silicon by design.
  https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_26_1708/IP_26_1708_EN.pdf
- **The €200bn InvestAI headline is not new money.** Commission's own release: funding "will come from existing EU funding programmes."
  https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_25_467/IP_25_467_EN.pdf
- Cloud: non-EU hyperscalers **~72%** of the EU market; European providers fell **27% (2017) → 13% (2022)** (European Commission study, Aug 2026). Largest European players ~2% each (SAP, Deutsche Telekom).

## Capital

- European pension funds allocate **0.009%** of assets to venture; US **0.028%**. Matching would unlock **~$210bn** over a decade (Atomico, State of European Tech 2025).
- VC mandates issued 2025: US pensions **$9.25bn**, European pensions **$485m** — 19× (S&P Global, Mar 2026).
- Europe invests **12× less at late stage**: $12bn vs $141bn (Dealroom).
- US private AI investment 2025 **$285.9bn** vs Europe **$20.9bn** (Stanford HAI AI Index 2026).
- Mistral's €3bn (Sept 2026) is Europe's largest-ever AI round = **2.4%** of OpenAI's $122bn round. Mistral total raised ~$6.5bn; Anthropic raised 10× that in one round four months earlier.

## The regulation story does not survive

- **GovAI, 375 LLM releases, June 2026**: "We find no strong evidence of other regulations, including the EU AI Act, causing delays or non-releases." The main regulatory barrier is **GDPR**. Of 14 models that held the top capability spot since 2023, **one** was delayed to the EU. **Zero** delays in the first five months of 2026. Their conclusion: US export controls may now be the bigger barrier.
  https://govai.b-cdn.net/Delays_to_Frontier_AI_in_the_EU_and_UK.pdf
- The €31bn compliance figure (CDI/ITIF 2021) is **disputed by the authors of the study it derives from** — CEPS: it "grossly exaggerates the cost of the AI Act." https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/
- Arithmetic: even €6bn/yr against a ~$265bn/yr investment gap cannot carry the explanation.
- Draghi's report puts capital markets first, regulation as compounding not causal.

## Who tried, and where they are now

- **Aleph Alpha** quit frontier training Sept 2024 (Andrulis: "Just having a European LLM is not sufficient as a business model"), founder left Oct 2025, ~50 layoffs Jan 2026, **acquired by Cohere (Canada)** April 2026, merger completed 16 Sept 2026.
- **Silo AI**, which ran Europe's most successful EuroHPC model programme (Poro, Viking on LUMI), **acquired by AMD** — old blog URLs now redirect to amd.com.
- **Apertus 70B** (Swiss AI Initiative, 4,096 GH200 on Alps, 15T tokens, Sept 2025) is the real counterexample — European-owned iron, but a generation behind, and Switzerland is not in the EU.
- Mistral's disclosed compute: CoreWeave, Scaleway, Nvidia DGX Cloud, EuroHPC Leonardo (7B only). The Feb 2024 Azure partnership was announced and **never substantiated** — no Mistral model attributed to Azure in 2.5 years.
- Google DeepMind trains on Google TPUs. Europe's most capable lab is a US subsidiary on US custom silicon.

## ASML

- **Only company producing EUV systems.** 2025 net sales €32.667bn, 48 EUV systems recognised, net income €9.609bn. 2026 guidance raised to €43–45bn.
- But the stack is multinational: Zeiss (DE) optics, Cymer (San Diego, ASML subsidiary) light source, AGC/Hoya (JP) mask blanks. "The Netherlands holds a monopoly" overstates it.
- Analytical point: Europe's one genuine chokehold delivers Europe zero compute.

## Models — the claim that failed hardest

- Artificial Analysis (30 Sept 2026): Claude Opus 5.5 **58**, GPT-6 **53**, Meta Muse Spark **48**, GLM-5.2 (CN) **34**, **Mistral Medium 3.5 14, Mistral Large 3 9**.
- Arena leaderboard: **no European model in the top 100.** Mistral Medium #112, Large 3 #138.
- Open-weight: Chinese leaders GLM-5.3 45, Kimi K3 44. Best American open 26. Mistral absent from the discussion.
- Devstral: Mistral self-reports 72.2% SWE-bench Verified; **official standardised board gives 53.8%** — beaten by Claude 4.5 Haiku.
- Likely origin of the "world-class" claim: AA's "#6 out of 65 models in its class" — a size-class ranking mistaken for a global one.

## REFUTED — do not reuse

1. "Training a frontier model costs $100M–$1B+." Epoch's highest costed run is **Grok 4 at ~$490M**. $1B+ is their **2027 projection**.
2. "US rounds routinely hit $6–10B." Badly understated: OpenAI **$122bn**, Anthropic **$65bn**, xAI **$20bn**.
3. "€500M–€1B is a historic outlier in Europe." Six European $1bn+ rounds closed in 2025–26.
4. "Mistral Large and Devstral rank among the world's most capable." See above. A year out of date.
5. "Brain drain to the US." **Reversed.** Revelio Labs: "For the first time... more AI workers are moving from the US to Europe than the reverse" — driven by US policy friction (the $100k H-1B fee), not European pull. https://www.interface-eu.org/publications/talent-in-talent-out
6. Aleph Alpha as a going concern. It is inside Cohere.
7. Pay gap of 5–10×. WTW (May 2026) medians: US >$170k, Germany ~$122k, UK just under $100k — **1.4× and 1.7×**.
