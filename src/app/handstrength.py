'''
Created on Oct 4, 2016

@author: mike
'''

class HandStrength(object):
    'Represents the strength of a players hand and any community cards'

    'enum list of possible hand outcomes'  
    ROYAL_FLUSH = "Royal Flush"
    STRAIGHT_FLUSH = "Straight Flush"
    FOUR_OF_A_KIND = "Four of a kind"
    FULL_HOUSE = "Full House"
    FLUSH = "Flush"
    STRAIGHT = "Straight"
    THREE_0F_A_KIND = "Three of a kind"
    TWO_PAIR = "Two Pair"
    PAIR = "Pair"
    HIGH_CARD = "High Card"
    
    
    def best_hand(self, card_list):
        pass
    
    
    def __init__(self):
        card_list = None
        preflop_code = None
        preflop_desc = None
        