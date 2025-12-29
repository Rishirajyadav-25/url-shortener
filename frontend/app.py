import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# BACKEND_URL = "http://localhost:8000"
BACKEND_URL =  os.getenv("BASE_URL")

st.set_page_config(page_title="URL Shortener", page_icon="🔗")

st.title("🔗 URL Shortener")

long_url = st.text_input("Enter a long URL")

if st.button("Shorten URL"):
    if not long_url:
        st.error("Please enter a URL")
    else:
        response = requests.post(
            f"{BACKEND_URL}/shorten",
            json={"long_url": long_url}
        )

        if response.status_code == 200:
            short_url = response.json()["short_url"]
            st.success("Short URL created!")
            st.code(short_url)
        else:
            st.error("Failed to shorten URL")
