import imaplib
import email
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.header import decode_header



load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def extract_text_from_email(msg):
    
    subject, encoding = decode_header(msg["subject"])[0]
    
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")

    if msg.is_multipart():
        for part in msg.walk():

            content_type = part.get_content_type()

            payload = part.get_payload(decode=True)

            if not payload:
                continue

            text = payload.decode(errors="ignore")

            if content_type == "text/plain":
                return text

            if content_type == "text/html":
                soup = BeautifulSoup(text, "html.parser")
                return soup.get_text()

    else:
        payload = msg.get_payload(decode=True)
        text = payload.decode(errors="ignore")

        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    return ""


def read_latest_email():

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "UNSEEN")

    email_ids = messages[0].split()

    if not email_ids:
        return "Inbox is empty."

    latest_email_id = email_ids[-1]

    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = msg_data[0][1]

    msg = email.message_from_bytes(raw_email)

    subject = msg["subject"]

    body = extract_text_from_email(msg)

    mail.logout()

    return f"Subject: {subject}\n\n{body}"