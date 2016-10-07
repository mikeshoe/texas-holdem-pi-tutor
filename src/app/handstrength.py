'''
Created on Oct 4, 2016

@author: mike
'''

class HandStrength(object):
    'Represents the strength of a players hand and any community cards'

    STEP_PRE_FLOP = 0
    STEP_POST_FLOP = 1
    STEP_POST_TURN = 2
    STEP_POST_RIVER = 3

    'enum list of hand strengths'
    ADVICE_MUST_PLAY = 1
    ADVICE_SHOULD_PLAY = 2
    ADVICE_MAY_PLAY = 3
    ADVICE_SHOULD_NOT_PLAY = 4
    ADVICE_NEVER_PLAY = 5
    
    
    'enum list of possible hand outcomes'  
    HAND_ROYAL_FLUSH = "Royal Flush"
    HAND_STRAIGHT_FLUSH = "Straight Flush"
    HAND_FOUR_OF_A_KIND = "Four of a kind"
    HAND_FULL_HOUSE = "Full House"
    HAND_FLUSH = "Flush"
    HAND_STRAIGHT = "Straight"
    HAND_THREE_0F_A_KIND = "Three of a kind"
    HAND_TWO_PAIR = "Two Pair"
    HAND_PAIR = "Pair"
    HAND_HIGH_CARD = "High Card"
    
    
    
    def __init__(self):
        step = None
        card_list = None
        advice = None
        message = None
        hand_result = None
        