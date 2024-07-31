import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

def create_chain(model_type):
    template = """Question: {question}

Answer: Let's think step by step."""
    prompt = ChatPromptTemplate.from_template(template)

    if model_type == "ollama":
        model = ChatOllama(model="llama3:8b", base_url=os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434"))
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    return prompt | model

async def main():
    os.environ["MODEL_TYPE"] = "ollama"
    chain = create_chain(os.environ.get("MODEL_TYPE"))

    async for text in chain.astream({"question": "Why is the sky blue?"}):
        print(text.content, end="", flush=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())