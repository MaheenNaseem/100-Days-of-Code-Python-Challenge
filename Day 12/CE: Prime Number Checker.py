def is_prime(num):
    divisible = []
    for i in range(1, num):
        if num % i == 0:
            divisible.append(i)

    if len(divisible) == 1:
        return True
    else:
        return False

number = int(input("Enter a number: "))
answer = is_prime(number)
print(f"{number} is a Prime Number: {answer}")
