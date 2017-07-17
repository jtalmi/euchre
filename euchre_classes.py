# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 13:53:20 2016

@author: talm
"""
import random

'''Global variables'''
suitlist = ["Clubs", "Spades", "Diamonds", "Hearts"]
ranklist = [None,None,"2","3","4","5","6","7","8","9", "10", "Jack", "Queen", "King", "Ace"]
bowers = {0:1, 1:0, 2:3, 3:2}
teams = {'p1': 'p3', 'p2': 'p4', 'p3': 'p1', 'p4': 'p1'}

class Card(object):
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 9-14
    """
    suitlist = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranklist = [None, None, "2","3","4","5","6","7","8","9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        #self.name = ranklist[self.rank],"of",suitlist[self.suit]
    
    def __str__(self):
        """Returns a string representation of this card."""
        return '%s of %s' % (ranklist[int(self.rank)], suitlist[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

class Deck(object):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        self.cards = []
        self.name = str(self)
        for suit in range(4):
            for rank in range(9, 15):
                self.cards.append(Card(suit, rank))
                self.cardlist = []
        self.cardlist = map(lambda x: str(x), self.cards)
        self.suits = [card.suit for card in self.cards]
        self.ranks = [card.rank for card in self.cards]

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)
        self.suits.append(card.suit)
        self.ranks.append(card.rank)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)
        self.suits.remove(card.suit)
        self.ranks.remove(card.rank)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        a = self.cards.pop(i)
        self.suits.remove(a.suit)
        self.ranks.remove(a.rank)
        return a
        
    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.cardlist = map(lambda x: str(x), self.cards)
        self.suits = [card.suit for card in self.cards]
        self.ranks = [card.rank for card in self.cards]

def next_player(player, players):
    """Function for cycling through players in a given trick"""
    if players.index(player) in range(0,3):
        player = players[players.index(player)+1]
    elif players.index(player) == 3:
        player = players[0]
    return player
        
def card_rank(trumpsuit,roundsuit):
    """Ranks cards based on the trump suit and the first card laid down (round suit)
        Trumps are ranked highest, followed by cards in the round suit, followed by all
        other cards in descending order. Offsuit cards with the same rank have equal value"""
    trumps = [Card(trumpsuit, 11), Card(bowers[trumpsuit], 11), Card(trumpsuit, 14),
    Card(trumpsuit,13), Card(trumpsuit,12), Card(trumpsuit,10), Card(trumpsuit,9)]
    rounds = [Card(roundsuit, 14), Card(roundsuit, 13),  Card(roundsuit, 12),  Card(roundsuit, 11),
    Card(roundsuit, 10), Card(roundsuit, 9)]
    ranking = dict((v,k) for k,v in dict(enumerate(trumps+rounds)).iteritems())
    offsuits = [i for i in range(4) if i not in [trumpsuit,roundsuit]]
    ranking.update({Card(offsuits[0], 14): 13, Card(offsuits[1],14): 13, Card(offsuits[0],13): 14,
                    Card(offsuits[1],13): 14, Card(offsuits[0],12): 15, Card(offsuits[1],12): 15,
                    Card(offsuits[1],11): 16, Card(offsuits[1],11): 16, Card(offsuits[0],10): 17,
                    Card(offsuits[1],10): 17, Card(offsuits[0],9): 18, Card(offsuits[1],9): 18})
    ranking[Card(bowers[trumpsuit], 11)] = 1
    #offsuits = [i for i in cardlist if i not in ranking.keys()]
    return ranking
    
def get_rank(card, ranking):
    '''Compares a single card against a rank ordering'''
    try:
        a = ranking.keys().index(card)
        return ranking[ranking.keys()[a]]
    except:
        pass

def get_playables(player, roundsuit):
    '''Returns a list of cards from a given hand that are playable in a trick. In euchre,
        the first card laid down in each trick determines the suit, and if subsequent players
        have a card in that suit, they must play that first'''
    cards = []
    if roundsuit in player.suits:
        for i,x in enumerate(player.cards):
            if x.suit == roundsuit:
                cards.append(x)
    else:
        cards = player.cards[:]
    return cards
    
def choose_card(player, player_names, dealer, players, roundsuit, trumpsuit, roundcards):
    '''Algorithm to optimize card selection in a given trick, based on the cards played so far. 
        The algorithm checks the rank of all the cards laid down so far in the trick. If the player's
        teammate is winning the trick, the player lays down the weakest of its playable cards.
        If the player's teammate is losing or hasn't played yet, the player checks if they have at least
        one card that can beat the others. If it does, it plays one of those cards, if it does not,
        it plays its weakest card'''
    player_name = player_names[players.index(player)]
    playables = get_playables(player, roundsuit)
    if roundsuit == None:
        card = random.choice(player.cards)
        roundsuit = card.suit
    else:
        ranking = card_rank(trumpsuit,roundsuit)
        ranks = map(lambda x: get_rank(x, ranking), playables)
        if get_rank(roundcards[teams[player_name]], ranking) == max(map(lambda x: get_rank(x, ranking),roundcards.values())):
            card = playables[ranks.index(min(ranks))]
        else:
            if max(ranks) > max(map(lambda x: get_rank(x, ranking), roundcards.values())):
                card = playables[ranks.index(max(ranks))]
            else:
                card = playables[ranks.index(min(ranks))]
    return card, roundsuit

def play_card(card, move, player, players, player_names, dealer, roundcards, game): 
    '''Based on card selected by choose_card, player plays card (moves it to dealer), and the
        trick and game history are recorded in the relevant locations'''
    player_name = player_names[players.index(player)]
    player.remove_card(card)
    dealer.add_card(card)
    roundcards.update({player_name: card})
    game.loc[move] = [card, card.suit, card.rank, player_name]
    return game

def play_trick(players, dealer, player_names, trumpsuit, move, winner, game):
    '''Cycles through the four moves in a given trick. Winner is set to None before the first trick
        so the player who goes first is randomly selected. All subsequent tricks are started by the winner
        of the previous trick.
        Returns: winner, game, move so that the function can be called for the next trick, and so that
        the game history can be updated.'''
    roundcards = {key: None for key in player_names}
    roundsuit = None
    if winner == None:
        player = players[random.randint(0,3)]
    else:
        player = players[player_names.index(winner)]
    for i in range(4):
        card, roundsuit = choose_card(player, player_names, dealer, players, roundsuit, trumpsuit, roundcards)
        game = play_card(card, move, player, players, player_names, dealer, roundcards, game)
        move += 1
        player = next_player(player, players)
    ranking = card_rank(trumpsuit, roundsuit)
    winner = roundcards.keys()[map(lambda x: get_rank(x,ranking), roundcards.values()).index(min(map(lambda x: get_rank(x,ranking), roundcards.values())))]
    return winner, game, move
    