import os
import pytest
from rag_util import extract_text_from_pdf, load_documents_from_folder, initialize_vector_store, initialize_llm

# Mock environment variable for API key
os.environ["GROQ_API_KEY"] = "dummy_api_key"

def test_extract_text_from_pdf():
    text = extract_text_from_pdf("./data/footballrule.pdf")
    assert isinstance(text, str)
    assert len(text) <= 2000  # Ensure text is limited to MAX_DOC_LENGTH

def test_load_documents_from_folder():
    documents = load_documents_from_folder("data")
    assert isinstance(documents, list)
    assert all(doc.content for doc in documents)

def test_initialize_vector_store():
    documents = load_documents_from_folder("data")
    vector_store = initialize_vector_store(documents)
    assert vector_store is not None
    assert hasattr(vector_store, "add_documents")

def test_initialize_llm():
    llm = initialize_llm()
    assert llm is not None
    assert isinstance(llm.api_key, str)
