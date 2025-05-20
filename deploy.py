import streamlit as st
from openai import OpenAI

# Initialize the client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.set_page_config(page_title="LLaMA Chatbot", page_icon="🤖")
st.title("💬 Chat with LLaMA 3.3 (8B - Instruct)")

# User input
user_input = st.text_input("Ask something:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3.3-8b-instruct:free",
                messages=[{"role": "user", "content": user_input}],
                extra_headers={
                    "HTTP-Referer": "https://bandalapatiramakrishna.com",  # Optional
                    "X-Title": "Rama krishna Agent",  # Optional
                },
            )
            st.success("Response:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")
