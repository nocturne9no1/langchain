from langchain_ollama import ChatOllama
from langchain_core.prompts.chat import ChatPromptTemplate

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = ChatOllama(model="llama3:8b", base_url="http://127.0.0.1:11434")

chain = prompt | model

result = chain.invoke({"question": "Why is the sky blue?"})
print(result)