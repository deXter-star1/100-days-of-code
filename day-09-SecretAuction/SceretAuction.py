
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print((f"The winner is {winner} with a bid of ${highest_bid}."))

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dictionary ={}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dictionary[name] = bid
    yes_or_no = input("Are there any other users? Type 'Yes' or 'No'.\n").lower()
    if yes_or_no == "no":
        continue_bidding = False
        find_highest_bidder(dictionary)
    elif yes_or_no == "yes":
        print("\n" * 100)







