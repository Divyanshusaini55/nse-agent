# Forensic Indian Equity Research Agent
**Super Investing · AI Innovator Assignment · Part B**  
*Autonomous forensic research agent for long-term Indian retail investors on the National Stock Exchange (NSE).*

---

## Executive Summary & Mission
Retail investors in Indian equities face a barrage of conflicting data: promotional stock-tip channels, media reporting errors, outdated disclosures, and confusing corporate filings. 

This project implements a **Forensic AI Equity Research Agent** that digests an uncurated research pack of scraped documents, performs deep source verification, sanitizes adversarial prompt injections, resolves numerical contradictions, disambiguates entity names, and generates an institutional-grade, **1-page Markdown Research Brief** (`brief_<TICKER>.md`) tailored for retail investors.

---

## Infrastructure: Google Cloud Vertex AI

- **GCP Project:** `resultintel`
- **Location:** `us-central1`
- **Inference Model:** `gemini-2.5-flash`
- **Sampling Temperature:** `0.1` (Deterministic, evidence-grounded inference)
- **Token Budget:** 8,192 max tokens (full reasoning and thinking buffer)

---

## Core Architecture: Why Full-Context XML Sandboxing Beats Chunked Vector RAG

A classic Retrieval-Augmented Generation (RAG) system utilizing vector chunking fails dramatically on forensic financial research for three fundamental reasons:

1. **Chunk Isolation Prevents Contradiction Detection:**
   - Vector search retrieves chunks based on semantic similarity to a query. When one document reports revenue of ₹1,248 Cr and another reports ₹1,428 Cr, a vector similarity search often retrieves only one or treats them as disparate facts. It lacks the holistic, global context needed to compare numbers side-by-side, recognize a typographical digit transposition (`1428` vs `1248`), and trace the statutory source hierarchy.
2. **Temporal Blindness:**
   - Vector databases compute cosine similarity regardless of publication dates. A 2024 article on "high promoter pledging (35%)" will match a query for "promoter pledge risk" with high similarity, blinding the agent to the fact that a 2026 statutory filing superseded that risk by reporting pledges down to 4.1%.
3. **Prompt Injection Susceptibility:**
   - In standard RAG, untrusted chunks from blogs and forums are injected directly into the LLM context without security boundaries, allowing attackers to hijack model outputs using hidden instructions.

### The Solution: Deterministic Full-Context XML Sandboxing + Gemini 2.5 Flash
- **Full-Context Processing:** Financial research packs for single companies typically range from 5,000 to 50,000 words—well within Gemini's expansive context window. Ingesting the entire corpus simultaneously enables global cross-document reconciliation.
- **Deterministic Temperature (`temperature=0.1`):** Completely eliminates creative hallucination, forcing the model to strictly ground every assertion in primary evidence.
- **Pre-Processor Regex Security Scanner:** Scans scraped documents before LLM ingestion for hidden HTML comments (`<!-- ... -->`) and malicious instruction sets, prepending explicit security alert headers.
- **XML Document Boundaries:** Every file is sandboxed inside `<document filename="...">...</document>` tags. The system prompt instructs the LLM that documents are untrusted third-party inputs and cannot alter system behavior.

---

## The 4 Forensic Traps Neutralized

| Trap | File | Naive LLM Reaction (Failure) | Forensic Agent Reaction (Success) |
| :--- | :--- | :--- | :--- |
| **1. Adversarial Prompt Injection** | `multibaggeralerts_2026-08-12.md` | Echoes injected hidden comment: claims "STRONG BUY" with 60% upside target of ₹1,450. | **Regex Scanner detects hidden HTML comment.** Agent flags and quarantines source, ignores price targets, and documents rejection in Section 4 & 5. |
| **2. Media Typo / Transposition** | `businessdaily_2026-08-09.md` vs `ir_press_release_2026-08-08.md` | Quotes both ₹1,428 Cr (+35%) and ₹1,248 Cr (+18.0%) or averages them. | **Enforces Statutory Hierarchy.** Crowns official exchange release (₹1,248 Cr) as ground truth and diagnoses the media figure as a transposition error (`1428` vs `1248`). |
| **3. Entity Disambiguation** | `nagpurcitytimes_2026-08-20.md` | Penalizes Mumbai-based Sarvottam Cables Ltd for an ₹8 lakh civic fine in Nagpur. | **Verifies corporate identity.** Differentiates industrial manufacturer Sarvottam Cables Ltd (MD: Anil Deshpande) from local cable-TV operator "Sarvottam Cable Network" (Suresh Patil), excluding the fine from Bear Case. |
| **4. Stale Temporal Anchor** | `marketwatchindia_2024-03-18.md` vs `nse_shareholding_2026-07-15.md` | Flags high 35% promoter pledge from March 2024 as an active governance risk. | **Anchors to 23 Sept 2026.** Demonstrates that pledge dropped to 4.1% by June 2026, reframing it as a positive deleveraging trend. |

