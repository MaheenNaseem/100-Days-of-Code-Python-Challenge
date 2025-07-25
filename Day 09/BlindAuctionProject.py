from art import logo
from collections import Counter
print(logo)

auction_data = {}
more_bids = False

while not more_bids:
    name= input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
  
    temporary_holder = {name:bid}
    #adds the key, value pair in auction data dict
    auction_data[name] = temporary_holder[name]
    #for looping
    new_person = input("Are there any other bidders? Type 'yes or 'no'.")

    if new_person == 'yes':
        print("\n"*20)
    else:
        #breaks loop
        more_bids = True

#using the max function on dict will return the highest bid among the bidders
highest_bid = max(auction_data.values())
winner = ""

#for winner selection use for loop and 
for key, value in auction_data.items():
    #if the value and max bid matched, it will be the winner
    if value == highest_bid:
        winner = key.capitalize()

"""
# TODO: Handle cases where multiple bids have the same highest amount (tie condition)

value_counts = Counter(auction_data.values())
duplicate_values = [value for value, count in value_counts.items() if count > 1]
print(f"Duplicate values: {duplicate_values}")

duplicate_counter = len(duplicate_values)
if duplicate_values > 0:

# select the first bidder
"""
print(f"\nThe winner is {winner} with a bid of ${highest_bid}")

