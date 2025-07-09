# 🕸️ Web Content Summarizer & X Post Generator

This project is a Python script that automates the process of extracting the **main content** from any webpage, **summarizes** it using a local LLM, and **generates a short, engaging social media post** for X (formerly Twitter). It utilizes **locally hosted models via [Ollama](https://ollama.com)** and the **OpenAI Python SDK**.

---

## 🚀 Features

- 🧠 Extracts the **core readable content** from a website (skipping headers, footers, nav, scripts, etc.)
- 📄 Summarizes the extracted content into **clear and concise bullet points**
- ✍️ Generates **engaging X (Twitter) posts** from the summary
- 💻 Works **completely offline** with **locally hosted models** (no OpenAI API key needed)

---

## ⚙️ Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- The following models as used or any that suits you installed via Ollama:
  - `gemma3:4b`
  - `qwen3:4b`
  - `gemma3:4b-it-qat` *(or any similar instruction-tuned model)*

---

## 📦 Installation

1. **Clone the repo or copy the script.**

2. **Install dependencies:**

```bash
pip install openai requests
---

## 🏃‍♂️ Usage

Run the script from your terminal, passing the target URL as an argument:

```bash
python <script_name>.py
```

Replace `<script_name>` with the actual script filename if different. The script will output a summary and a suggested X post based on the webpage content.

