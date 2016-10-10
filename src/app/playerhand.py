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
            'cannot add the same the same card twice'
            if self.holeCards.count(card) == 0:
                self.holeCards.append(card)
            else:
                raise Exception("Hole cards must be different")
        else:
            raise Exception("A player is limited to 2 hole cards")
        
    def num_hole_cards(self):
        return len(self.holeCards)
    
    'Pocket Rocks is the term used to describe having a pair of aces'
    def is_pocket_rockets(self):
        if False == self.is_pair():
            return False
        
        for card in self.holeCards:
            if card.cardValue is not CardValue.ACE:
                return False
        return True
    
    def is_pair(self):
            if len(self.holeCards) != 2:
                return False
            else:
                'Pairs have the same card value'
                return self.holeCards[0].cardValue == self.holeCards[1].cardValue
            
    'A pair of face cards (kings, queens, jacks)'         
    def is_face_pair(self):
        return self.is_pair() and self.holeCards[0].is_face() == self.holeCards[1].is_face()
    
    'Big slick is the term used to describe having one ace and one king.  Suit does not matter.' 
    def is_big_slick(self):
        if len(self.holeCards) != 2:
            return False
        else:
            return self.holeCards[0].is_ace() and self.holeCards[1].is_king() or self.holeCards[0].is_king() and self.holeCards[1].is_ace()

    def is_suited(self):
        if len(self.holeCards) != 2:
            return False
        else:
            return self.holeCards[0].cardSuit == self.holeCards[1].cardSuit

    def is_connected(self):
        if len(self.holeCards) != 2:
            return False
        else:
            return self.holeCards[0].is_connected(self.holeCards[1])
        
    def is_connected_and_suited(self):
        return self.is_suited() and self.is_connected()
    
    def has_card(self, card):
        return self.holeCards[0] == card or self.holeCards[1] == card
    
    def get_player_hole_cards(self):
        return self.holeCards
    
    def is_seven_two(self):
        return self.holeCards[0].is_seven() and self.holeCards[1].is_two() or self.holeCards[0].is_two() and self.holeCards[1].is_seven()
    
    def is_eight_two(self):
        return self.holeCards[0].is_eight() and self.holeCards[1].is_two() or self.holeCards[0].is_two() and self.holeCards[1].is_eight()
      
        