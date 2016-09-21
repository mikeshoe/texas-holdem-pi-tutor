'''
Created on Sep 20, 2016

@author: mike
'''
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards

class HandAnalyzer(object):
    'Class that contains the hand analyzer logic'


    def calculate_hand_strength(self, player_hand, community_cards):
        self.preflop_strength = self.__preflop_calc__(player_hand)
        
        self.flop_strength = None
        self.turn_strength = None
        self.river_strength = None
        
    def __preflop_calc__(self, player_hand):
        if player_hand.is_pocket_rockets():
            'best'
        elif player_hand.is_face_pair():
            'very strong'
        elif player_hand.is_pair() or player_hand().is_big_slick():
            'strong'
        elif player_hand.is_suited() or player_hand.is_connected():
            'has potential'
        else:
            'run'
            
                
        
        
        
        