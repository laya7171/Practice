import streamlit as st
from  chatbot import generate_response

st.title("Simple text completion chatbot")

user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)  # Call the function
        st.text_area("Chatbot:", value=response, height=200)  # Display the response
    else:
        st.warning("Please enter a message.")