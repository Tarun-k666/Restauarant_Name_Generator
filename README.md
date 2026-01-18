# Restaurant Name Generator

🍴 A GenAI-powered app that creates restaurant names and customized menus using local LLMs with LangChain orchestration and Streamlit UI.

## Features

- **Cuisine Selection**: Choose from Indian, Chinese, Mexican, Italian, Arabic, or American cuisine
- **AI-Powered Names**: Generate unique, fancy restaurant names using Ollama LLama 3.2 model
- **Dynamic Menus**: Automatically generate 8 relevant menu items for each restaurant
- **User-Friendly Interface**: Clean, intuitive Streamlit interface with sidebar controls

## Tech Stack

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **Language Model**: Ollama (Llama 3.2)
- **Python Version**: 3.11+

## Prerequisites

- Python 3.11 or higher
- Ollama installed and running locally on `http://localhost:11434`
- Llama 3.2 model pulled in Ollama

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Ollama is running with Llama 3.2 model:
   ```bash
   ollama run llama3.2
   ```

## Usage

Run the application with Streamlit:
```bash
streamlit run main.py
```

The app will open in your browser. Use the sidebar to select a cuisine, and the app will:
1. Generate a fancy restaurant name
2. Create 8 menu items specific to that restaurant

## Project Structure

- `main.py` - Streamlit frontend application
- `langchain_helper.py` - LangChain orchestration and LLM integration
- `pyproject.toml` - Project configuration and dependencies