import os
from art import logo

print(logo)

bids = {}
commence_bidding = 'y'

while commence_bidding != 'n':
    name = str(input("Name: "))
    bid = int(input("Bid pride: $"))
    bids[name] = bid

    commence_bidding = str(
        input("Are there other users who would like to bid? y/n"))

    if commence_bidding == 'y':
        os.system('clear')
    elif commence_bidding == 'n':
        winner = max(bids, key=bids.get)
        print("The winner is " + winner +
              " with the highest bid of $" + bids[winner])
