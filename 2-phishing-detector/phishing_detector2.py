import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import pickle
import streamlit as st

# Load dataset
data = pd.read_csv("phishing_dataset.csv")

# Combine features
data['Combined'] = data['Email Body'] + " " + data['Header Info']

# Split data
X = data['Combined']
y = data['Label']

# Vectorize text
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.3, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model and vectorizer
with open("phishing_detector.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

# Predict
y_pred = model.predict(X_test)

# Accuracy and Report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legitimate", "Phishing"])
disp.plot()

# Load model and vectorizer
with open("phishing_detector.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Streamlit App
st.title("Phishing Email Detector")
st.write("Enter email details below to check if it is a phishing attempt:")

# Input fields
email_body = st.text_area("Email Body")
header_info = st.text_input("Header Info")

# Detect button
if st.button("Detect"):
    if email_body and header_info:
        input_text = [email_body + " " + header_info]
        input_vect = vectorizer.transform(input_text)
        prediction = model.predict(input_vect)
        result = "Phishing" if prediction[0] == 1 else "Legitimate"
        st.write(f"Result: **{result}**")
    else:
        st.write("Please enter both Email Body and Header Info.")
