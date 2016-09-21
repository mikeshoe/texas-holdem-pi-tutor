'''
Created on Sep 14, 2016

@author: mike
'''

from app.cardvalue import CardValue

class Card(object):
    'Class that represents an individual playing card'
    
    def is_face(self):
        return self.cardValue in (CardValue.KING, CardValue.QUEEN, CardValue.JACK)
    
    def is_king(self):
        return self.cardValue == CardValue.KING
    
    def is_ace(self):
        return self.cardValue == CardValue.ACE

    def __init__(self, cardSuit, cardValue):
        self.cardSuit = cardSuit
        self.cardValue = cardValue
        
    def __eq__(self,other):
        return self.cardSuit == other.cardSuit and self.cardValue == other.cardValue
    
    def __str__(self):
        return self.cardValue + " of " +  self.cardSuit
