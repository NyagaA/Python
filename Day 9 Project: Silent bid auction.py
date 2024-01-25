                                                        # SILENT BID AUCTION
# PROGRAM 1

from art import logo

print(logo)

bidders = {}
bidding_active = True

while bidding_active:
    name = input("What is your name? ").upper()
    bid = float(input("What is your bid? $"))

    # Add a new bid entry to the dictionary
    bidders[name] = bid
    

    another_bidder = input("Is there another bidder? Type 'yes' or 'no': ").lower()

    if another_bidder != 'yes':
        bidding_active = False    # "break" can also be used to exit the loop if the user enters anything other than 'yes'
        
# Find the highest bidder
# compares the values in the bidders dictionary and returns the key (bidder's name) associated with the maximum value (highest bid). 
highest_bidder = max(bidders, key=bidders.get)

# Retrieve the bid using the highest bidder's name
highest_bid = bidders[highest_bidder]

# Output the results
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")

# PROGRAM 2

from art import logo
print(logo)

bids = {}
bidding_active = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_active:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_active = False

# Call the function to find the highest bidder outside the while loop
find_highest_bidder(bids)
