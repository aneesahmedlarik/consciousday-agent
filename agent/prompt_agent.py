import streamlit as st
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models.base import BaseChatModel
import os

from langchain_core.runnables import Runnable

from langchain_core.language_models.chat_models import SimpleChatModel

# ✅ Force OpenRouter API to authenticate via headers using environment var
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    temperature=0.7
)

prompt_template = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)

def generate_reflection(journal, dream, intention, priorities):
    try:
        return chain.run({
            "journal": journal,
            "dream": dream,
            "intention": intention,
            "priorities": priorities
        })
    except Exception as e:
        st.error(f"❌ LLM error: {e}")
        return None
