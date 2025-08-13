#TODO: Create a letter using starting_letter.txt 

#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as name_data:
    names_list = name_data.read().split()

with open("./Input/Letters/starting_letter.txt") as invite:
    letter_data = invite.read()

for each_name in names_list:
    # Replace the [name] placeholder with the actual name.
    final_letter = letter_data.replace("[name]", each_name)
    header = f"Letter_for_{each_name}"

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{header}",mode = "w") as final_invitation:
        final_invitation.write(final_letter)

print("Letters Created Successfully!")
