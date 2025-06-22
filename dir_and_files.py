import os
import string
import shutil

#1 List only directories, only files, and all in a specified path
def list_path_contents(path):
    print("#1 Contents of path:", path)
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All entries:", os.listdir(path))

# Example usage:
list_path_contents(".")


#2 Check access to a specified path
def check_access(path):
    print(f"#2 Access check for path: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# Example usage:
check_access(".")


#3 Test if path exists; if so, show filename and directory
def test_path(path):
    print(f"#3 Testing path: {path}")
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

# Example usage:
test_path("example.txt")


#4 Count number of lines in a text file
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"#4 Number of lines in {file_path}: {len(lines)}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage:
count_lines("example.txt")


#5 Write a list to a file
def write_list_to_file(file_path, items):
    with open(file_path, 'w') as file:
        for item in items:
            file.write(f"{item}\n")
    print(f"#5 List written to file: {file_path}")

# Example usage:
write_list_to_file("list_output.txt", ["apple", "banana", "cherry"])


#6 Generate 26 text files named A.txt to Z.txt
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")
    print("#6 Alphabet files A.txt to Z.txt created.")

# Example usage:
generate_alphabet_files()


#7 Copy the contents of a file to another file
def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
        print(f"#7 Contents copied from {src} to {dst}")
    except FileNotFoundError:
        print(f"Source file not found: {src}")

# Example usage:
copy_file("list_output.txt", "copied_output.txt")


#8 Delete file by specified path with checks
def delete_file(path):
    print(f"#8 Deleting file: {path}")
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")

# Example usage:
delete_file("copied_output.txt")
