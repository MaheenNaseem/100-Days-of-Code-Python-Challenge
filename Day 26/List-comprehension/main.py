# Coding Exercise: Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

#Coding Exercise: Filtering Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result)

# Coding Exercise: Data Overlap
# file1.txt = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
# file2.txt = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

with open("file1.txt") as file:
    list1 = file.read().split()

list1 = [int(num) for num in list1]

with open("file2.txt") as file2:
    list2 = file2.read().split()

list2 = [int(num) for num in list2]


result = [num for num in list1 if num in list2]

print(result)
