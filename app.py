
import streamlit as st
import joblib

st.set_page_config(
    page_title="Cynbit AI Classifier",
    page_icon="🤖"
)

# Load trained model and vectorizer
model = joblib.load("cynbit_model.pkl")
vectorizer = joblib.load("cynbit_vectorizer.pkl")

st.title("Cynbit AI Inquiry Classifier")
st.write("Enter a customer inquiry to predict its category.")

inquiry = st.text_area(
    "Customer Inquiry",
    placeholder="I need an AI chatbot for my business"
)

if st.button("Predict Category"):
    if inquiry.strip():
        inquiry_vector = vectorizer.transform([inquiry])
        prediction = model.predict(inquiry_vector)

        st.success("Predicted Category: " + prediction[0])
    else:
        st.warning("Please enter a customer inquiry.")
