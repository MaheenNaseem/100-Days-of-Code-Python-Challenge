import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter your name: ").upper()

#using list comprehension
code_words_list = [nato_dict[each_alphabet] for each_alphabet in user_input]

#using for loop
# code_words_list = []
# for each_alphabet in user_input:
#     code = nato_dict[each_alphabet]
#     code_words_list.append(code)

print(code_words_list)