from gmail_reader import read_latest_email
from email_ai import summarize_email
from notifier import send_notification


def check_email():

    print("Checking email...")

    email_content = read_latest_email()

    summary = summarize_email(email_content)

    print(summary)

    send_notification(
        "📧 Email Summary",
        summary[:200]
    )