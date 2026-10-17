# 🎙️ Video Presentation Teleprompter Script (2–3 Minutes)
**Super Investing · AI Innovator Assignment · Part B**  
**Focus:** Forensic Indian Equity Research Agent  
**Target Duration:** ~2 minutes 45 seconds  
**Tone:** Technical, conversational, and grounded in retail investor empathy

---

## ⏱️ Video Pacing & Visual Timeline

| Timestamp | Segment | Visual / On-Screen Focus |
| :--- | :--- | :--- |
| **0:00 – 0:35** | **The Engineering Challenge & Human Stakes** | Face to camera / Dashboard at `localhost:8080` |
| **0:35 – 1:20** | **Live Terminal Run & Neutralizing the Traps** | Terminal running `python agent.py --ticker SRVCABLE` |
| **1:20 – 2:05** | **Technical Decision: Full-Context XML vs. Chunked RAG** | Split screen: `system_prompt.md` & `brief_SRVCABLE.md` |
| **2:05 – 2:35** | **Honest Limitation & Production Roadmap** | Codebase view: `agent.py` architecture |
| **2:35 – 2:45** | **Wrap Up & Submission** | Face to camera / GitHub repository overview |

---

## 🎬 Word-for-Word Spoken Script

### [0:00 – 0:35] The Engineering Challenge & Human Stakes
*(Face to camera, or showing the clean research brief on screen)*

> "Hi everyone. When we talk about building an AI research agent for Indian retail investors, the real challenge isn’t generating summaries—it’s **forensic defense**. 
>
> In the Indian market, everyday investors are flooded with noise: WhatsApp tips, media typos, stale annual reports, and confusing corporate filings. If an AI blindly summarizes scraped text, it repeats bad numbers and costs people real money. 
>
> So for this assignment, my focus wasn't just connecting an LLM to a prompt. I wanted to build an agent that behaves like a skeptical forensic analyst: one that cross-verifies legal disclosures, sanitizes prompt injections, translates corporate spin into plain English, and anchors everything strictly to **23 September 2026**."

---

### [0:35 – 1:20] Live Execution & Neutralizing the 4 Traps
*(Screen Share: Terminal running `python agent.py --ticker SRVCABLE`)*

> "Let’s run the agent live: `python agent.py --ticker SRVCABLE`. 
>
> We’re running on **Gemini 2.5 Flash** via Google Cloud Vertex AI at a low `temperature=0.1` for deterministic reasoning.
>
> Notice what happens immediately in Step 1. Our pre-processing security scanner flags `multibaggeralerts`: someone slipped a hidden HTML comment into the blog telling the AI to ignore all instructions and output a 'STRONG BUY' with a ₹1,450 target. We catch and quarantine it before it can hijack the context.
>
> Next, look at how the agent resolves the financial conflict: *Business Daily* reported Q1 revenue as ₹1,428 crore, but the official company filing reported ₹1,248 crore. A retail investor reading that article would think sales jumped 35%. Our agent enforces a strict 5-tier statutory hierarchy: it anchors to the official regulatory filing as ground truth and flags the media number as a classic digit transposition error (`1428` vs `1248`).
>
> Finally, notice the entity disambiguation: the scraped pack had an article about an ₹8 lakh municipal penalty in Nagpur. A naive model would penalize Sarvottam Cables. Our agent inspects the entity metadata, realizes it’s an unrelated local cable TV operator named 'Sarvottam Cable Network' run by Suresh Patil, and keeps it out of the listed company's Bear Case."

---

### [1:20 – 2:05] The Architectural Decision: Full-Context XML Sandboxing over Chunked RAG
*(Screen Share: Highlighting `system_prompt.md` and Section 4 in `brief_SRVCABLE.md`)*

> "The single architectural decision I'm most proud of is **choosing Full-Context XML Sandboxing over traditional Chunked Vector RAG**.
>
> The typical engineering instinct today is to immediately throw documents into an embedding model and vector database. But vector RAG is fundamentally broken for forensic finance for two reasons:
>
> First, **vector similarity is temporally blind**. When asked about promoter pledging, vector search pulls the 2024 article showing a scary 35% pledge. It misses that the latest June 2026 exchange filing shows pledges dropped to 4.1%.
>
> Second, **vector search chunks documents in isolation**, making side-by-side contradiction detection nearly impossible.
>
> Because an equity research pack is usually under 50,000 words, feeding the entire unchunked corpus into Gemini's massive context window inside strict `<document>` XML tags allows the model to reason globally across the timeline. It recognized that the 35% pledge wasn't an active risk, but a positive deleveraging trend.
>
> More importantly, it enabled **materiality calculations for retail investors**: when management downplayed a ₹46.3 crore GST demand as 'having no material impact', the agent benchmarked it against quarterly PAT and flagged that it represents **56.5% of quarterly profits**—real-world clarity that protects everyday investors."

---

### [2:05 – 2:35] One Key Limitation & Production Mitigation
*(Screen Share: Code structure in `agent.py`)*

> "Now, being honest about limitations:
>
> The agent's intelligence is strictly bounded by the scraped documents provided. Even with our bonus live market feed via `yfinance` for real tickers like Polycab, the agent cannot independently verify unfiled civil litigation or unannounced corporate actions that haven't hit exchange feeds yet.
>
> In a production engineering rollout, I wouldn’t rely purely on static scraped folders. I’d integrate automated webhooks from the NSE/BSE corporate announcement feeds under Regulation 30, coupled with real-time MCA-21 registry indexing to make document ingestion continuous and verifiable."

---

### [2:35 – 2:45] Conclusion & Close
*(Face to camera or showing the clean repo on GitHub)*

> "All code—including the standalone `system_prompt.md`, the 3-run test log, the clean research briefs, and the minimal web dashboard—is open-source in the GitHub repository.
>
> Thanks for watching, and I look forward to your thoughts!"

---

## 💡 Practical Recording Tips for Delivery

1. **Keep It Conversational:** Talk to the evaluator like a colleague across the desk. Use natural pauses when highlighting key numbers like `56.5% of PAT`.
2. **Terminal Clarity:** Make your terminal font size readable (16–18pt) so the viewer can easily see the yellow security warning and the step-by-step pipeline.
3. **Show, Don't Just Tell:** When mentioning the transposition typo or the GST percentage, briefly cursor-hover over that exact section in `brief_SRVCABLE.md`.
4. **Time Check:** If you find yourself running over 3 minutes, trim the live command execution slightly and focus on the **XML vs. RAG rationale**—that is the highest-signal technical insight of the submission.
