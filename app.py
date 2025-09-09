from dotenv import load_dotenv

load_dotenv()


import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# LLMから回答を取得する関数

# OpenAI APIキーの取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_llm_response(user_input: str, expert_type: str) -> str:
    # 専門家の種類に応じてシステムメッセージを変更
    if expert_type == "UFC":
        system_prompt = "あなたはUFC（アメリカ最大の総合格闘技団体）の領域の専門家です。ユーザーの質問に専門的な知識をもとに答えてください。"
    elif expert_type == "RIZIN":
        system_prompt = "あなたはRIZIN（日本最大の総合格闘技のフェデレーション）の領域の専門家です。ユーザーの質問に専門的な知識をもとに答えてください。"
    else:
        system_prompt = "あなたは様々な分野に詳しい専門家です。"

    # LLM呼び出し（OpenAI API例）
    chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = chat(messages)
    return response.content

# Webアプリの概要・操作説明


st.title("専門家LLM質問アプリ")
st.markdown(
    """
**このアプリについて**

UFCまたはRIZINの専門家として振る舞うAIに質問できるWebアプリです。

---

**操作方法**

- 下のラジオボタンで専門家の種類を選択してください。
- 質問したい内容（例：現在のライト級のチャンピオンは誰？）を入力フォームに記入し、「送信」ボタンを押してください。
- AI専門家からの回答が画面に表示されます。
"""
)

st.divider()

# ラジオボタンで専門家の種類を選択
expert_type = st.radio("専門家の種類を選択してください", ("UFC", "RIZIN"))

# 入力フォーム
user_input = st.text_input("質問内容を入力してください")

# 送信ボタン

if st.button("送信"):
    if not OPENAI_API_KEY:
        st.error("OpenAI APIキーが設定されていません。環境変数OPENAI_API_KEYを設定してください。")
    elif user_input.strip() == "":
        st.warning("質問内容を入力してください。")
    else:
        with st.spinner("AI専門家が回答中..."):
            answer = get_llm_response(user_input, expert_type)
        st.success("AI専門家の回答:")
        st.write(answer)