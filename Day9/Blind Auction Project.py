from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
dict = {}
def highest_bider(bids_dict):
    highest_bid= 0
    winner =""
    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with ${highest_bid}")
# TODO-3: Whether if new bids need to be added
countinue_bid = True
while countinue_bid :
    name = input("what is your name? :")
    bid = int(input("what is your Bid :$"))
    dict[name]=bid
    should_countinue = input("is there any biders left? type yes/no\n").lower()
    if should_countinue == "no":
        countinue_bid = False
        highest_bider(dict)
    elif  should_countinue == "yes":
        print("\n" * 20)

# TODO-4: Compare bids in dictionary



