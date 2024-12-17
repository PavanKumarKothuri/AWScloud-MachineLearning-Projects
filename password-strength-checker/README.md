# 🔒 **Password Strength Checker**  
### An interactive tool to evaluate password strength and provide actionable feedback.  

---

## **🚀 Project Overview**  
The **Password Strength Checker** helps users analyze the strength of their passwords based on key metrics like:  
1. **Length**  
2. **Character Diversity** (Uppercase, Numbers, Special Characters)  
3. **Entropy Calculation**  

The tool gives a **strength score** and suggestions to help users create stronger passwords.  

---

## **📸 Project Demo**  
![App Screenshot](demo-screenshot.png)  

---

## **🎯 Features**  
- ✅ **Password Length Check:** Ensures passwords meet minimum length requirements.  
- ✅ **Character Diversity:** Checks for the inclusion of uppercase letters, numbers, and special characters.  
- ✅ **Entropy Calculation:** Measures password unpredictability using mathematical entropy.  
- ✅ **Actionable Feedback:** Provides suggestions to improve password security.  
- ✅ **Real-Time Strength Score:** Displays a percentage-based score for password strength.  

---

## **🛠️ Tech Stack**  
- **Language:** Python  
- **Framework:** Streamlit  
- **Libraries:**  
   - `re` for Regex checks  
   - `math` for entropy calculations  

---

## **💻 How to Run Locally**  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/pavankumarkothuri/password-strength-checker.git
   cd password-strength-checker
   ```  

2. **Install Dependencies**:  
   Make sure you have Python and pip installed. Install Streamlit:  
   ```bash
   pip install streamlit
   ```  

3. **Run the Application**:  
   Execute the Streamlit app from the terminal:  
   ```bash
   streamlit run password_strength_checker.py
   ```  

4. **Open in Browser**:  
   Streamlit will open the app in your browser at `http://localhost:8501`.  

---

## **🧩 Code Explanation**  

1. **Entropy Calculation**  
   - Entropy measures the randomness of a password:  
   ```python
   charset_size = 0
   if any(char.islower() for char in password):
       charset_size += 26
   entropy = len(password) * math.log2(charset_size)
   ```

2. **Feedback Generation**  
   - Regex is used to check for character diversity:  
   ```python
   if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
       feedback.append("Add special characters for better strength.")
   ```

3. **Strength Score**  
   - Calculates the strength as a percentage:  
   ```python
   strength_score = (strength / 5) * 100
   ```  

---

## **📝 Example Output**  
| **Password**     | **Strength Score** | **Feedback**                          |  
|-------------------|--------------------|---------------------------------------|  
| `12345`          | 20%                | Too short, no special characters.     |  
| `Hello123`       | 60%                | Add special characters.               |  
| `H3llo@World`    | 100%               | Strong password!                      |  

---

## **🌐 Deployment**  
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud).  
- [Live Demo Link](https://your-app-link.streamlit.app)  

---

## **🚀 Enhancements**  
Ideas for future improvements:  
1. **Password Generator:** Automatically generate strong passwords.  
2. **Secure Storage:** Store and retrieve hashed passwords securely.  
3. **API Integration:** Build an API for third-party applications.  

---

## **📂 Project Structure**  
```
password-strength-checker/
│
├── password_strength_checker.py    # Main Streamlit app
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
```

---

## **🤝 Contributing**  
Contributions are welcome! Please fork this repository and open a pull request.  

---

## **📧 Contact**  
For any queries, feel free to reach out:  
- **Email:** your.email@example.com  
- **LinkedIn:** [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)  

---

## **⭐ Show Your Support**  
If you find this project helpful, please give it a ⭐ on GitHub!  