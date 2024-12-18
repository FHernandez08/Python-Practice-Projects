# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def compare_bids(bidding_dict):
    winner = ""
    higgest_bid = 0

    max(bidding_dict)

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > higgest_bid:
            higgest_bid = bid_amount
            winner = bidder

    print(f"The winner is {bidder} with a bid of {higgest_bid}.")

current_bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    current_bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        continue_bidding = False
        compare_bids(current_bids)
    elif should_continue == "yes":
        print("\n" * 20)
