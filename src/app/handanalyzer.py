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
            return "No better starting hand than Pocket Rockets!"
        elif player_hand.is_face_pair(): #2 should play
            hand_strength.preflop_code = 2
            hand_strength.preflop_desc = "Pocket pair of face cards is very strong"
            return "Pocket pair of face cards is very strong"
        elif player_hand.is_pair(): #2 should play
            hand_strength.preflop_code = 2
            hand_strength.preflop_desc = "A pocket pair is a great way to start"
            return "A pocket pair is a great way to start"
        elif player_hand.is_big_slick(): #2 should play
            hand_strength.preflop_code = 2
            hand_strength.preflop_desc = "Big Slick offers great potential"            
            return "Big Slick offers great potential"
        elif player_hand.is_connected_and_suited(): #2 should play
            hand_strength.preflop_code = 2
            hand_strength.preflop_desc = "Suited connectors offer great potential"  
            return "Suited connectors offer great potential"
        elif player_hand.is_suited(): #3 may play
            hand_strength.preflop_code = 3
            hand_strength.preflop_desc = "Suited cards are flush with possibility"  
            return "Suited cards are flush with possibility" 
        elif player_hand.is_connected(): #3 may play
            hand_strength.preflop_code = 3
            hand_strength.preflop_desc = "Connectors offer straight potential"
            return "Connectors offer straight potential"
        elif player_hand.is_seven_two(): #5 worst starting hand
            hand_strength.preflop_code = 5
            hand_strength.preflop_desc = "Worst starting hand in hold em. Run!!!!"
            return "Worst starting hand in hold em.  Run!!!!"
        else: #4 advise against
            hand_strength.preflop_code = 4
            hand_strength.preflop_desc = "A good word for of your hand is milk toast. Beware!!!"
            return "A good word for of your hand is milk toast. Beware!!!"
        
    def calculate_flop_strength(self, player_hand, community_cards):
        pass
    
    def calculate_turn_strength(self, player_hand, community_cards):
        pass
            
    def calculate_river_strength(self, player_hand, community_cards):
        hand_strength = HandStrength() 
        self.combine_cards(player_hand, community_cards)
        return hand_strength.best_hand(self.all_cards_list)
                
    
    def combine_cards(self, player_hand, community_cards):
        if player_hand != None:
            for phcard in player_hand.get_player_hole_cards():
                self.all_cards_list.append(phcard)
        if community_cards != None:
            for cccard in community_cards.get_community_cards():
                self.all_cards_list.append(cccard)       
        return self.all_cards_list
    
    def num_cards(self):
        return len(self.all_cards_list)
        
        
    def __init__(self):
        self.preflop_strength = None
        self.flop_strength = None
        self.turn_strength = None 
        self.river_strength = None
        self.all_cards_list = list()
        
        
        
        