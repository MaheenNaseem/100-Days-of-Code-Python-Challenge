#imports logo from art file
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function for encoding and decoding 
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
  
    # reverse the shift range when user decodes 
    if encode_or_decode == "decode":
        shift_amount *= -1
      
    for letter in original_text:
        #if any special character or space is found it will be sent to output text consecutively
        if letter not in alphabet:
            output_text += letter
        else:
            if letter in alphabet:
                #takes the alphabet's index and add the shift for new alphabet selection
                shifted_position = alphabet.index(letter) + shift_amount 
                # index would remain inside 0-25 range 
                #(34(z+9(shift_amount) % 25 = 9))
                shifted_position %= len(alphabet)                        
                output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}\n")
  
repeat = False
#to repeat the program
while not repeat:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    decision = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()

    if decision == "no":
        print("Goodbye!")
        repeat = True
        break
