# 🤖 RAG-based Chatbot with FastAPI 

This project is a Retrieval-Augmented Generation (RAG) based chatbot, built with FastAPI as the backend framework. The chatbot uses a hybrid approach combining retrieval-based and generation-based techniques to provide users with more accurate and contextually relevant responses. The application leverages document embeddings and vector stores to retrieve relevant context from documents, enhancing response quality when answering queries.

## 📨 Introduction to RAG in NLP 

**Retrieval-Augmented Generation (RAG)** is an advanced Natural Language Processing (NLP) approach that improves the quality of generated responses by combining a retrieval mechanism with a generative model. Instead of relying solely on pre-trained knowledge, RAG retrieves relevant documents or context from a vector store based on the user's input, then augments the response generation. This method makes RAG particularly useful for applications where up-to-date or domain-specific knowledge is required.

## 📝 Project Description 

This is primarily a backend project done in `Python` using `FASTAPI`. It also has a fronend chatbot for visualization written in `Vanilla JS` for easy sampling in any modern frontend framework. `Jinja2` templating was used and the frontend is served statically from the *static* folder. The *test* folder contains unit and integration tests for easy testing and automation.

## 📂 Project Structure 
├── main.py             # Main application entry point
├── rag_service.py      # RAG handler and services
├── rag_util.py         # Utility functions for document processing
├── static/             # Static files (CSS, JS, etc.)
├── templates/          # HTML templates
├── test/               # Unit and integration tests
├── Dockerfile          # Docker setup file
├── .env                # Environment variables file
└── README.md           # Project documentation

## 🤖 Introducing Christiana Rolando!!! 

**Christiana Roland** is a chatbot 💬 that provides you information based on the documents provided in the `data` folder. You can add any document of your choice. However, note that you may encounter some limitations in running for larger files depending on the models and API key you use. In this repo, I used a pdf (footballrule.pdf) that contains footbal/soccer rules. Therefore, Christiana's scope is football rules. You can change the pdf to any one of your choosing to change the subject.

## 📌 Limitations!!! 

* There is a limit to the file size that can be added to the models used. After many trials and errors I discovered that the document you add to the data folder shouldn't be too big, shouldn't contain too many images or else the `token limit` will be exceeded.

* Christiana can be forgetful: When the model gives an obscure answer you may need to type in "Try again" to have it give a better answer.
  
* For this RAG, I included a document that contains football rules. In the backend I had to limit the amount of text parsed from the document as this too had a limit. You can adjust the length of document parsed in the *MAX_DOC_LENGTH* variable in the `rag_util.py` file or choose to dynamically set this.

## ➡️ To do!!!
* As is the case with NLP and AI in general, a lot of feature engineering and parameter tuning is needed for use cases. You can experiment further with this if you want to use it in your own application.

## 🔥 Features
- 🧠 **LLM/NLP Processing** for intelligent responses.
- 🚀 **WebSocket support** for real-time query responses.
- ⚡ **HTTP API** for traditional request-response handling.
- 📄 **Document embedding and retrieval** using a custom vector store.
- 🌍 **Environment-based configuration** for easy local and production setup.

## Prerequisites

- 🐍 Python 3.10+
- 🐋 [Docker](https://www.docker.com/) (if you want to run using Docker)
- 📡 A `.env` file with necessary configurations. See [Environment Variables](#environment-variables) below.

## 🌍 Environment Variables

Make sure to create a `.env` file in the project root with the following variables:

```
GROQ_API_KEY=<Your_GROQ_API_Key>
APP_BASE_URL=http://127.0.0.1:
WEBSOCKET_URL=ws://127.0.0.1:8000
```

## How to Run Locally 🖥️
* 👥 Clone the repository
  * `git clone https://github.com/oyinoye/rag-chatbot.git`
  * `cd rag-chatbot`
  
* 🌐 Set up a virtual environment:
  * `python -m venv venv`
  * `source venv/bin/activate`  # On Windows: venv\Scripts\activate
  
* 🛠️ Install the dependencies:
  * `pip install -r requirements.txt`

* 💥 Start the application:
  * `uvicorn main:app --host 0.0.0.0 --port 8000`

* 🏁 Access the application:
  * Open http://127.0.0.1:8000/docs in your browser for the API documentation.
  * Open http://127.0.0.1:8000 in your browser to interact with Christiana Rolando.


## How to Run using Docker 🐳
You can use docker for easy setup.

* Build the Docker image:
  * `docker build -t rag-chatbot .`
  
* Run the Docker container:
  * `docker run -p 8000:8000 --env-file .env rag-chatbot`

* 🏁 Access the application:
  * Open http://127.0.0.1:8000/docs in your browser for the API documentation.
  * Open http://127.0.0.1:8000 in your browser to interact with Christiana Rolando.


## Startup Commands 💻
*** Running the API (FastAPI) with Uvicorn  ***
  🚀 To run the FastAPI application using Uvicorn, execute:
  * `uvicorn main:app`
  
*** WebSocket Setup ***
  🔄  Make sure your frontend is configured to connect to the WebSocket endpoint:
  * ```const websocketUrl = `${window.location.protocol === "https:" ? "wss://" : "ws://"}${window.location.host}/ws/query`:```
  
*** Testing *** 
  🔬 Unit Tests (for Python functions, services, and controllers):
  * `pytest test/`
  🧪 Selenium Tests (for frontend and WebSocket integration):
  * `python -m unittest test/test_selenium.py`
  ✅ All Tests: 
  * `pytest`
  
## Contributing 🤝
* Feel free to open issues or submit pull requests for new features, improvements, or bug fixes.
  
  
## Licensing 📄
* This project is licensed under the MIT License.

## HAVE FUN!
