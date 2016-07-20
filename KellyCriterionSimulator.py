import random
import sys

#Set your values here
odds = 1
probW = 0.51

probL = 1 - probW
mult = ((odds*probW)-probL)/odds


#Simulates a betting simluation with x bets
def simulate(x):
    bankroll = 1000
    for i in range(x):
        roll = random.random()

        bet = bankroll * mult
        if roll<probW:
            bankroll += bet*odds
        else:
            bankroll -= bet
    return bankroll

bets = []
tot = 0

for i in range(sys.argv[1]):
    x = (simulate(sys.argv[2]))
    bets.append(x)
    tot += x

print(mult + " " + tot/len(bets))

