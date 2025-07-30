import streamlit as st
from scraper import get_reviews

st.set_page_config(page_title="Review Aggregator", layout="wide")

st.title("🛒 Product Review Aggregator")
product = st.text_input("Enter Product Name (e.g., Lenovo LOQ):")

if st.button("Fetch Reviews"):
    with st.spinner("Fetching reviews from Flipkart..."):
        reviews = get_reviews(product)
        if reviews:
            for review in reviews:
                st.write(f"⭐ {review['rating']} - {review['text']}")
        else:
            st.error("No reviews found or error fetching.")
