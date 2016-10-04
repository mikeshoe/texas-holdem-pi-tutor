'''
Created on Sep 20, 2016

@author: mike
'''
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards


class HandAnalyzer(object):
    'Class that contains the hand analyzer logic'

        
    def calculate_preflop_strength(self, player_hand):
        if player_hand.is_pocket_rockets():
            return "Pocket Rocks are the best!"
        elif player_hand.is_face_pair():
            return "Pocket pair of face cards is very strong"
        elif player_hand.is_pair():
            return "Pocket pair is a great way to start"
        elif player_hand.is_big_slick():
            return "Big Slick offers great potential"
        elif player_hand.is_connected_and_suited():
            return "Connected and suited - great potential"
        elif player_hand.is_suited():
            return "Suited cards bring flush potential"
        elif player_hand.is_connected():
            return "Connectors bring straight potential"
        else:
            return "Proceed with caution.  Your hand blows!"
        
    def calculate_flop_strength(self, player_hand, community_cards):
        pass
    
    def calculate_turn_strength(self, player_hand, community_cards):
        pass
            
    def calculate_river_strength(self, player_hand, community_cards):
        pass         
    
    def __init__(self):
        self.preflop_strength = None
        self.flop_strength = None
        self.turn_strength = None 
        self.river_strength = None
        
        
        
        