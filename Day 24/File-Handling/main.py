#opening the file and reading its content

with open("file.txt") as file:
     content = file.read()
     print(content)

#write inside the file

with open("file.txt", mode = "w") as file:
    file.write("File was Overwrited.")

#appending something inside the file

with open("file.txt", mode = "a") as file:
    file.write("\nFile was appended.")


