 🛡️ AI-Powered API Security Agent CLI

An automated command-line tool designed to audit OpenAPI specifications for security vulnerabilities before deployment. By pairing static spec parsing with AI risk analysis via OpenRouter, the agent automatically identifies unauthenticated or misconfigured endpoints and outputs detailed security reports.

---

 🎯 Key Features & Value

* **Shift-Left Security:** Catches missing authentication and potential security oversights at the specification stage before code goes live.
* **Automated AI Risk Evaluation:** Leverages LLM intelligence to analyze route paths, methods, parameters, and authentication statuses for context-aware risk reasoning.
* **Rich Terminal Interface:** Displays scan findings in a clear, formatted terminal table using `rich`.
* **Exportable Audit Reports:** Generates structured JSON reports (`report.json`) for audit compliance and integration into security pipelines.

---

 🏗️ How It Works

1. **Parser (`parser.py`):** Reads OpenAPI (JSON/YAML) files and extracts endpoints into structured models (`RouteEndpoint`).
2. **Analyzer (`analyzer.py`):** Evaluates endpoint parameters and authentication status against an AI model on OpenRouter.
3. **CLI Interface (`main.py`):** Coordinates parsing, AI analysis, terminal rendering, and file export via `typer`.

---

🚀 Quickstart Guide

 1. Prerequisites
Ensure you have Python 3.9+ installed and your virtual environment activated:

```powershell
.\venv\Scripts\activate