import random
from art import logo

def play_blackjack():

    # check for black jack condition in deck
    def blackjack_check(u_score, c_score):
        if u_score == 21 and c_score == 21:
            print("It's a draw with Blackjacks!")
            return True
        elif u_score == 21:
            print("Blackjack! You win!")
            return True
        elif c_score == 21:
            print("Computer has Blackjack. You lose.")
            return True
        return False

    # If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
    def ace_check(deck):
        score = sum(deck)
        for i in range(len(deck)):
            if deck[i] == 11 and score > 21:
                deck[i] = 1
                score = sum(deck)
        return deck

    # to get more cards from the deck
    def more_card(u_deck):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        u_deck.append(random.choice(cards))

        # checks if an ace was found
        u_deck = ace_check(u_deck)
        u_score = sum(u_deck)
        return u_deck, u_score

    def game_conditions(u_score, c_score):

        if c_score > 21:
            print("\nOpponent went over. You win 😁")

        elif u_score > c_score:
            print("\nYou win")

        elif u_score < c_score:
            print("\nYou Lost 😭")

        elif u_score == c_score:
            print("\nIts a draw")

        return True

    replay = True

    while replay:
        print("\n"*10)
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        game_over = False
        while not game_over:

            # assign two cards to user and computer
            user_deck = random.choices(cards, k=2)
            computer_deck = random.choices(cards, k=2)

            # calculates the scores
            user_score = sum(user_deck)
            computer_score = sum(computer_deck)

            print(f"\tYour cards: {user_deck}, current score: {user_score}")
            print(f"\tComputer's first card: {computer_deck[0]}")

            # if any one have blackjack then its Gameover
            game_over = blackjack_check(user_score, computer_score)
            if game_over:
                break

            # checks if user score is less than 21
            userscore_less_than_21 = True
            while userscore_less_than_21:

                # if user score is less than 21 than ask if they need another card
                if user_score < 21:
                    new_card = input("\nType 'y' to get another card, type 'n' to pass:  ").lower()

                    if new_card == "y":
                        user_deck, user_score = more_card(user_deck)

                        print(f"\n\tYour cards: {user_deck}, current score: {user_score}")
                        print(f"\tComputer's First Card: {computer_deck[0]}")
                    else:
                        userscore_less_than_21 = False
                else:
                    userscore_less_than_21 = False

            if user_score > 21:
                print("# You went over. You lose 😭")
                game_over = True
                break

            else:
                computer_deck = ace_check(computer_deck)
                computer_score = sum(computer_deck)

                computerscore_less_than_17 = True
                while computerscore_less_than_17:
                    if computer_score < 17:
                        computer_deck, computer_score = more_card(computer_deck)
                    else:
                        computerscore_less_than_17 = False

            print(f"\n\tYour Final Hand: {user_deck}, Final score: {user_score}")
            print(f"\tComputer's Final Hand: {computer_deck}, Final score: {computer_score}")

            # results for the black jack game
            game_over = game_conditions(user_score, computer_score)

        replay = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if replay == "n":
            replay = False
        else:
            replay = True


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
    play_blackjack()
else:
    print("GoodBye")