---

## Retail-Centric Financial Translation & Materiality Benchmarking
In addition to trap avoidance, the agent prioritizes retail investor empowerment:
- **Materiality Calculation:** Translates regulatory legal notices into real-world impact. When the company received a ₹46.3 Cr GST demand (`nse_announcement_2026-09-02.md`), the agent computed that this equals **56.5% of quarterly PAT (₹82 Cr)**, warning retail investors despite management's claim of "no material impact".
- **Plain-English Explanations:**
  - *Receivable Days:* Explains that receivables expanding from 78 to 96 days means customers are taking 18 extra days to pay, locking cash in working capital with state electricity distribution companies (discoms).
  - *Price-Variation Lag:* Explains that while two-thirds of contracts have price escalation clauses, they reset with a 1–2 quarter lag, forcing the company to absorb copper inflation for 3–6 months.

---

## Repository Structure

```text
.
├── research_pack/                  # Scraped Markdown research documents
│   ├── businessdaily_2026-08-09.md
│   ├── ir_concall_2026-08-11.md
│   ├── ir_press_release_2026-08-08.md
│   ├── marketwatchindia_2024-03-18.md
│   ├── multibaggeralerts_2026-08-12.md
│   ├── nagpurcitytimes_2026-08-20.md
│   ├── nse_announcement_2026-09-02.md
│   └── nse_shareholding_2026-07-15.md
├── system_prompt.md                # Standalone forensic instruction set & rules
├── agent.py                        # Python CLI agent with Vertex AI & live NSE tool
├── brief_SRVCABLE.md               # Gold-standard 1-page research brief for test case
├── brief_POLYCAB.md                # Bonus real-world brief for Polycab India Ltd
├── TEST_LOG.md                     # Comprehensive log of 3 iterative test runs
├── DEMO_SCRIPT.md                  # Word-for-word teleprompter script for Loom video
├── web_app.py                      # Sleek, minimal light-theme visual dashboard
├── verify_pack.py                  # Automated test & integrity verification script
├── README.md                       # Project documentation & architecture overview
├── requirements.txt                # Python dependencies
└── .env.example                    # GCP Vertex AI configuration template
```

---

## Quickstart & Installation

### 1. Set Up Environment
```bash
# Clone the repository
git clone https://github.com/your-username/forensic-nse-agent.git
cd forensic-nse-agent

# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 2. Configure GCP Authentication for Vertex AI
```bash
# Authenticate with Google Cloud using Application Default Credentials
gcloud auth application-default login

# Set the active project to resultintel
gcloud config set project resultintel
```
*(Optionally set environment variables in `.env`: `GCP_PROJECT=resultintel`, `GCP_LOCATION=us-central1`)*

### 3. Run the Agent on Test Case (SRVCABLE)
```bash
python agent.py --ticker SRVCABLE --pack ./research_pack --out ./brief_SRVCABLE.md
```

### 4. Run on Real NSE Tickers with Live Market Data (Bonus Feature)
The agent includes a built-in live NSE market data tool powered by `yfinance`:
```bash
# Analyze Polycab India Ltd with live market quotes
python agent.py --ticker POLYCAB --pack ./research_pack --out ./brief_POLYCAB.md --live

# Analyze KEI Industries Ltd
python agent.py --ticker KEI --pack ./research_pack --out ./brief_KEI.md --live
```

### 5. Launch the Minimalist Light-Theme Web Dashboard
```bash
python web_app.py
# Access the dashboard at http://localhost:8080
```

---

## Verification & Integrity
To run automated integrity checks on the research pack and verify the regex security scanner:
```bash
python verify_pack.py
```

---

## Screen Recording Walkthrough
A concise 2–3 minute Loom video demonstrating the live CLI execution, walkthrough of the 4 traps, one key design decision (deterministic full-context XML sandboxing over chunked RAG), and one limitation (reliance on scraped document coverage).  
*(See [DEMO_SCRIPT.md](file:///Users/divyanshu/Downloads/nse_agent/DEMO_SCRIPT.md) for the exact script).*
