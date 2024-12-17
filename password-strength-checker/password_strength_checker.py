import streamlit as st
import math
import re

# Function to calculate password entropy
def calculate_entropy(password):
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26  # Lowercase letters
    if any(char.isupper() for char in password):
        charset_size += 26  # Uppercase letters
    if any(char.isdigit() for char in password):
        charset_size += 10  # Digits
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        charset_size += 32  # Special characters
    if charset_size == 0:
        return 0  # No valid characters
    return len(password) * math.log2(charset_size)

# Function to check password strength
def evaluate_password(password):
    feedback = []
    strength = 0

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    else:
        strength += 1

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Add special characters for better strength.")
    else:
        strength += 1

    # Check for numbers
    if not any(char.isdigit() for char in password):
        feedback.append("Include numbers for better strength.")
    else:
        strength += 1

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("Add uppercase letters for better strength.")
    else:
        strength += 1

    entropy = calculate_entropy(password)
    if entropy < 40:
        feedback.append("Entropy is low. Use a longer and more diverse password.")
    elif entropy >= 60:
        strength += 1

    strength_score = (strength / 5) * 100
    return strength_score, feedback

# Streamlit App
def main():
    st.title("🔒 Password Strength Checker")
    st.write("Enter a password to check its strength.")

    password = st.text_input("Password:", type="password")

    if st.button("Check Strength"):
        if not password:
            st.warning("Please enter a password to analyze.")
        else:
            strength_score, feedback = evaluate_password(password)
            st.write(f"**Strength Score:** {strength_score:.2f}%")

            if feedback:
                st.error("Suggestions for improvement:")
                for tip in feedback:
                    st.write(f"- {tip}")
            else:
                st.success("Your password is strong!")

if __name__ == "__main__":
    main()
