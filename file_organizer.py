import os
import shutil
from ai_file_classifier import classify_file

def organize_folder(folder_path):

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        print("Processing:", file)

        category = classify_file(file)

        if "Folder name:" in category:
            category = category.split("Folder name:")[-1]

        category = "".join(c for c in category if c.isalnum() or c in (" ", "_", "-"))
        category = category.strip()

        if not category:
            category = "Others"

        new_folder = os.path.join(folder_path, category)
        os.makedirs(new_folder, exist_ok=True)

        destination = os.path.join(new_folder, file)

        if os.path.exists(destination):
            print(f"Skipping duplicate: {file}")
            continue

        shutil.move(file_path, destination)

        print(f"Moved {file} → {category}")