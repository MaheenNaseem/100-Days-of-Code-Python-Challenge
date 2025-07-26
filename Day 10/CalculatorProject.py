from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#dictionary for the calculations - Storing Functions as a key's Value
operations_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}

#calculator function
def calculator():

    new = True
    #outer loop
    while new:
        num1 = float(input("Enter the first number: "))

        loop = True
        #inner loop
        while loop:

            # prints the operations (dictionary's key)
            print("\nOperations:")
            for key in operations_dict.keys():
                print(key)
            operation_symbol = input("Pick an operation: ")

            num2 = float(input("Enter the second number: "))

            #calculate the answer for using the dictionary, the operation symbol and passing the number parameters to it
            answer = operations_dict[operation_symbol](num1, num2)

            #prints the answer in a 3 + 3 = 6 format
            print(f"\n{num1} {operation_symbol} {num2} = {answer}")

            #asking user to enter y/n
            choice = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
            
            #overwrite the first number with the answer of the previous and keeps looping until user chooses new calculation
            if choice == "y":
                num1 = answer
            
            #if user chose n then inner loop is exit and num1 is asked again
            elif choice == "n":
                loop = False
                print("\n" * 20)
                print(logo)

calculator()
