'''
Created on Sep 14, 2016

@author: mike
'''

from app.cardvalue import CardValue
from app.cardsuit import CardSuit

class Card(object):
    'Class that represents an individual playing card'

    def is_two(self):
        return self.cardValue == CardValue.TWO
    
    def is_seven(self):
        return self.cardValue == CardValue.SEVEN

    def is_eight(self):
        return self.cardValue == CardValue.EIGHT
        
    def is_face(self):
        return self.cardValue in (CardValue.KING, CardValue.QUEEN, CardValue.JACK)
    
    def is_king(self):
        return self.cardValue == CardValue.KING
    
    def is_ace(self):
        return self.cardValue == CardValue.ACE
    
    def is_suited(self, card):
        return self.cardSuit == card.cardSuit
    
    def is_connected(self, card):
        cardValueList = (CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE, CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE)
    
        myindex = cardValueList.index(self.cardValue)
        otherindex = cardValueList.index(card.cardValue)
    
        result = myindex - otherindex
        
        'connected cards will be next to one another in the cardValueList'
        if result >= -1 and result <= 1:
            return True
        else:
            return False
    

    def __init__(self, cardSuit, cardValue):
        self.cardSuit = cardSuit
        self.cardValue = cardValue
        
    def __eq__(self,other):
        return self.cardSuit == other.cardSuit and self.cardValue == other.cardValue
    
    def __str__(self):
        return self.cardValue + " of " +  self.cardSuit
