from os import system
import art

print(art.logo)
#system('cls') # it is clear screen
# print("\n" * 20) or that could be

# TODO-1: Ask the user for input
# name = input("What is your name?")
# price = int(input("What is your bid?"))
# bids = {}
# TODO-2: Save data into dictionary {name : price}
# bids[name] = price
# TODO-3: Whether if new bids need to be added
# should_continue = input("Are there any other bidders?")
# TODO-4: Compare bids in dictionary
# highest_bidder = max(bids, key=bids.get) --> or write own function






bids = {}
# try to solve more question with finding the biggest in list,dict,tupple
def find_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


cont = True
while cont:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        cont = False
        find_highest_bid(bids)
    else:
        system('cls')