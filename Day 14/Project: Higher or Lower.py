#Higher or Lower Game
#TODO: Input Validation

from art import logo, vs
from game_data import data
from random import choice

def anti_duplication(ch_a, ch_b):
    """Prevents same Celebrity being selected."""
    while ch_a == ch_b: #runs until choice a is equal to choice b
        ch_b = choice(data)
    return ch_b


def answer_check(guess, ch_a, ch_b):
    """Checks if the user's guess is correct."""
    if guess == "a":
        if ch_a['follower_count'] > ch_b['follower_count']:
            return True, ch_a
        else:
            return False, None
    elif guess == "b":
        if ch_b['follower_count'] > ch_a['follower_count']:
            return True, ch_b
        else:
            return False, None
    return True

def printing (choice_a, choice_b):
    """Prints on the environment of the user's choice."""
    # display the first data (A)
    print(f"Compare A: {choice_a['name']},a {choice_a['description']}, from {choice_a['country']}")

    print(vs)
    # display the second data (B)
    print(f"\nAgainst B: {choice_b['name']},a {choice_b['description']}, from {choice_b['country']}")

    #prints

def swaps (winning, ch_a, ch_b):
    """Swap the winning choice and assign a new second choice."""
    ch_a = winning
    ch_b = choice(data) # assigns new data to choice b
    return ch_a, ch_b


def play_higher_lower():

    replay = True
    while replay:
        print(logo)

        #selects two choices from the data
        choice_a = choice(data)
        choice_b = choice(data)
        score = 0

        game_over = False
        while not game_over:

            choice_b = anti_duplication(choice_a, choice_b)

            printing(choice_a, choice_b)

            guess = input("Who has more followers? Type 'A' or 'B': ")

            answer, winning_choice = answer_check(guess, choice_a, choice_b)

            #if answer is correct then score is calculated and shown to user
            if answer:
                score += 1
                print(logo)
                print(f"You're right! Current score: {score}")

                # provides a new choice
                choice_a, choice_b = swaps(winning_choice, choice_a, choice_b)

            else:
                #if the user couldn't pick the right option it prints the score and exits the loop
                print("\n"*5)
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                break

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == "n":
            print("Thank you for playing! See You Again")
            replay = False
        else:
            print("\n"*10)
            replay = True

play_higher_lower()
