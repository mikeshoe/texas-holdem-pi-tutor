'''
Created on Sep 14, 2016

@author: mike
'''
from app.card import Card
from app.cardsuit import CardSuit
from app.cardvalue import CardValue
from random import randint

class Deck(object):
    'Class that represents a deck of playing cards'
  
    'class variable lists containing card suits and values'
    cardSuitList = [CardSuit.CLUB, CardSuit.DIAMOND, CardSuit.HEART, CardSuit.SPADE]
    cardValueList = [CardValue.ACE, CardValue.KING, CardValue.QUEEN, CardValue.JACK, CardValue.TEN, CardValue.NINE, CardValue.EIGHT, CardValue.SEVEN, CardValue.SIX, CardValue.FIVE, CardValue.FOUR, CardValue.THREE, CardValue.TWO]
    
    
    def __init__(self):
        self
        self.cards = []
        self.__load_cards__()
        self.__shuffle_cards__()

    def is_shuffled(self):
        return False
    
    'Retrieves and removes element [0] card from deck'
    def draw_card(self):
        return self.cards.pop(0)
    
    'Returns number of cards remaining in the deck'
    def num_cards_remaining(self):
        return len(self.cards)
    
    'Removes Card from deck so it cannot be part of flop, turn, or river'
    def remove_card_from_deck(self, card):
        pass
    
    'Loads deck unshuffled with 52 playing cards'
    def __load_cards__(self):
        for cardSuit in self.cardSuitList:
            for cardValue in self.cardValueList:
                card = Card(cardSuit, cardValue)
                'print "Card: %s" % card'
                self.cards.append(card)
    
    'loop through cards list in order 0...51 and swap current card with a card in random position in deck'                    
    def __shuffle_cards__(self):
        for x in range(0,51):
            swap_index = randint(0,51)
            loop_card = self.cards.pop(x)
            swap_card = self.cards.pop(swap_index-1) 
            self.cards.insert(x, swap_card)
            self.cards.insert(swap_index, loop_card)
            
            
            
            
        
        

