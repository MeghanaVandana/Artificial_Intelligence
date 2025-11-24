"""
eval_email_receive.py
Simple IMAP check example to list recent subjects from an IMAP mailbox.
Requires: pip install imap-tools
"""

from imap_tools import MailBox, AND
import os

IMAP_HOST = os.environ.get("EMAIL_IMAP_HOST", "imap.gmail.com")
IMAP_USER = os.environ.get("EMAIL_ADDRESS")
IMAP_PASS = os.environ.get("EMAIL_PASSWORD")

def list_recent_subjects(limit=10):
    if not IMAP_USER or not IMAP_PASS:
        raise EnvironmentError("Set EMAIL_ADDRESS and EMAIL_PASSWORD env variables.")
    with MailBox(IMAP_HOST).login(IMAP_USER, IMAP_PASS, 'INBOX') as mailbox:
        messages = mailbox.fetch(limit=limit)
        for msg in messages:
            print(f"From: {msg.from_} | Subject: {msg.subject}")

if __name__ == "__main__":
    list_recent_subjects(10)
