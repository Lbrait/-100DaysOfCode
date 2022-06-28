import os


def findmaxbid(bidding):
    hb = 0
    for bidder in bidding:
        bidamount = bidding[bidder]
        if bidamount > hb:
            hb = bidamount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${hb}')


def clear():
    print('\n' * 50)


bids = {}
print('Welcome to the secret auction program.')
while True:
    name = str(input('What is your name? '))
    bid = float(input('Whats your bid?: $'))
    bids[name] = bid
    flag = str(input('Are there any other bidders?[Y/N]: ')).upper()[0]
    if flag == 'Y':
        clear()
    else:
        break
findmaxbid(bids)
