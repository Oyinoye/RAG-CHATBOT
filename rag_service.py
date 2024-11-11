from swarmauri.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
from swarmauri.messages.concrete import SystemMessage
from swarmauri.agents.concrete.RagAgent import RagAgent
from rag_util import initialize_llm, initialize_vector_store, load_documents_from_folder, get_allowed_models

# Folder path containing PDFs
FOLDER_PATH = "./data"

# Initialize LLM
llm = initialize_llm()
allowed_models = get_allowed_models(llm)
print("Allowed Models:", allowed_models)

# Load documents and initialize vector store
documents = load_documents_from_folder(FOLDER_PATH)
vector_store = initialize_vector_store(documents)

# Set up RAG agent
rag_system_context = "Use the information below to answer user questions."
rag_conversation = MaxSystemContextConversation(system_context=SystemMessage(content=rag_system_context), max_size=2)

rag_agent = RagAgent(
    llm=llm,
    conversation=rag_conversation,
    system_context=rag_system_context,
    vector_store=vector_store,
)

def handle_query(query: str):
    response = rag_agent.exec(query)
    # Handle cases where an empty string is returned from the agent.
    if response == "":
        response = "I'm sorry. I seem to be unable to answer this at the moment. You may ask me to try again."
    return response
