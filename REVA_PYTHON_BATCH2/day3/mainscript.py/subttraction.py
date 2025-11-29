#Reading content from data.txt and printing it

with open("data.txt", "r") as file:
    content = file.read()

print("Contents of data.txt:")
print(content)