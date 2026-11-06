import os
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b:groq",
    task="text-generation",
    max_new_tokens=100
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capotal of America")
print(result.content)
