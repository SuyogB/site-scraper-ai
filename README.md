# Site Scraper AI

## Description
Site Scraper AI is an application that uses web crawling, text processing, and a large language model (LLM) for intelligent question-answering based on crawled website content. The application automatically scrapes a website, extracts its markdown content, and converts it into embeddings for efficient similarity search using FAISS. Users can ask questions, and the AI provides answers strictly based on the content available in the scraped website.

## Features
- **Web Crawling:** Automatically scrape websites and extract content using Crawl4AI.
- **Data Processing:** Convert the scraped markdown content into text chunks for efficient processing.
- **Embedding and Vector Search:** Use GoogleGenerativeAIEmbeddings for generating vector representations, with FAISS for fast similarity-based search.
- **Conversational Interface:** Use a prompt template to guide an AI assistant in answering questions strictly based on the crawled content.
- **Streamlit UI:** A simple user interface for interacting with the AI, allowing users to ask questions and receive relevant responses.

## Requirements
- Python 3.8+
- Google API Key (for accessing Google Generative AI)
- Streamlit
- LangChain
- FAISS
- Crawl4AI

## Installation

### 1. Clone the repository: 
   ```bash
   git clone https://github.com/your-username/site-scraper-ai.git
   cd site-scraper-ai
   ```
### 2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### 3. Set up your .env file:

Create a .env file in the root of the project and add your Google API key:
GOOGLE_API_KEY=your-google-api-key

## File Descriptions

app.py: Main application file. It initializes the Streamlit app, processes the crawled content, and handles user interaction.
crawl_deloitte.py: This script uses Crawl4AI to scrape the specified website and extract the content in markdown format.
requirements.txt: Contains all the necessary dependencies for the project.

## Running the Application

### 1. S Scraping the Website:
Run the crawl_deloitte.py file to scrape the website content.
   ```bash
   python crawl_deloitte.py
   ```
This will scrape the content of the specified website (https://www2.deloitte.com/us/en/insights/economy/asia-pacific/india-economic-outlook.html) and store it in the crawler_output.txt file in markdown format.

### 2. Run the Streamlit App:
Once the scraping is complete, run the Streamlit app using the following command:

 ```bash
   streamlit run app.py
   ```
### 3. Interact with the Assistant:

The assistant will ask you to input questions about the scraped content.
Type your questions in the input box, and the assistant will retrieve relevant answers based on the scraped website data.

### 4. Clear Chat History:

Click on the "Clear Chat History" button to reset the conversation.

## How It Works

Web Crawling (via crawl_deloitte.py): This file crawls the specified website, extracts its content, and stores it in a markdown format.
Text Ingestion (via app.py): The scraped markdown content is loaded into the application and split into smaller chunks.
Embeddings and Vector Search (via FAISS): The text chunks are converted into vector embeddings using Google's Generative AI API, and indexed using FAISS for efficient retrieval.
Conversational Assistant: The user can ask questions about the website, and the assistant responds based on the information stored in the FAISS index.

## Notes

You need an internet connection to run the app and use the Google API for embeddings.
Ensure the .env file is properly set up before running the app.

## Future Enhancements

### Dynamic URL Input: 
The app will allow users to input any URL to scrape, making it more flexible.

### Local LLM Integration: 
Integration of local language models for more private and efficient querying.

### Image Extraction:
Extracting and integrating images from the website for more detailed insights.





