"""
send_email_example.py
A simple example using yagmail to send an email (similar to plugin usage).
Make sure to install yagmail:
pip install yagmail
"""

import yagmail
import os

# Recommended: store credentials in environment variables or .env and load them
EMAIL = os.environ.get("EMAIL_ADDRESS")  # e.g., youremail@gmail.com
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")  # app password or token

def send_test_email(to_address: str, subject: str, contents: str):
    if EMAIL is None or EMAIL_PASSWORD is None:
        raise EnvironmentError("Set EMAIL_ADDRESS and EMAIL_PASSWORD env variables or fill them in the script.")
    yag = yagmail.SMTP(EMAIL, EMAIL_PASSWORD)
    yag.send(to=to_address, subject=subject, contents=contents)
    print(f"Email sent to {to_address}")

if __name__ == "__main__":
    # example usage
    send_test_email(
        to_address="vmeghana890@gmail.com",
        subject="Invitation to my Birthday Party",
        contents="Hello, I’m Meghana. The party starts at 8 pm this Friday..."
    )
