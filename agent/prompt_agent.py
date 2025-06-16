import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# ✅ Load API key securely from Streamlit Secrets
api_key = st.secrets["OPENAI_API_KEY"]

# ✅ Define LLM with OpenRouter settings
llm = ChatOpenAI(
    openai_api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3-8b-instruct",
    temperature=0.7
)

# ✅ Prompt template to guide the reflection agent
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

# ✅ Combine LLM and prompt into a LangChain Chain
chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)

# ✅ Function to run the reflection agent
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
