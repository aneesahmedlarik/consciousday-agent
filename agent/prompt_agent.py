import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI   
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# ✅ Set Google Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyA-d4_-4CtqFDWWhukNYI03zBte289n7dE"

# ✅ Gemini Model Initialization
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# ✅ Prompt Template
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

# ✅ Create the LLM Chain
chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)

# ✅ Define generation function
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
