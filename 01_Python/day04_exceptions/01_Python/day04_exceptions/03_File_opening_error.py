# 1. Ask the user for a filename
filename = input("Enter filename: ")

try:
    # 2 & 3. Attempt to open in read mode ("r") using the filename variable
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:")
        print(content)

# 4. Handle the specific error if the file does not exist
except FileNotFoundError:
    print("Error: File was not found.")

# 5. This block runs no matter what happens above
finally:
    print("File operation completed.")

