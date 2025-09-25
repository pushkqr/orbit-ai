# orbit-ai

**orbit-ai** is a LangGraph-powered personal aide that orbits around your tasks — scraping, searching, and assisting you on the web. Built with modularity in mind, it’s designed to extend beyond web utilities into a versatile AI sidekick.

## ✨ Features

* **Web Scraping & Browsing**: Navigate and extract content from web pages using Playwright.
* **Internet Search**: Query the web with Google Serper and Wikipedia integration.
* **Notifications**: Push real-time updates to your device (via Pushover).
* **File Management**: Read and write files in a controlled sandbox.
* **Python REPL**: Execute and test Python snippets inline.
* **Markdown to PDF**: Convert Markdown (.md) files to PDF.
* **Evaluation Loop**: Smart self-evaluation of responses against success criteria.

## 🚀 Quickstart

Clone the repo:

```bash
git clone https://github.com/pushkqr/orbit-ai
cd orbit-ai
```

Create and activate a virtual environment:

```bash
uv venv
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
uv run playwright install
```

Set up environment variables in `.env`:

```
PUSHOVER_TOKEN=your_token
PUSHOVER_USER=your_user
GOOGLE_API_KEY=your_google_api_key
DEBUG=True | False
SERPER_API_KEY=your_serper_api_key
SMTP_EMAIL=your_email_address
SMTP_PASSWORD=your_app_password
SMTP_SERVER=your_smtp_server_url
```

Run the app:

```bash
uv run app.py
```

Access the UI in your browser at [http://localhost:7860](http://localhost:7860).

## 🛠️ Tech Stack

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain](https://www.langchain.com/)
* [Playwright](https://playwright.dev/)
* [Gradio](https://gradio.app/)
* [Google Serper](https://serper.dev/)
* [Pushover](https://pushover.net)

## 📂 Project Structure

```
orbit-ai/
├── app.py          # Gradio UI
├── orbit.py        # Core orchestrator (worker/evaluator graph)
├── tools.py        # Tool integrations (browser, search, notifications, etc.)
├── utils.py        # Function wrappers and other utilities
├── pyproject.toml
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or file an issue.
