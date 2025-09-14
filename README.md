# orbit-ai

**orbit-ai** is a LangGraph-powered personal aide that orbits around your tasks — scraping, searching, and assisting you on the web. Built with modularity in mind, it’s designed to extend beyond web utilities into a versatile AI sidekick.

## ✨ Features

- **Web Scraping & Browsing**: Navigate and extract content from web pages using Playwright.
- **Internet Search**: Query the web with Google Serper and Wikipedia integration.
- **Notifications**: Push real-time updates to your device (via Pushover).
- **File Management**: Read and write files in a controlled sandbox.
- **Python REPL**: Execute and test Python snippets inline.
- **Evaluation Loop**: Smart self-evaluation of responses against success criteria.

## 🚀 Quickstart

Clone the repo:

```bash
git clone https://github.com/pushkqr/orbit-ai
cd orbit-ai
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

Set up environment variables in `.env`:

```
PUSHOVER_TOKEN=your_token
PUSHOVER_USER=your_user
GOOGLE_API_KEY=your_google_api_key
DEBUG=True | False   
```

Run the app:

```bash
uv run app.py
```

Access in browser at [http://localhost:7860](http://localhost:7860).

## 🛠️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://www.langchain.com/)
- [Playwright](https://playwright.dev/)
- [Gradio](https://gradio.app/)
- [Google Serper](https://serper.dev/)
- [Pushover](https://pushover.net/)

## 📂 Project Structure

```
orbit-ai/
├── app.py          # Gradio UI
├── orbit.py        # Core orchestrator (worker/evaluator graph)
├── tools.py        # Tool integrations (browser, search, notifications, etc.)
├── utils.py        # Function wrappers and other utilities
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or file an issue.

