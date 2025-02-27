import os

# Define the directory and file name
directory = r"C:\Users\tony\Downloads"
file_name = "delete.docx"

# Combine directory and file name to form the full file path
full_path = os.path.join(directory, file_name)

# Check if the file exists and delete it, otherwise inform the user
if os.path.exists(full_path):
    os.remove(full_path)
    print("File deleted.")
else:
    print("File does not exist")
