from pathlib import Path

# Home Directory
print(Path.home())

# Current Working Directory
print(Path.cwd())


# All about given file from its path
path = Path("/home/rakesh12/Projects/AFour_Stage2/I_O_Operations/A1.py")
print("Parent:", path.parent)
print("NameOfFile:", path.name)
print("Extension:", path.suffix)


# Read write with pathlib
print("--------------------------")

path = Path.cwd() / "Sample.txt"
# content = path.read_text()
# print(content)

# writing in the file
path.write_text("Hello, I am writing in the file from my Python code\n")

# reading the text file
content = path.read_text()
print(content)


# Creating a file

filePath = Path("New.txt")
filePath.touch(exist_ok=True)


# Deleting a file
path = Path.cwd() / "New.txt"
path.unlink()
