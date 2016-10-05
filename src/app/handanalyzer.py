'''
Created on Sep 20, 2016

@author: mike
'''
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards
from app.handstrength import HandStrength



class HandAnalyzer(object):
    'Class that contains the hand analyzer logic'
    
    MUST_PLAY = 1
    SHOULD_PLAY = 2
    MAY_PLAY = 3
    SHOULD_NOT_PLAY = 4
    NEVER_PLAY = 5

        
    def calculate_preflop_strength(self, player_hand):
        hand_strength = HandStrength()
        
        if player_hand.is_pocket_rockets():  #1 best possible
            hand_strength.preflop_code = 1
            hand_strength.preflop_desc = "No better starting hand than Pocket Rockets!"
        elif player_hand.is_face_pair(): #2 should play
            return "Pocket pair of face cards is very strong"
        elif player_hand.is_pair(): #2 should play
            return "Pocket pair is a great way to start"
        elif player_hand.is_big_slick(): #2 should play
            return "Big Slick offers great potential"
        elif player_hand.is_connected_and_suited(): #2 should play
            return "Connected and suited - great potential"
        elif player_hand.is_suited(): #3 may play
            return "Suited cards bring flush potential"
        elif player_hand.is_connected(): #3 may play
            return "Connectors bring straight potential"
        elif player_hand.is_seven_two(): #5 worst starting hand
            return "Worst starting hand in hold em"
        else: #4 advise against
            return "Proceed with caution.  Your hand blows!"
        
    def calculate_flop_strength(self, player_hand, community_cards):
        pass
    
    def calculate_turn_strength(self, player_hand, community_cards):
        pass
            
    def calculate_river_strength(self, player_hand, community_cards):
        pass         
    
    def combine_cards(self, player_hand, community_cards):
        all_cards_list = list()
        all_cards_list.append(player_hand.get_player_hole_cards())
        all_cards_list.append(community_cards.get_community_cards())
        return all_cards_list
        
        
    def __init__(self):
        self.preflop_strength = None
        self.flop_strength = None
        self.turn_strength = None 
        self.river_strength = None
        
        
        
        