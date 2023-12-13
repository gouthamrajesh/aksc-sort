import os
import re
import shutil

# Define the source directory and pattern components
source_dir = "./certi"  # Update with the path to your source directory
start_pattern = r"(.*?)\("
clg_name_pattern = r"([\w\s]+)\)"
end_pattern = r"\.pdf"

# Combine the patterns into a single regex
pattern = re.compile(f"{start_pattern}{clg_name_pattern}{end_pattern}")

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    # Apply the regex to extract the CLG_NAME
    match = pattern.match(filename)
    if match:
        # Extract the CLG_NAME
        clg_name = match.group(1)

        # Create a subfolder for the CLG_NAME if it doesn't exist
        clg_folder_path = os.path.join(source_dir, clg_name)
        if not os.path.exists(clg_folder_path):
            os.makedirs(clg_folder_path)

        # Move the file to the subfolder
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(clg_folder_path, filename)
        shutil.move(source_path, dest_path)

print("PDF files successfully sorted and moved to subfolders!")
