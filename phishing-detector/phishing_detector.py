# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# Step 1: Simulate a Dataset
data = {
    'Email': [
        "Congratulations! You've won a lottery. Claim your prize now!",
        "Your account has been compromised. Click here to reset your password.",
        "Meeting scheduled for 3 PM tomorrow. Please confirm attendance.",
        "Invoice attached. Kindly process the payment.",
        "Update your bank details to avoid suspension.",
        "Lunch with the team tomorrow at 12 PM. See you there!",
    ],
    'Label': [1, 1, 0, 0, 1, 0]  # 1: Phishing, 0: Legitimate
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 2: Preprocess the Data
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

df['Processed_Email'] = df['Email'].apply(preprocess)

# Step 3: Feature Extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Processed_Email'])  # Transform email text to feature vectors
y = df['Label']  # Labels

# Step 4: Split Data for Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Machine Learning Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Test with New Emails
new_emails = [
    "Congratulations, you won $10,000! Click to claim.",
    "Don't miss our meeting tomorrow at 10 AM."
]
new_emails_processed = [preprocess(email) for email in new_emails]
new_emails_vectorized = vectorizer.transform(new_emails_processed)
predictions = model.predict(new_emails_vectorized)

for email, pred in zip(new_emails, predictions):
    print(f"Email: {email} --> {'Phishing' if pred == 1 else 'Legitimate'}")
