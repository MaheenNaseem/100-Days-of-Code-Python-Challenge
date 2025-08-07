def is_leap_year(year):
    
    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                leap_year = True

            else:
                leap_year = False
        else:
            leap_year = True

    else:
        leap_year = False
    return leap_year

print("LEAP YEAR OR NOT?\n")
input_year = int(input("Enter a Year: \n"))
output = is_leap_year(input_year)
print(f"{input_year} was a leap year: {output}")
