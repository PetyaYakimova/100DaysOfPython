def find_highest_bidder(bidding_dictionary):
    best_bid = 0
    best_bid_name = ""
    for key in bidding_dictionary:
        if bidding_dictionary[key] > best_bid:
            best_bid = bidding_dictionary[key]
            best_bid_name = key

    print(f"The winner is {best_bid_name} with bid of ${best_bid}.")


print("Welcome to the secret auction program!")

bids = {}
more_bidders = "yes"
while more_bidders == "yes":
    name = input("What is your name? ")
    bid = float(input("How much do you bid? $"))
    bids[name] = bid
    more_bidders = input("Are there more people to bid? type 'yes' or 'no'\n").lower()
    print("\n" * 100)

find_highest_bidder(bids)
