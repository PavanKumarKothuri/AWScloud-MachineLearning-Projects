import pandas as pd
import numpy as np
import string
import random

# Generate random passwords
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Label passwords as strong (1) or weak (0)
def label_password(password):
    if len(password) >= 12 and any(c in string.punctuation for c in password):
        return 1  # Strong
    else:
        return 0  # Weak

# Generate a dataset
data = []
for _ in range(1000):
    length = random.randint(6, 16)
    password = generate_password(length)
    strength = label_password(password)
    data.append([password, strength])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Password", "Strength"])
df.to_csv("password_data.csv", index=False)
print("Dataset created and saved as password_data.csv!")
