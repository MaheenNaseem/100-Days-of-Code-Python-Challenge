#TODO: Create modularity, Add input validation 
import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)

def play_game():

    replay = True

    while replay:

        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.\n")

        
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

        #checks if user want to play easy/hard level
        if difficulty == "easy":
            tries = 10
        else:
            tries = 5
            
        #randomly generates a number
        number = random.randint(1, 100)

        #list for all the guessed numbers
        guessed_number = []

        #runs until tries are 0 
        while tries > 0:

            print(f"\nYou have {tries} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            #TODO: error handling for input other than int

            if guess > 0 and guess < 101:

                if guess in guessed_number:
                    print(f"You've already guessed the number {guess}. Guess again.")
                    continue #skips the rest of the loop

                if guess == number:
                    print(f"You got it! The answer was {number}.")
                    break

                elif guess > number:
                    tries -= 1
                    guessed_number.append(guess)
                    print("Too High. Guess again.")
                elif guess < number:
                    guessed_number.append(guess)
                    tries -= 1
                    print("Too Low. Guess again.")

            else:
                print("Sorry, your guess is outside the range")
        if tries == 0:
            print(f"\nYou've run out of guesses. The answer was {number}.")

        play = input("\nDo you want to play again? Y/N. ")
        if play.lower() == "n":
            print("Goodbye.")
            replay = False
        elif play.lower() == "y":
            print("\n" * 15)
            print(logo)

play_game()
