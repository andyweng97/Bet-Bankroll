# Bet-Bankroll
Gives you how much of your bankroll you should bet given that you know the odds. 

Uses the Kelly critereon to give you the optimal % of your bankroll that you should bet on a binary bet, given you know the odds and the probability of winning.

First, set the odds and the probability of winning in the python file. 

Then call it using a command line arg in the form of:
Python KellyCritereonSimulator.py numberOfTrials numberOfBetsPerTrial

It will return to you the percentage of your bankroll you should bet with each bet, followed by the avg amount of money you end up with assuming you start with 1000.
