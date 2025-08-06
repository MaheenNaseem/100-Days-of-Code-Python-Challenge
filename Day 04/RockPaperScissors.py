import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice < 0 and user_choice >= 3:
    print("Invalid choice.")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    #logic for the game rules

    #1. is user choose 0(rock) and computer choose 2(scissor)
    # user wins
    # this condition contradicts 3
    if user_choice == 0 and computer_choice == 2:
        print("You win!")

    #2. if user choose 2(scissors and computer choose 0(rock)
    # computer wins
    #this condition contradicts 4
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")

    #3. if user's choice is less than computer's
    # computer wins
    elif user_choice < computer_choice:
        print("You lose!")

    #4. if user's choice is greater than computers
    # user wins
    elif user_choice > computer_choice:
        print("You win!")

    # computer and user choose same =  draw
    elif computer_choice == user_choice:
        print("It's a draw!")
