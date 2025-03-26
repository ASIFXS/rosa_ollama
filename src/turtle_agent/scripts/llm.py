import dotenv
from langchain_ollama import ChatOllama

def get_llm(streaming: bool = False):
    """A helper function to get the Ollama LLM instance."""
    dotenv.load_dotenv(dotenv.find_dotenv())  # Kept if other parts of your app use dotenv
    
    return ChatOllama(
        model="llama3.1:8b",  # Replace with your preferred model
        temperature=0,
        num_ctx=8192,          # Adjust based on the model's context window
        streaming=streaming    # Preserve streaming functionality if needed
    )