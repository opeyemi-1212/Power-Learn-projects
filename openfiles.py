# Open the file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
# Print the content of the file
print(content);

with open('Assignment.txt', 'w') as file:
    file.write("This is a new line of text")

try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.");
