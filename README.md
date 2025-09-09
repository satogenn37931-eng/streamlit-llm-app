# streamlit-llm-app
#from dotenv import load_dotenv

#load_dotenv()

import os

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# LLMから回答を取得する関数

# OpenAI APIキーの取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")