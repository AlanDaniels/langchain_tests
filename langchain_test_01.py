#!/usr/bin/env python3

import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv


load_dotenv()
my_key = os.getenv("OPENAI_API_KEY")
if not my_key:
    raise Exception("OpenAI API key not set. Check your setup.")

chat_model = ChatOpenAI(api_key=my_key)
messages = [
    HumanMessage(content='Hello there! Good morning!'),
    HumanMessage(content='For the rest of the conversation, be succinct, but very enthusiastic about the answer.'),
    HumanMessage(content='What is Band of the Hand?')
]

for msg in messages:
    result = chat_model.invoke([msg])
    print(result.content)