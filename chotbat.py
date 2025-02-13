import streamlit as st
import os
import google.generativeai as genai

# Title with custom font size and color
st.title("Chotbat333")


# API Key and Model Configuration
os.environ['GOOGLE_API_KEY'] = "AIzaSyBarcP_PUAEYV1kbCW84K46Bm21LgEXB88"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Ask me Anything 💬"
        }
    ]

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to handle query and response
def llm_function(query):
    response = model.generate_content(query)

    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response.text
        }
    )

# User input section with a custom placeholder text
query = st.chat_input("What's on your mind? 🤔")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)

