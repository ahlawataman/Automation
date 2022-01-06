import os
import argparse
from posixpath import dirname

parser = argparse.ArgumentParser(description="Clean up directory and put files into corresponding folders.")

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the to be cleaned up directory"
)

args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

# get all files from the current directory
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]
moved = 0
created_folders = []

# go through all files and move them into corresponding folders
for doc in docs:
    # separate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    # skip this python file and all hidden files
    if doc_name == "directory_clean" or doc_name.startswith("."):
        continue

    # get the subfolder name and create the folder if not exists
    subfolder_path = os.path.join(path, filetype[1:].lower()) # ignore . in ".txt"

    if subfolder_path not in folders and subfolder_path not in created_folders:
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as err:
            print(f"Folder already exists at {subfolder_path}... {err}")

    # get the new folder path and move the file
    new_doc_path = os.path.join(doc_path, subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1

    print(f"Moved file {doc} to {new_doc_path}")

print(f"Renamed {moved} of {len(docs)} files.")