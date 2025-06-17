from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st

llm = ChatGoogleGenerativeAI(
    google_api_key=st.secrets["GOOGLE_API_KEY"],  # or hardcoded just for local
    model="gemini-pro",
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

chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))

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
