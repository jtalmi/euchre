# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 13:41:47 2016

@author: talm
"""

import random
import pandas as pd
import numpy as np
from euchre_classes import *
import json

'''Game setup:
- Generate a euchre deck, 5 player hands, and 1 dealer hand
- Shuffle deck and deal 5 cards to each player and the remainder to the dealer
- Create tricks dictionary which stores points scored in each trick, and game dataframe
  which stores game history
- Randomly select trump suit '''
deck = Deck()
deck.shuffle()
p1, p2, p3, p4, dealer = Hand(), Hand(), Hand(), Hand(), Hand()
players = [p1,p2,p3,p4]
player_names = ['p1','p2','p3','p4']
for i in range(4):
    deck.move_cards(players[i],5)
deck.move_cards(dealer, 4)
tricks = {name: 0 for name in player_names[:]}
game = pd.DataFrame(np.nan, index = range(1, 21), columns = ['card','suit','rank','player'])
trumpsuit = random.randint(0,3)
move = 1 
winner = None

'''Play 5 tricks to complete a full game'''
for i in range(5):
    winner, game, move = play_trick(players, dealer, player_names, trumpsuit, move, winner, game)
    tricks[winner] +=1
    
'''Print the winning team
if tricks['p1'] + tricks['p3'] > tricks['p2'] + tricks['p4']:
    print "Players 1 and 3 win"
else:
    print "Players 2 and 4 win"
'''

'''Create a dictionary to store results'''
adict = {i: None for i in range(1,20)}
for i in adict.iterkeys():
    adict[i] = game.loc[i].to_dict()
    adict[i].pop('card')
adict['trump'] = trumpsuit
adict = json.dumps(adict, sort_keys=True)

with open("results.csv", "a") as file:
    file.write(adict+"\n")

'''
with open("results.csv",'r') as file:
    test = file.readlines()
a = map(lambda x: json.loads(x), test)
'''

test1 = test[0]



