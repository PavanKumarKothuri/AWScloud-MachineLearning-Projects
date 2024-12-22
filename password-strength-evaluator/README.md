# Password Strength Evaluator

A simple web application to assess password strength using machine learning.  
The app evaluates password strength based on length, character diversity, and entropy using a trained model.

## Features
- Analyzes passwords for:
  - Length
  - Character diversity
  - Use of special characters
- Classifies passwords as **Weak** or **Strong** using a Random Forest model.
- User-friendly interface built with Streamlit.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the web interface.
- **Scikit-learn**: For machine learning model training.
- **NumPy** and **Pandas**: For data manipulation.
- **Joblib**: For saving and loading the trained model.

## How It Works
1. Passwords are vectorized using character-level n-grams (via `TfidfVectorizer`).
2. A Random Forest Classifier is trained to label passwords as strong or weak.
3. The Streamlit app provides a simple UI for users to input passwords and check their strength.

## Installation and Usage

### Prerequisites
- Python 3.8+
- Required Python packages:
  - `streamlit`
  - `scikit-learn`
  - `numpy`
  - `pandas`
  - `joblib`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/PavanKumarKothuri/CyberSecurity-MachineLearning-Projects/tree/main/password-strength-evaluator.git
   cd password-strength-evaluator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser (default: `http://localhost:8501`).

## File Structure
```
password-strength-evaluator/
│
├── app.py               # Streamlit app script
├── password_data.csv     # Mock password dataset
├── password_model.pkl    # Trained Random Forest model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Inspired by the need for secure passwords in online systems.
- Special thanks to the open-source community.

---
Happy coding! 🎉