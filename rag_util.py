import os
import fitz
from dotenv import load_dotenv
from swarmauri.documents.concrete.Document import Document
from swarmauri.vector_stores.concrete.TfidfVectorStore import TfidfVectorStore
from swarmauri.llms.concrete.GroqModel import GroqModel

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MAX_DOC_LENGTH = 2000


def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text[:MAX_DOC_LENGTH]


def load_documents_from_folder(folder_path):
    """Function to load pdf files from folder"""
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            content = extract_text_from_pdf(file_path)
            documents.append(Document(content=content))
    return documents


def initialize_vector_store(documents):
    """Function to initialize vector store and add documents to it"""
    vector_store = TfidfVectorStore()
    vector_store.add_documents(documents)
    return vector_store


def initialize_llm():
    if API_KEY:
        return GroqModel(api_key=API_KEY)
    else:
        raise ValueError("API Key not found! Check your .env file.")


def get_allowed_models(llm):
    failing_llms = [
        "llama3-70b-8192",
        "llama3.2-90b-text-preview",
        "mixtral-8x7b-32768",
        "llava-v1.5-7b-4096-preview",
        "llama-guard-3-8b"
    ]
    return [model for model in llm.allowed_models if model not in failing_llms]
