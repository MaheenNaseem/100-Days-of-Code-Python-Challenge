import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Day 30: Added Error Handling for user input
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        # using list comprehension
        code_words_list = [nato_dict[each_alphabet] for each_alphabet in user_input]
    except KeyError:
        error_message = "Sorry, only letters in the alphabet please."
        print(error_message)
        generate_phonetic()
    else:
        print(code_words_list)

generate_phonetic()
