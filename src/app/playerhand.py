'''
Created on Sep 16, 2016

@author: mike
'''

from app.card import Card
from app.cardvalue import CardValue

class PlayerHand(object):
    'Class that represents a single players hand (hole cards)'
   

    def __init__(self):
        self.holeCards = []
        
    def add_hole_card(self, card):
        if self.num_hole_cards() < 2:
            if self.holeCards.count(card) == 0:
                self.holeCards.append(card)
            else:
                raise Exception("Hole cards must be different")
        else:
            raise Exception("A player is limited to 2 hole cards")
        
    def num_hole_cards(self):
        return len(self.holeCards)
    
    def is_pocket_rockets(self):
        for card in self.holeCards:
            if card.cardValue is not CardValue.ACE:
                return False
        return True
        
    
        