print("Starting Now")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print("You walk straight into the forest and see two paths which one are you choosing?")

#first choice left or right
choice_1 = input("Right or Left\n"
                 "")

if choice_1.capitalize()=="Right":
    print("You're Stuck in QuickSand! \nGAME OVER!")
elif choice_1.capitalize()=="Left":

    #choice_2
    print("\nYou saw rune hidden under the leaves.Are you picking it up or letting it go?")
    choice_2 = input("P for Pick Up, L for Let go\n")
    if choice_2.capitalize()=="P":
        print("Item added in Backpack\n")
    else:
        print("There's no going back now!\n")

    #choice 3
    print("You smell the salt air around you,Following the smell you found Sea!\nYou are a good swimmer, would you swim to cross the river or build a raft with the materials scatter along the seaside? ")
    choice_3= input("Swim or Build\n")
    if choice_3.capitalize()=="Swim":
        print('''     
         .-;':':'-.
        {'.'.'.'.'.}
         )        '`.
        '-. ._ ,_.-='
          `). ( `);(
          ('. .)(,'.)
           ) ( ,').(
          ( .').'(').
          .) (' ).('
           '  ) (  ).
            .'( .)'
              .).
              ''')
        print("You were Killed By a JellyFish!\nGAME OVER!")
    elif choice_3.capitalize()=="Build":
        print('''
                                  \   O,
                        \___________\/ )_________/
            ~~~~~~~~~~~~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        print("You have built a raft and can travel safely!\n")

        print('You row the boat into the cave and saw the pedestal made of stone.'
              '\n\nOn it was an inscription that said'
              '"Put what you have Picked on the way here"'
              'The empty space was as same as the rune you saw in the forest')

        #choice 4
        choice_4=input("\nDid you Picked Up the Rune? (Yes or No)\n")
        if choice_4.capitalize()=="Yes":
            if choice_2.capitalize()=="P":
                print('''\nYou had picked up the Rune!\nAs you placed the rune on the pedestal, The stones of the cave moved to reveal you it's treasure''')
                print('''
                                    _.--.
                                _.-'_:-'||
                            _.-'_.-::::'||
                       _.-:'_.-::::::'  ||
                     .'`-.-:::::::'     ||
                    /.'`;|:::::::'      ||_
                   ||   ||::::::'     _.;._'-._
                   ||   ||:::::'  _.-!oo @.!-._'-.
                   \'.  ||:::::.-!()oo @!()@.-'_.|
                    '.'-;|:.-'.&$@.& ()$%-'o.'-.||
                      `>'-.!@%()@'@_%-'_.-o _.|'||
                       ||-._'-.@.-'_.-' _.-o  |'||
                       ||=[ '-._.-\o/.-'    o |'||
                       || '-.]=|| |'|      o  |'||
                       ||      || |'|        _| ';
                       ||      || |'|    _.-'_.-'
                       |'-._   || |'|_.-'_.-'
                       '-._'-.|| |' `_.-'
                            '-.||_/.-'
                ''')
                print("Congratulations!!! You found the Hidden treasure")
            if choice_2.capitalize() == "L":
                print('''
                              (         (
                               )      (
                             )          )
                            (          ( ,
                           _ _)_      .-Y.
                .--._ _.--'.',T.\_.--' (_)`.
              .'_.   `  _.'  `-'    __._.--;
             /.'  `.  -'     ___.--' ,--.  :       
            : |  xX|       ,'  .-'`.(   |  '      
           :  `.  .'    ._'-,  \   | \  ||/       
          .;    `'    ,',\|\|   \  |  `.;'     
          ;           |   ` `    \.'|\\ :      
         .'           ` /|,         `|\\ \       
         :             \`/|,-.       `|\\ :        
         :        _     \`/  |   _   .^.'\ \         
         `;      --`-.   \`._| ,' \  |  \ : \           
          :.      .---\   \   ,'   | '   \ : .          
           :.        __\   `. :    | `-.-',  :               
           `:.     -'   `.   `.`---'__.--'  /
            `:         __.\    `---'      _'
             `:.     -'    `.       __.--'
              `:.          __`--.--'|
                 `:.      --'     __   `.
                ''')
                print("You Lied and for that you were fed to the Dragon.\nGAME OVER!")
        elif choice_4.capitalize()=="No":
            print("YOU LOSE!\nYou Don't have the rune so you can't enter the cave where the treasure resides")
