# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:24:52 2021

@author: 13072
"""

import random

suits = {"clubs":1, "diamonds":2, "hearts":3,"spades":4}
ranks = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10
        ,"jack":11,"queen":12,"king":13,"ace":14}


def flushCheck(x):
    flush = True
    for card in x:
        if card.suit != x[0].suit:
            flush = False
    return flush
def pairCheck(x):
    n = 0
    for i in range(5):
        for j in range(5):
            if i>j and x[i].rank == x[j].rank:
                n = n+1
    return n
                
                

class Card:
    def __init__(self,rank,suit):3  
        self.rank = rank
        self.suit = suit 
        
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def getValue(self):
        return (4*ranks[self.rank] + suits[self.suit])
    def cardName(self):
        return str(self.rank)  + " of " + str(self.suit)
    def showCard(self):
        print (self.cardName())
        
class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks.keys():
            for suit in suits.keys():
                self.cards.append(Card(rank,suit) )
    def showDeck(self):
        for card in self.cards:
            card.showCard()
    def shuffle(self):
        random.shuffle(self.cards)
    def dealCard(self):
        return self.cards.pop()
    def deckSize(self):
        return len(self)

class Hand:
    def __init__(self,deck):
        self.hand = []
        for i in range(5):
            self.hand.append(deck.dealCard())
    def sortHand(self):
        self.hand.sort(key = lambda card: card.getValue())
    def showHand(self):
        x = []
        for card in self.hand:
            x.append(card.cardName())
        print (x)
    def getCard(self,i):
        return self.hand[i]
    def handValue(self):
        y = self
        y.sortHand()
        x = y.hand
        if ranks[x[0].rank]==ranks[x[4].rank]+4 and flushCheck(x) and x[4].rank == "ace":
            return 9
        elif ranks[x[4].rank]+4==ranks[x[0].rank] and flushCheck(x):
            return 8
        elif ranks[x[4].rank]+4==ranks[x[0].rank]:
            return 4
        elif flushCheck(x):
            return 5
        elif x[0].rank == x[3].rank:
            return 7
        elif (x[0].rank == x[2].rank and x[3].rank == x[4].rank) or (x[0].rank == x[1].rank and x[2].rank == x[4].rank):
            return 6
        elif x[0].rank == x[2].rank or x[1].rank == x[3].rank or x[2].rank== x[4].rank:
            return 3
        elif pairCheck(x)==2:
            return 2
        elif pairCheck(x)==1:
            return 1
        else:
            return 0
        

            
        
        


def compareCards(card1,card2):
    if suits[card1.suit] > suits[card2.suit]:
        return True
    elif suits[card1.suit] < suits[card2.suit]:
        return False
    else:
        if ranks[card1.rank] > ranks[card2.rank]:
            return True
        else:
            return True
        



# def dealFlush():
#     hand = []
#     for i in range(3):
#         hand.append(Card(i+2,"clubs"))
#     hand.append(Card(7,"diamonds"))
#     return hand

# x = dealFlush()

# print (flushCheck(x))


x = "yes"
while x == "yes":   
    deck1 = Deck()
    deck1.showDeck()
    deck1.shuffle()
    print ("___ _______   _")
    hand1 = Hand(deck1)
    print ("blahhhhhhhhhhhhhh")
    hand1.showHand()
    hand1.sortHand()
    hand1.showHand()
    print(hand1.handValue())
    if hand1.handValue() >=2:
        x = input("would you like to continue: ")
    
