# 🏠 Real Estate Assistant - RAG-Based Q&A System

A Retrieval-Augmented Generation (RAG) application that enables users to ask questions about real estate content from web URLs and receive accurate, source-cited answers.

# Demo Link
🌐 -> https://real-estate-assistant-tool.streamlit.app/

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





---

**Built with ❤️ using LangChain and OpenAI**
