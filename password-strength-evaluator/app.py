import streamlit as st
import joblib
import numpy as np

# Load the model and vectorizer
model = joblib.load("password_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("Password Strength Evaluator")
st.markdown("""
Enter a password to check its strength.  
The app will classify the password as **Weak** or **Strong** based on its features.
""")

# Input field
password = st.text_input("Enter Password:")

if st.button("Check Strength"):
    if password:
        # Feature extraction
        features = vectorizer.transform([password])
        prediction = model.predict(features)[0]
        strength = "Strong" if prediction == 1 else "Weak"
        
        # Display result
        st.write(f"The password is **{strength}**!")
    else:
        st.write("Please enter a password to evaluate.")
