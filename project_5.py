# silent Auction
import os
def find_winner(bidder_details): # jenny:10000, sai: 2000, jonathan: 100000
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:   #jenny
        bidding_price = bidder_details[bidder] #10000 # 2000
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(bidder_details)
    print(f"The winner is {winner} with a bid price of {highest_bid}")


bidder_data = {}
end_of_bidding = False

while not end_of_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidder_data[name] = price
    more_bidders = input("Are there more bidders? Type 'yes' or 'no' : ").lower()

    if more_bidders == 'no':
        find_winner(bidder_data)
        end_of_bidding=True
    elif more_bidders == 'yes':
        os.system("cls")