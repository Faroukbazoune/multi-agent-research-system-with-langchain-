# Multi-Agent Research System with LangChain 🧠

A powerful AI-driven research system that leverages multiple agents and LLMs to conduct comprehensive web research, content extraction, and generate well-structured reports with critical analysis.

## 📋 Overview

This system combines multiple AI agents working together to:
- **Search** the web using Tavily API for relevant information
- **Scrape** and extract content from web pages
- **Analyze** gathered research data
- **Generate** structured, thoughtful reports
- **Critique** reports for quality assurance

The application features a modern Streamlit-based UI called "AI Research Studio" for an intuitive research experience.

## ✨ Key Features

- **Multi-Agent Architecture**: Specialized agents for searching, scraping, writing, and critiquing
- **Advanced LLM Integration**: Uses Google Gemini and Groq models for optimal performance
- **Intelligent Web Search**: Powered by Tavily API for accurate, relevant results
- **Web Content Extraction**: Sophisticated scraping with multiple fallback strategies
- **Structured Report Generation**: Automatically formatted reports with insights and sources
- **Critical Analysis**: AI-powered report evaluation and quality rating
- **Beautiful UI**: Streamlit-based interface with modern dark theme and responsive design

## 🛠️ Tech Stack

- **Framework**: LangChain, LangChain Community, LangChain Google GenAI
- **LLMs**: Google Gemini 3.7, Groq Qwen 2.7B
- **Web Tools**: Tavily API, BeautifulSoup, Trafilatura, Readability
- **Frontend**: Streamlit
- **Language**: Python 3.13

## 📦 Dependencies

```
langchain
langchain_core
langchain-groq
langchain_community
langchain_google_genai
streamlit
tavily_python
beautifulsoup4
requests
lxml
trafilatura
readability-lxml
python-dotenv
rich
```

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd multi-agent-research-system-with-langchain-
```

### 2. Create Virtual Environment
```bash
python -m venv langAgent
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.\langAgent\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.\langAgent\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source langAgent/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory with your API keys:
```env
TAVILY_API_KEY=your_tavily_api_key_here
GOOGLE_API_KEY=your_google_genai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

## 📂 Project Structure

```
multi-agent-research-system-with-langchain-/
├── app.py                 # Streamlit application entry point
├── main.py               # Command-line entry point for testing
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
├── .env                 # Environment variables (create this)
├── langAgent/           # Virtual environment directory
└── src/                 # Source code directory
    ├── __init__.py
    ├── agents/          # AI agents implementation
    │   ├── __init__.py
    │   └── agents.py    # Search, scraping, writer, and critic agents
    ├── tools/           # External tools and utilities
    │   ├── __init__.py
    │   └── tools.py     # Tavily search and web scraping functions
    └── pipelines/       # Research pipeline orchestration
        ├── __init__.py
        └── pipelines.py # Main search pipeline
```

## 💻 Usage

### Running the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Command-Line Interface

```bash
python main.py
```

This will execute a sample research pipeline searching for "cristiano ronaldo"

### Running the Search Pipeline Programmatically

```python
from src.pipelines.pipelines import run_search_pipeline

# Run research on a specific topic
results = run_search_pipeline("your research topic")
```

## 🤖 Agent Descriptions

### Search Agent
- **Role**: Expert web researcher
- **Tool**: Tavily Search API
- **Capability**: Searches the internet for relevant information
- **Output**: Top 5 results with titles, URLs, and snippets

### Scraping Agent
- **Role**: Web content extraction specialist
- **Tool**: Web Scraper (Trafilatura + BeautifulSoup + Readability)
- **Capability**: Extracts detailed content from web pages
- **Output**: Cleaned, text-only content (up to 5000 characters)

### Writer Agent
- **Role**: Research report author
- **Model**: Google Gemini 3.7
- **Capability**: Synthesizes research into structured reports
- **Output Format**:
  - Introduction
  - Key Insights (3 detailed points)
  - Conclusion
  - Sources (with URLs)

### Critic Agent
- **Role**: Report quality evaluator
- **Model**: Google Gemini 3.7
- **Capability**: Analyzes and critiques generated reports
- **Output**:
  - Rating (out of 10)
  - Weak points
  - Strong points
  - One-line verdict

## 🔑 API Keys Required

1. **Tavily API Key**: Get from [tavily.com](https://tavily.com)
   - Used for web search functionality
   
2. **Google GenAI API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Used for Gemini model access
   
3. **Groq API Key**: Get from [Groq Console](https://console.groq.com)
   - Used for Qwen model access (optional, for enhanced processing)

## 📝 Example Workflow

1. User enters a research topic in the Streamlit UI
2. Search Agent queries the web using Tavily API
3. Scraping Agent extracts detailed content from top results
4. Writer Agent creates a structured report from the gathered data
5. Critic Agent evaluates the report quality
6. Results are displayed in the UI

## 🎨 UI Features

- **Dark Modern Theme**: Eye-friendly dark background with gradient elements
- **Wide Layout**: Optimized for large screen viewing
- **Responsive Design**: Adapts to different screen sizes
- **Interactive Elements**: Real-time research execution with feedback

## 🔧 Customization

### Changing LLM Models
Edit `src/agents/agents.py` to modify the models:
```python
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", temperature=0.0)
groq_model = ChatGroq(model_name="qwen/qwen3.6-27b")
```

### Adjusting Search Results
Modify the `max_results` parameter in `src/tools/tools.py`:
```python
response = taviliy_client.search(query=query, max_results=10)  # Change from 5
```

### Customizing Report Format
Edit the prompt templates in `src/agents/agents.py` for the writer and critic agents.

## 📋 Requirements

- Python 3.13+
- Active internet connection for web search and content extraction
- Valid API keys for Tavily, Google GenAI, and Groq

## 📄 License

See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Note**: Ensure all API keys are kept secure and never commit `.env` files to version control.