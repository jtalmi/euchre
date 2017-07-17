# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 13:41:47 2016

@author: talm
"""

import random
import pandas as pd
import numpy as np
from euchre_classes import *

'''Set up the game by generating a deck, dealing 5 cards to each player, and dealing the remainder to the dealer'''
deck = Deck()
deck.shuffle()
p1, p2, p3, p4, dealer = Hand(), Hand(), Hand(), Hand(), Hand()
players = [p1,p2,p3,p4]
player_names = ['p1','p2','p3','p4']
for i in range(4):
    deck.move_cards(players[i],5)
deck.move_cards(dealer, 4)
tricks = {name: 0 for name in player_names[:]}
game = pd.DataFrame(np.nan, index = range(1, 21), columns = ['card', 'suit','rank','player'])
trumpsuit = random.randint(0,3)
move = 1
winner = None

for i in range(5):
    winner = play_trick(players, dealer, player_names, trumpsuit, move, winner, game)
    tricks[winner] +=1
    
if tricks['p1'] + tricks['p3'] > tricks['p2'] + tricks['p4']:
    print "Players 1 and 3 win"
else:
    print "Players 2 and 4 win"
    
'''
#Round 1
roundcards = {key: None for key in player_names}
roundsuit = None
player = players[random.randint(0,3)]
for i in range(4):
    card, roundsuit = choose_card(player, dealer, players, roundsuit, trumpsuit, roundcards)
    play(card, move, player, players, dealer, roundcards, game)
    move += 1
    player = next_player(player, players)
ranking = deck_rank(trumpsuit, roundsuit)
winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
tricks[winner] +=1

#Round 2
roundcards = {key: None for key in player_names}
roundsuit = None
player = players[player_names.index(winner)]
for i in range(4):
    card, roundsuit = choose_card(player, dealer, players, roundsuit, trumpsuit, roundcards)
    play(card, move, player, players, dealer, roundcards, game)
    move += 1
    player = next_player(player, players)
ranking = deck_rank(trumpsuit, roundsuit)
winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
tricks[winner] +=1

#Round 3
roundcards = {key: None for key in player_names}
roundsuit = None
player = players[player_names.index(winner)]
for i in range(4):
    card, roundsuit = choose_card(player, dealer, players, roundsuit, trumpsuit, roundcards)
    play(card, move, player, players, dealer, roundcards, game)
    move += 1
    player = next_player(player, players)
ranking = deck_rank(trumpsuit, roundsuit)
winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
tricks[winner] +=1

#Round 4
roundcards = {key: None for key in player_names}
roundsuit = None
player = players[player_names.index(winner)]
for i in range(4):
    card, roundsuit = choose_card(player, dealer, players, roundsuit, trumpsuit, roundcards)
    play(card, move, player, players, dealer, roundcards, game)
    move += 1
    player = next_player(player, players)
ranking = deck_rank(trumpsuit, roundsuit)
winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
tricks[winner] +=1

#Round 5
roundcards = {key: None for key in player_names}
roundsuit = None
player = players[player_names.index(winner)]
for i in range(4):
    card, roundsuit = choose_card(player, dealer, players, roundsuit, trumpsuit, roundcards)
    play(card, move, player, players, dealer, roundcards, game)
    move += 1
    player = next_player(player, players)
ranking = deck_rank(trumpsuit, roundsuit)
winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
tricks[winner] +=1

#Score
team1 = tricks['p1'] + tricks['p3']
team2 = tricks['p2'] + tricks['p4']
if team1>team2:
    print "Players 1 and 3 win"
else:
    print "Players 2 and 4 win"

testf
roundsuit = card.suit
ranking = ranking(trumpsuit, roundsuit)
dealer.add_card(card)
game.loc[move] = [card, card.suit, card.rank, 'p1']
roundcards['1'] = card

#P2's move
player = next_player(player, players)
move +=1
player_name = player_names[players.index(player)]


    
ranks = map(lambda x: get_rank(x), playables)

roundsuit = None


def playables(player, roundsuit):
    playables = []
    if roundsuit in player.suits:
        for i,x in enumerate(player.cards):
            if x.suit == roundsuit:
                playables.append(x)
    else:
        playables = player.cards[:]
    return playables
    
def play(player, move, roundsuit, trumpsuit, roundcards):
    player_name = player_names[players.index(player)]
    playables = playables(player,roundsuit)
    if roundsuit == None:
        card = random.choice(player.cards)
        roundsuit = card.suit
    else:
        ranking = ranking(trumpsuit,roundsuit)        
        if get_rank(roundcards[teams[player_name]], ranking) == max(lambda x: get_rank(roundcards.values(),ranking)):
            card = playables[playables.index(min(ranks))]
        else:
            if max(ranks) > max(map(lambda x: get_rank(x, ranking), roundcards.values)):
                card = playables[playables.index(max(ranks))]
            else:
                card = playables[playables.index(min(ranks))]
    player.remove_card(card)
    dealer.add_card(card)
    roundcards.update({player_name: card})
    game.loc[move] = [card, card.suit, card.rank, player_name]
    move += 1
    player = next_player(player)



    dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
        
card = player.pop_card(playables[playables.index(min(alist))])


    playables = playables + player.cards
    alist = map(lambda x: get_rank(x), playables)
    if max(alist) > max(map(lambda x: get_rank(x), roundcards.values)):
        card = player.pop_card(playables[playables.index(max(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    else:
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
        


#P3's move
playables = []
player = next_player(player, players)
move +=1
player_name = player_names[players.index(player)]
if roundsuit in player.suits:
    for i,x in enumerate(player.cards):
        if x.suit == roundsuit:
            playables.append(x)
    alist = map(lambda x: get_rank(x), playables)
    if get_rank(roundcards[teams[player_name]]) == max(lambda x: get_rank(roundcards.values())):
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    elif max(alist) > max(map(lambda x: get_rank(x), roundcards.values)):
        card = player.pop_card(playables[playables.index(max(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    else:
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
else:
    playables = playables + player.cards
    alist = map(lambda x: get_rank(x), playables)
    if max(alist) > max(map(lambda x: get_rank(x), roundcards.values)):
        card = player.pop_card(playables[playables.index(max(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    else:
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]  
        
#P4's move
playables = []
player = next_player(player, players)
move +=1
player_name = player_names[players.index(player)]
if roundsuit in player.suits:
    for i,x in enumerate(player.cards):
        if x.suit == roundsuit:
            playables.append(x)
    alist = map(lambda x: get_rank(x), playables)
    if get_rank(roundcards[teams[player_name]]) == max(lambda x: get_rank(roundcards.values())):
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    elif max(alist) > max(map(lambda x: get_rank(x), roundcards.values)):
        card = player.pop_card(playables[playables.index(max(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    else:
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
else:
    playables = playables + player.cards
    alist = map(lambda x: get_rank(x), playables)
    if max(alist) > max(map(lambda x: get_rank(x), roundcards.values)):
        card = player.pop_card(playables[playables.index(max(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]
    else:
        card = player.pop_card(playables[playables.index(min(alist))])
        dealer.add_card(card)
        roundcards.update({player_name: card})
        game.loc[move] = [card, card.suit, card.rank, player_name]  
        
#Next trick

def next_player(player, players):
    if players.index[player] in range(0,3):
        player = players[players.index(player)+1]
    elif players.index[player] == 3:
        player = players[0]
    return player
        
def ranking(trumpsuit,roundsuit):
    trumps = [Card(trumpsuit, 11), Card(bowers[trumpsuit], 11), Card(trumpsuit, 14),
    Card(trumpsuit,13), Card(trumpsuit,12), Card(trumpsuit,10), Card(trumpsuit,9)]
    rounds = [Card(roundsuit, 14), Card(roundsuit, 13),  Card(roundsuit, 12),  Card(roundsuit, 11),
    Card(roundsuit, 10), Card(roundsuit, 9)]
    offsuits = [i for i in test if i not in [trumpsuit,roundsuit]]
    ranking = trumps + rounds
    for i in reversed(range(9,14)):
        ranking.append([Card(offsuits[0],i),Card(offsuits[1])])
    return ranking
    
def get_rank(card, ranking):
    if card == None:
        pass
    else:
        for i in ranking[:]:
            if i < 13:
                if i == card:
                    return ranking.index(i)
            else:
                if i[0] == card:
                    return ranking.index(i)
                elif i[1] == card:
                    return ranking.index(i)
            
            
    
    
    for i in range(len(cardlist)):
        card = cardlist[i]
        if card.suit == trumpsuit:
            
            cardlist.insert(i+6,cardlist.pop(i))
    return cardlist

test = cardlist[:]

map(lambda x: str(x), test)
           
testf

dealer.add_card(p2.pop_card())


        
            
alist = deck.cards
    
    

p1.play()

play(history, action)

def play(history, round_suit):
    if round_suit != "":
        player.suits = map(lambda x: x.suit, player.cards)
        x = []    
        for i in range(len(player.cards)):
            a = player.suits[i]
            if a == round_suit:
                x += i
        if x != []:
            a = random.choice(x)
        else:
            a = random.randint(0,len(player.cards)-1)
        card = player.cards[a]
        player.play(card)
    if round_suit == "":
        x = random.randint(0,len(player.cards)-1)
        card = player.cards[x]
        round_suit = card.suit
        player.play(card)
    return player, card

round_suit = ""

for i in range(5):
    j=0
    for name in player_names[:4]:
        j+=1
        x = eval(name)
        x, card = f(x, round_suit)
        game.ix[i*4+j-1,[name, 'total']] = card

round_suit = ""

game.suit = game.total.map(lambda x: x.suit)

testf



players = {"p" + str(i): Hand() for i in range(1,5)}
players.update({"dealer": Hand()})

for player in players.iterkeys():
    if player == "dealer":
        deck.move_cards(players[player],4)
    else:
        deck.move_cards(players[player], 5)
'''
'''
for i in range(len(players)):
    x = player[i].cards
    y = map(lambda x: x.suit, x)
    z = dict(zip(range(4), [0,0,0,0]))
    for i in z.iterkeys():
        z[i] = y.count(i)
    
    n = str(player)
    n
    
def play(hand, card):
    
    
    
    x = game.total[game.total.isnull()==False].index
        
    if round_suit in hand.suits.keys():
        card = hand.tolist()
    
    
#dict(lambda z.count(i) for i in range(4) ))

#Round 1
player_init = eval(player_names[random.randint(0,3)])
card_init = random.randint(0,4)
suit_init = player_init.cards[card_init].suit
rank_init = player_init.cards[card_init].rank
player_init.play(player_init.cards[card_init])

x.cards()
 



for i in range(4):
    j = [0, 4, 8, 12, 16]
    f = lambda x: x + 1
    j = map(f, j)
    player = "p" + str(i+1)
    cards = eval(player).cards
    game.ix[j,player]= pd.Series(cards)
    dealer.cards.append(cards)
    game.ix[j,'total'] = cards
    game.ix[j,'suit'] = game.ix[j,'total'].map(lambda x: x.suit)
    game.ix[j, 'rank'] = game.ix[j, 'total'].map(lambda x: x.rank)

round_suit = int(game.suit[0])

def ranking(rank, round_suit, trump):
    rank['Jack of ' + trump] = 1
    if trump == "Hearts" or trump == "Diamonds":
        if trump == "Hearts":
            rank['Jack of Diamonds'] = 2
        else:
            rank['Jack of Hearts'] = 2
    if trump == "Clubs" or trump == "Spades":
        if trump == "Clubs":
            rank['Jack of Spades'] = 2
        else:
            rank['Jack of Clubs'] = 2

    rank['Ace of ' + trump] = 3
    rank['King of ' + trump] = 4
    rank['Queen of ' + trump] = 5
    rank['10 of ' + trump] = 6
    rank['9 of ' + trump] = 7
    rank['Ace of ' + suit_names[round_suit]] = 8
    rank['King of ' + suit_names[round_suit]] = 9
    rank['Queen of ' + suit_names[round_suit]] = 10
    rank['10 of ' + suit_names[round_suit]] = 11
    rank['9 of ' + suit_names[round_suit]] = 12
    for key in rank.iterkeys():
        if trump not in key:
            if suit_names[round_suit] not in key:
                rank[key] = 13
    return rank


for i in range(4):
    game.points[i] = rank[str(game.total[i])'''