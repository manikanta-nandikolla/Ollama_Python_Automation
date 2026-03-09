import schedule
import time

from email_task import check_email
from meeting_task import check_meeting
from file_task import organize_downloads


def main():

    print("\n==============================")
    print(" AI AUTOMATION ASSISTANT")
    print("==============================\n")

    print("Automation system started...")

    # Check email every hour
    schedule.every(1).hours.do(check_email)

    # Analyze meeting daily
    schedule.every().day.at("09:00").do(check_meeting)

    # Organize files every 30 minutes
    schedule.every(30).minutes.do(organize_downloads)

    while True:

        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()