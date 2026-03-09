from file_organizer import organize_folder
from notifier import send_notification


def organize_downloads():

    folder = r"E:\zzzzzz"

    organize_folder(folder)

    send_notification(
        "📂 File Organizer",
        "Downloads folder organized successfully."
    )