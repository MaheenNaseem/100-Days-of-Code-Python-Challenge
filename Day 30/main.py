# File Not Found Error :  No such file or directory
# with open ("a_file.txt") as file:
#     file.read()

# Key Error: retrieving a value from the key that does not exist in the dictionary
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

# Index Error: fetch element on the index that does not exist in the list
# fruits = ["mango", "pear", "apple"]
# print(fruits[3])

# Type Error: using any data type instead of the one it requires
# a= 3
# b="k"
# print(a+b)

# Catching Exception for File not Found and Key Error:
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", mode = "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key does not exist {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()

