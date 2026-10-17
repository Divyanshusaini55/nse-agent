#!/usr/bin/env python3
"""
Forensic Equity Research Dashboard (Sleek, Minimal, Light Theme)
Super Investing · AI Innovator Assignment · Part B

Focused entirely on the Research Brief with zero unnecessary clutter.
"""

import os
import sys
import re
import json
import subprocess
import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super Investing · Forensic Research Brief</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-page: #f8fafc;
            --bg-surface: #ffffff;
            --border: #e2e8f0;
            --border-hover: #cbd5e1;
            --text-main: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --accent: #0f172a;
            --accent-hover: #1e293b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-main);
            line-height: 1.6;
            font-size: 15px;
            -webkit-font-smoothing: antialiased;
            padding-bottom: 80px;
        }

        /* Top Bar */
        header {
            background-color: var(--bg-surface);
            border-bottom: 1px solid var(--border);
            padding: 16px 40px;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-content {
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .brand-title {
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: var(--text-main);
        }

        .brand-subtitle {
            font-size: 0.88rem;
            font-weight: 400;
            color: var(--text-muted);
            margin-left: 10px;
        }

        .header-meta {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: var(--text-muted);
            background: #f1f5f9;
            padding: 4px 10px;
            border-radius: 4px;
            border: 1px solid var(--border);
        }

        /* Main Container */
        .container {
            max-width: 900px;
            margin: 32px auto 0 auto;
            padding: 0 20px;
        }

        /* Controls */
        .control-strip {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }

        .control-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .select-ticker {
            background-color: var(--bg-surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            font-weight: 500;
            padding: 7px 14px;
            border-radius: 4px;
            outline: none;
            cursor: pointer;
            transition: border-color 0.15s ease;
        }

        .select-ticker:hover, .select-ticker:focus {
            border-color: var(--border-hover);
        }

        .btn-run {
            background-color: var(--accent);
            color: #ffffff;
            border: 1px solid var(--accent);
            font-family: 'Inter', sans-serif;
            font-size: 0.82rem;
            font-weight: 600;
            padding: 7px 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.15s ease;
        }

        .btn-run:hover {
            background-color: var(--accent-hover);
        }

        .btn-run:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        .btn-copy {
            background-color: var(--bg-surface);
            color: var(--text-secondary);
            border: 1px solid var(--border);
            font-family: 'Inter', sans-serif;
            font-size: 0.82rem;
            font-weight: 500;
            padding: 7px 14px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .btn-copy:hover {
            background-color: #f1f5f9;
            color: var(--text-main);
        }

        /* Research Brief Document Card */
        .brief-paper {
            background-color: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 44px 50px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
        }

        .doc-body h1 {
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 6px;
            letter-spacing: -0.02em;
        }

        .doc-meta {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-bottom: 22px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border);
        }

        .doc-body h2 {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 28px;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 1px solid var(--border);
            letter-spacing: -0.01em;
        }

        .doc-body p {
            color: var(--text-secondary);
            margin-bottom: 12px;
            font-size: 0.94rem;
            line-height: 1.65;
        }

        .doc-body ul, .doc-body ol {
            padding-left: 20px;
            margin-bottom: 14px;
        }

        .doc-body li {
            color: var(--text-secondary);
            margin-bottom: 10px;
            font-size: 0.94rem;
            line-height: 1.6;
        }

        .doc-body strong {
            color: var(--text-main);
            font-weight: 600;
        }

        .citation-tag {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 600;
            background: #eff6ff;
            color: #1d4ed8;
            border: 1px solid #dbeafe;
            padding: 1px 5px;
            border-radius: 3px;
            margin: 0 1px;
            display: inline-block;
            vertical-align: baseline;
            letter-spacing: -0.01em;
        }

        .doc-body ol {
            padding-left: 20px;
            margin-bottom: 14px;
        }

        .doc-body ol li {
            color: var(--text-secondary);
            margin-bottom: 8px;
            font-size: 0.92rem;
            line-height: 1.6;
        }

        /* Loading / Toast Status */
        #status-bar {
            display: none;
            background: #0f172a;
            color: #ffffff;
            font-size: 0.82rem;
            padding: 9px 16px;
            border-radius: 4px;
            position: fixed;
            bottom: 24px;
            right: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
            z-index: 999;
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <div>
                <span class="brand-title">Super Investing</span>
                <span class="brand-subtitle">/ Forensic Equity Research</span>
            </div>
            <div class="header-meta">
                ANCHOR: 23 SEPT 2026
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Control Bar -->
        <div class="control-strip">
            <div class="control-left">
                <select id="ticker-select" class="select-ticker" onchange="handleTickerChange()">
                    <option value="SRVCABLE" selected>SRVCABLE (Sarvottam Cables Ltd)</option>
                    <option value="POLYCAB">POLYCAB (Polycab India Ltd)</option>
                </select>
                <button id="btn-run" class="btn-run" onclick="triggerAgentRun()">Generate Brief</button>
            </div>
            <div>
                <button class="btn-copy" onclick="copyBriefText()">Copy Markdown</button>
            </div>
        </div>

        <!-- Document View -->
        <div class="brief-paper">
            <div id="brief-container" class="doc-body">
                __BRIEF_CONTENT_HTML__
            </div>
        </div>
    </div>

    <div id="status-bar"></div>

    <script>
        function showStatus(text, duration = 3000) {
            const bar = document.getElementById('status-bar');
            bar.innerText = text;
            bar.style.display = 'block';
            if (duration > 0) {
                setTimeout(() => { bar.style.display = 'none'; }, duration);
            }
        }

        function copyBriefText() {
            const container = document.getElementById('brief-container');
            navigator.clipboard.writeText(container.innerText);
            showStatus('Brief copied to clipboard');
        }

        function handleTickerChange() {
            const ticker = document.getElementById('ticker-select').value;
            window.location.href = '/?ticker=' + ticker;
        }

        function triggerAgentRun() {
            const ticker = document.getElementById('ticker-select').value;
            const btn = document.getElementById('btn-run');
            btn.disabled = true;
            btn.innerText = 'Analyzing...';
            showStatus('Generating forensic research brief via Vertex AI...', 0);

            fetch('/api/run?ticker=' + ticker)
                .then(r => r.json())
                .then(data => {
                    btn.disabled = false;
                    btn.innerText = 'Generate Brief';
                    if (data.status === 'ok') {
                        showStatus('Research brief generated successfully');
                        setTimeout(() => { window.location.reload(); }, 600);
                    } else {
                        showStatus('Error: ' + data.error);
                    }
                })
                .catch(err => {
                    btn.disabled = false;
                    btn.innerText = 'Generate Brief';
                    showStatus('Network error: ' + err);
                });
        }
    </script>
</body>
</html>
"""


def format_inline(text: str) -> str:
    """Format inline markdown elements: citations, bold, and italics."""
    filename_map = {
        "ir_press_release_2026-08-08": "1",
        "businessdaily_2026-08-09": "2",
        "ir_concall_2026-08-11": "3",
        "nse_shareholding_2026-07-15": "4",
        "nse_announcement_2026-09-02": "5",
        "marketwatchindia_2024-03-18": "6",
        "multibaggeralerts_2026-08-12": "7",
        "nagpurcitytimes_2026-08-20": "8"
    }

    # 1. Clean up any legacy .md filenames: map to clean source numbers
    for fn, num in filename_map.items():
        text = text.replace(f"[{fn}.md]", f"[{num}]")
        text = text.replace(f"[{fn}]", f"[{num}]")
    
    # Clean any remaining .md filename extensions inside brackets
    text = re.sub(r'\[([a-zA-Z0-9_\-]+)\.md\]', r'[\1]', text)

    # 2. Style clean numbered citations: [1], [2], [1, 3], etc.
    text = re.sub(r'\[(\d+(?:,\s*\d+)*)\]', r'<span class="citation-tag">[\1]</span>', text)

    # 3. Bold formatting
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

    # 4. Italics formatting
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)

    return text


def convert_markdown_to_clean_html(md: str) -> str:
    """Format markdown into clean typographic HTML with sleek citations and zero .md clutter."""
    lines = md.split("\n")
    out = []
    in_ul = False
    in_ol = False

    for line in lines:
        s = line.strip()

        # Headings and structure
        if s.startswith("# "):
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            out.append(f"<h1>{format_inline(s[2:])}</h1>")
        elif s.startswith("## "):
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            out.append(f"<h2>{format_inline(s[3:])}</h2>")
        elif s.startswith("### "):
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            out.append(f"<h3>{format_inline(s[4:])}</h3>")
        elif s.startswith("*   ") or s.startswith("- ") or s.startswith("* "):
            if in_ol: out.append("</ol>"); in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            content = re.sub(r'^(\*\s+|- |\*\s{3})', '', s)
            out.append(f"<li>{format_inline(content)}</li>")
        elif re.match(r'^\d+\.\s+', s):
            if in_ul: out.append("</ul>"); in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            content = re.sub(r'^\d+\.\s+', '', s)
            out.append(f"<li>{format_inline(content)}</li>")
        elif s.startswith("---"):
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            out.append("<hr style='border:0;border-top:1px solid #e2e8f0;margin:20px 0;'>")
        elif s:
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            if s.startswith("**As of:**"):
                out.append(f"<div class='doc-meta'>{format_inline(s)}</div>")
            else:
                out.append(f"<p>{format_inline(s)}</p>")

    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")

    return "\n".join(out)


class MinimalDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        # API endpoint to execute agent.py via Vertex AI
        if parsed.path == "/api/run":
            query = parse_qs(parsed.query)
            ticker = query.get("ticker", ["SRVCABLE"])[0]
            try:
                venv_py = os.path.join(BASE_DIR, ".venv", "bin", "python3")
                python_bin = venv_py if os.path.isfile(venv_py) else sys.executable
                cmd = [
                    python_bin,
                    os.path.join(BASE_DIR, "agent.py"),
                    "--ticker", ticker,
                    "--project", os.environ.get("GCP_PROJECT", "resultintel"),
                    "--location", os.environ.get("GCP_LOCATION", "us-central1")
                ]
                if ticker != "SRVCABLE":
                    cmd.append("--live")
                res = subprocess.run(cmd, capture_output=True, text=True, check=True)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "output": res.stdout}).encode("utf-8"))
            except subprocess.CalledProcessError as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "error": e.stderr}).encode("utf-8"))
            return

        # Main HTML rendering
        if parsed.path in ["/", "/index.html"]:
            query = parse_qs(parsed.query)
            selected_ticker = query.get("ticker", ["SRVCABLE"])[0]

            if selected_ticker == "POLYCAB":
                brief_file = os.path.join(BASE_DIR, "brief_POLYCAB.md")
            else:
                brief_file = os.path.join(BASE_DIR, "brief_SRVCABLE.md")

            brief_md = ""
            if os.path.exists(brief_file):
                with open(brief_file, "r", encoding="utf-8") as f:
                    brief_md = f.read()

            brief_html = convert_markdown_to_clean_html(brief_md)
            final_html = HTML_TEMPLATE.replace("__BRIEF_CONTENT_HTML__", brief_html)

            if selected_ticker == "POLYCAB":
                final_html = final_html.replace('value="SRVCABLE" selected', 'value="SRVCABLE"')
                final_html = final_html.replace('value="POLYCAB"', 'value="POLYCAB" selected')

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(final_html.encode("utf-8"))
        else:
            super().do_GET()


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


def main():
    print(f"Launching Minimalist Research Dashboard on http://localhost:{PORT}")
    server_address = ("", PORT)
    httpd = ThreadingHTTPServer(server_address, MinimalDashboardHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")


if __name__ == "__main__":
    main()
