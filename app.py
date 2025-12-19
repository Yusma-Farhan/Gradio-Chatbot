import gradio as gr
from groq import Groq

# ⚠️ Your Groq API key (paste directly here)
import os
API_KEY = os.environ["GROQ_API_KEY"]


client = Groq(api_key=API_KEY)

def chat_with_groq(message, history):
    try:
        chat_history = []
        for human, ai in history:
            chat_history.append({"role": "user", "content": human})
            chat_history.append({"role": "assistant", "content": ai})

        chat_history.append({"role": "user", "content": message})

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ Updated active model
            messages=chat_history
        )

        reply = completion.choices[0].message.content
        return reply

    except Exception as e:
        return f"⚠️ Error: {e}"

# 🧠 Simple Gradio UI
chatbot = gr.ChatInterface(
    fn=chat_with_groq,
    title="🤖 Groq Chatbot",
    description="A chatbot powered by Groq's Llama 3.1 model. Built with ❤️ using Gradio.",
    theme="soft",
    examples=["Hello!", "Who are you?", "Tell me a fun fact!"]
)

if __name__ == "__main__":
    chatbot.launch()
