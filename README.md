# 🌞 ConsciousDay Agent

> Reflect inward. Act with clarity.

**ConsciousDay Agent** is an AI-powered journaling and day-planning assistant built with **Streamlit**, **LangChain**, and **OpenRouter API**. It helps users reflect on their thoughts, analyze dreams, understand mindset, and generate a strategic plan for the day — all from a simple morning input.

---

## ✨ Features

- 📝 Submit a **Morning Journal**, **Dream**, **Daily Intention**, and **Top 3 Priorities**
- 🧠 Get AI-generated:
  - **Inner Reflection Summary**
  - **Dream Interpretation**
  - **Mindset Insight**
  - **Day Strategy Plan**
- 💾 Stores each entry in a local **SQLite** database
- 📆 View previous reflections by date
- 🔐 (Optional) Add auth & session state for more control

---

## 🧠 Built With

| Layer        | Tech                          |
|--------------|-------------------------------|
| 💻 UI        | [Streamlit](https://streamlit.io)             |
| 🧠 LLM Agent | [LangChain](https://www.langchain.com/) + [OpenRouter](https://openrouter.ai) |
| 🗃 Database   | SQLite (via `sqlite3`)        |
| 🧪 Testing    | Python unit tests             |

---

## 🚀 Try the App Live

> 🌐 [Live Demo on Streamlit Cloud](https://consciousday-agent.streamlit.app)  
(*Replace this with your actual link after deployment*)

---

## 🛠️ Getting Started (Local Setup)

### 1. Clone the repo

```bash
git clone https://github.com/aneesahmedlarik/consciousday-agent.git
cd consciousday-agent
