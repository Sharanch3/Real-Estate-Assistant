# 🏠 Real Estate Assistant - RAG-Based Q&A System

A Retrieval-Augmented Generation (RAG) application that enables users to ask questions about real estate content from web URLs and receive accurate, source-cited answers.

## 📋 Problem Statement

In the real estate industry, professionals and consumers need to quickly extract specific information from multiple online sources—such as mortgage rates, market trends, policy changes, and property news. Manually reading through numerous articles and websites is time-consuming and inefficient.

**Challenges:**
- **Information Overload**: Real estate news is scattered across multiple websites and articles
- **Time Constraints**: Reading through lengthy articles to find specific data points (e.g., current mortgage rates) is inefficient
- **Source Tracking**: Difficult to remember where specific information came from
- **Context Understanding**: Need to synthesize information from multiple sources to answer complex queries

**Solution:**
This application solves these problems by:
1. Ingesting content from multiple real estate-related URLs
2. Breaking down the content into searchable chunks
3. Storing information in a vector database for semantic search
4. Providing accurate answers with source attribution using AI

## ✨ Features

- **Multi-URL Processing**: Load and process content from up to 3 URLs simultaneously
- **Intelligent Chunking**: Splits documents into optimal chunks for better retrieval
- **Semantic Search**: Uses MMR (Maximal Marginal Relevance) for diverse, relevant results
- **Source Attribution**: Every answer includes citations to original sources
- **Interactive UI**: Clean Streamlit interface for easy interaction
- **Persistent Storage**: Vector store persists between sessions for faster subsequent queries

## 🛠️ Technology Stack

- **LangChain**: Framework for building LLM applications
- **OpenAI GPT-4o-mini**: Language model for generating answers
- **OpenAI Embeddings**: Text embedding model for semantic search
- **Chroma**: Vector database for storing and retrieving document chunks
- **Streamlit**: Web application framework
- **Python 3.8+**: Programming language

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd real-estate-assistant
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install langchain langchain-community langchain-openai langchain-chroma streamlit python-dotenv beautifulsoup4 chromadb
```

4. **Configure environment variables**

Create a `.env` file in the project root:
```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Usage

### Running the Application

**Start the Streamlit app:**
```bash
streamlit run app.py
```

### Using the Application

1. **Enter URLs**: In the sidebar, paste up to 3 real estate-related URLs
2. **Process URLs**: Click the "Process URLs" button to load and index the content
3. **Ask Questions**: Type your question in the text area
4. **Get Answers**: Receive AI-generated answers with source citations

### Example Use Cases
```python
# Example 1: Mortgage rates
"What was the 30-year fixed mortgage rate in December 2024?"

# Example 2: Policy impact
"How does the Federal Reserve's rate policy affect mortgages?"

# Example 3: Market trends
"Why did mortgage rates increase despite the Fed's rate cut?"
```

## 📂 Project Structure
```
real-estate-assistant/
│
├── app.py                 # Streamlit web application
├── rag_utils.py          # Core RAG functionality
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
│
└── resources/
    └── vector_store/    # Chroma vector database (auto-generated)
```

## ⚙️ Configuration

Key parameters in `rag_utils.py`:
```python
MODEL = "gpt-4o-mini"              # OpenAI model
TEMPERATURE = 0.5                   # Response creativity (0-1)
EMBED_MODEL = "text-embedding-3-small"  # Embedding model
CHUNK_SIZE = 300                    # Text chunk size
CHUNK_OVERLAP = 10                  # Overlap between chunks
```

### Retrieval Settings
```python
search_type = "mmr"                 # Maximal Marginal Relevance
k = 3                               # Number of chunks to retrieve
fetch_k = 7                         # Initial fetch size
lambda_mult = 0.5                   # Diversity vs relevance (0-1)
```

## 🔧 Advanced Usage

### Standalone Script

Run the RAG system without the UI:
```bash
python rag_utils.py
```

Modify the `urls` and `query` variables in the `__main__` block to test different sources and questions.

### Custom Integration
```python
from rag_utils import process_urls, generate_answer

# Process URLs
urls = ["https://example.com/article1", "https://example.com/article2"]
for status in process_urls(urls):
    print(status)

# Generate answer
answer, sources = generate_answer("Your question here")
print(f"Answer: {answer}")
print(f"Sources: {sources}")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- **API Costs**: This application uses OpenAI's API which incurs costs. Monitor your usage.
- **Rate Limits**: Be mindful of OpenAI API rate limits
- **Data Privacy**: URLs are processed and stored locally. Ensure compliance with data privacy regulations.
- **Content Limitations**: Works best with well-structured HTML content. Some websites may block web scraping.

## 🐛 Troubleshooting

**Issue: "VectorDB is not initialized"**
- Solution: Click "Process URLs" before asking questions

**Issue: Import errors**
- Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue: OpenAI API errors**
- Solution: Verify your API key in the `.env` file and check your account credits

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Built with ❤️ using LangChain and OpenAI**