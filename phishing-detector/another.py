import pandas as pd

# Data for phishing dataset
data = {
    "Email Body": [
        "Congratulations, you've won a prize! Click here.",
        "Your package has been shipped.",
        "Urgent: Update your payment details now.",
        "Meeting scheduled at 2 PM.",
        "Get a free gift card now! Limited offer.",
        "Your invoice for the order is attached.",
        "Update your login credentials to avoid suspension.",
        "Upcoming event reminder: Annual company retreat."
    ],
    "Header Info": [
        "From: unknown@abc.com",
        "From: amazon@amazon.com",
        "From: alerts@bank-secure.com",
        "From: hr@company.com",
        "From: gift@promo-deals.com",
        "From: support@reputable-store.com",
        "From: noreply@secure-account.com",
        "From: events@company.com"
    ],
    "Label": [1, 0, 1, 0, 1, 0, 1, 0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("phishing_dataset.csv", index=False)

print("Dataset saved as phishing_dataset.csv")
