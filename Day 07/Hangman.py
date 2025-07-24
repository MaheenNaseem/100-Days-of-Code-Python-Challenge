import random

#import stages for the hangman figure
from hangman_art import logo, stages
#imports words from hangman words file
from hangman_words import words
#player's tries 
lives = 6

#prints hangman logo from file
print(logo)

#selects a random word from list
chosen_word = random.choice(word_list)

#displays the chosen word at the beginning 
#print(chosen_word)

#displays the chosen word in underscore format
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("\nWord to guess: " + placeholder)


game_over = False

#to prevent overwriting of the display
correct_letters = []

#to allows user to guess until game over
while not game_over:

    print(f"\n------------------------{lives}/6 LIVES LEFT------------------------\n")

    #takes input from user
    guess = input("Guess a letter: ").lower()

    #inform user if their guess was repeated
    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    display = ""

    #checks if guesses letter is in chosen word
    for letter in chosen_word:

        if letter == guess:
            display += letter               #replace the _ with the correct guess
            correct_letters.append(guess)   #add the correct word in the correct letter list

        #to prevent overwriting of the display
        elif letter in correct_letters:
            display += letter               #if the word exists in the correct letter list it will show the letter to the user

        else:
            display += "_"

    print("\nWord to guess: " + display)

    if "_" not in display:
        game_over = True
        print("YOU WIN!")

    #logic for the game 
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    #prints the hangman figure according to lives remaining
    if lives > 0:
        print(stages[lives])
    elif lives == 0:
        game_over = True
        print(stages[0])
        print(f"\nIt was {chosen_word.upper()}! YOU LOSE!")
