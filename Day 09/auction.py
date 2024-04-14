import os
from art import logo

auction_dic = {}

print(logo)
print("Welcome to the secret auction program.")

highest_bidder = []

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: "))
    auction_dic[name] = bid

    more_bidders = input("Are there any more bidders? Type 'Yes' or 'No': ").lower()
    if more_bidders == "no":
        highest_bid = max(auction_dic.values())

        # Find all bidders with the highest bid
        for bidder, bid in auction_dic.items():
            if bid == highest_bid:
                highest_bidder.append(bidder)

        if len(highest_bidder) == 1:
            print(
                f"The highest bidder is {highest_bidder[0]} with a bid of ${highest_bid}."
            )
        else:
            print(
                f"The highest bidders are {', '.join(highest_bidder)} each with a bid of ${highest_bid}."
            )
        break
    elif more_bidders == "yes":
        os.system("cls")
