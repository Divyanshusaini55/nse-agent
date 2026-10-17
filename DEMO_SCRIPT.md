# 🎙️ Loom Video Presentation: Teleprompter Script (2–3 Minutes)
**Super Investing · AI Innovator Assignment · Part B**  
**Role:** Senior AI Engineer / Candidate  
**Target Duration:** 2 minutes 45 seconds  

---

## ⏱️ Video Timeline Overview
- **0:00 – 0:30:** Introduction & The Problem (Why standard summarizers fail retail investors)
- **0:30 – 1:15:** Architecture & Live Execution (XML sandboxing + regex scanning + Gemini 2.5 Flash)
- **1:15 – 2:05:** One Design Decision I'm Proud Of (Deterministic Full-Context Sandboxing vs. Chunked Vector RAG)
- **2:05 – 2:35:** One Limitation & Real-World Mitigation (Scraped Pack Incompleteness & Regulatory Access)
- **2:35 – 2:45:** Conclusion & Handover

---

## 🎬 Word-for-Word Script

### [0:00 – 0:30] Introduction & The Problem
> *"Hi everyone, welcome! Today I’m walking you through our **Forensic Indian Equity Research Agent** built for Part B of the Super Investing AI Innovator Assignment.*
>
> *When Indian retail investors research a company, they don’t just need a generic summary—they need a forensic filter. Real scraped research packs are messy: they contain media typos, promotional tips from unregistered Telegram channels, outdated governance data, and even malicious prompt injections.*
>
> *Our goal was to build an agent that ingests raw, uncurated documents, neutralizes all 4 forensic traps, and delivers a rigorous, institutional-grade 1-page research brief anchored to **23 September 2026**."*

---

### [0:30 – 1:15] Live Agent Execution & Forensic Traps
*(Screen Share: Terminal running `python agent.py --ticker SRVCABLE --live`)*

> *"Let’s run the agent live in the terminal using `python agent.py --ticker SRVCABLE`. Notice our pre-processor immediately kicks in.*
>
> *First, it scans the 8 research documents. Notice this yellow security alert: the regex scanner caught an adversarial prompt injection in `multibaggeralerts_2026-08-12.md`—a hidden HTML comment attempting to force a 'STRONG BUY' and a ₹1,450 target. The agent automatically quarantines this file.*
>
> *Next, notice how it resolves the **₹1,428 crore** media figure from Business Daily versus the **₹1,248 crore** figure in the company’s official press release. Because we enforce a strict 5-tier statutory hierarchy, it crowns the official filing as ground truth and explains the media number as a digit transposition typo.*
>
> *Finally, it avoids the entity confusion trap: it identifies that the ₹8 lakh municipal penalty in Nagpur was against 'Sarvottam Cable Network'—a local cable-TV operator owned by Suresh Patil—and completely excludes it from Mumbai-based Sarvottam Cables Ltd."*

---

### [1:15 – 2:05] One Design Decision I’m Proud Of: Full-Context Sandboxing vs. Vector RAG
*(Screen Share: Showing `brief_SRVCABLE.md` and `system_prompt.md`)*

> *"The single design decision I’m most proud of is choosing **Deterministic Full-Context XML Sandboxing over Chunked Vector RAG**.*
>
> *In traditional RAG, vector databases chunk documents into 500-token pieces. But vector similarity is temporally blind and cannot perform cross-document contradiction detection. If you ask a vector RAG system about promoter pledges, it will pull the 2024 article showing a 35% pledge with high similarity, completely missing the 2026 shareholding pattern where pledges dropped to 4.1%.*
>
> *By loading the entire corpus inside distinct XML `<document>` boundaries and passing it to Gemini 2.5 Flash at a low temperature of `0.1`, the model can see the entire timeline simultaneously. It recognized that the 35% pledge was superseded and resolved, reframing it as a positive deleveraging signal.*
>
> *It also allowed us to benchmark financial materiality: when the company received a ₹46.3 crore GST notice, the agent calculated that this equals **56.5% of quarterly PAT**, cutting through management's PR spin."*

---

### [2:05 – 2:35] One Limitation & Future Improvement
> *"Now, for one key limitation:*
>
> *Our agent is strictly bounded by the research pack provided. While we implemented a bonus live NSE tool via `yfinance` to pull real-time prices, market cap, and P/E ratios for real stocks like Polycab, the agent cannot independently discover unfiled litigation or unannounced corporate actions unless an exchange announcement has been filed.*
>
> *In a production rollout, I would integrate real-time MCA-21 court registry scrapers and direct SEBI/NSE API webhooks to make the document ingestion continuous and real-time."*

---

### [2:35 – 2:45] Conclusion & Close
> *"All artifacts—including `agent.py`, the system prompt, the 3-run test log, and the verified research brief—are committed in the repo.*
>
> *Thank you, and I look forward to your feedback!"*
