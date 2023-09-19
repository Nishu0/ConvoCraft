import warnings
import os
import streamlit as st

import sidebar
import chat
import llm

warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="ConvoCraft",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state=sidebar.sidebar_init_state,
    menu_items={
        "Report a bug": "https://github.com/Nishu0/ConvoCraft/issues",
        "About": """
            # ConvoCraft
            Transform conversations into stunning web apps. Dynamic code generation + intuitive interface. Unleash your creativity effortlessly. Use the power of GPT OpenAI LLM and Langchain.

            Go to the GitHub repo to learn more about the project. https://github.com/Nishu0/ConvoCraft
            """,
    },
)

sidebar.setup()

openai_api_key = st.secrets["openai_api_key"]

if openai_api_key:
    assistant = llm.setup(openai_api_key)
    generative_app_path = os.path.join(os.getcwd() , "generative_app", "pages" ,"🤖GeneratedApp.py")
    chat.setup(assistant, generative_app_path)

st.markdown('<div id="input-container-placeholder"></div>', unsafe_allow_html=True)