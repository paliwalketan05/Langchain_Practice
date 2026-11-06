from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model ="openai/gpt-oss-120b")

messages=[
    SystemMessage(content='You are a Good Assistant '),
    HumanMessage(content='What is the capital of Indonesia')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)