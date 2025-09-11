#My Code

def calculate_love_score(name_1, name_2):

    true_check = 0
    love_check = 0

    #Uppercasing the names and saving them in list
    names_list = list(name_1.upper()) + list(name_2.upper())
    print(names_list)

    for check in "TRUE":

        if check in names_list:
            counter_for_true = names_list.count(check)
            print(f"{check} occurs {counter_for_true} times")
            true_check += counter_for_true
        else:
            print(f"{check} occurs 0 times")

    print("Total = ", true_check)

    for check in "LOVE":

        if check in names_list:
            counter_for_love = names_list.count(check)
            print(f"{check} occurs {counter_for_love} times")
            love_check += counter_for_love
        else:
            print(f"{check} occurs 0 times")

    print("Total = ", love_check)

    total = str(true_check) + str(love_check)
    print("Love Score = ", total)

name1 = input("Enter First Name: ")
name2 = input("Enter Second Name: ")

calculate_love_score(name_1 = name1,name_2 = name2)
