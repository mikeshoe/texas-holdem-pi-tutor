'''
Created on Sep 20, 2016

@author: mike
'''
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards
from app import playerhand

class HandAnalyzer(object):
    'Class that contains the hand analyzer logic'

        
    def preflop_strength(self, player_hand):
        if player_hand.is_pocket_rockets():
            return "Pocket Rocks are the best!"
        elif player_hand.is_face_pair():
            return "Pocket pair of face cards is very strong"
        elif player_hand.is_pair():
            return "Pocket pair is a great way to start"
        elif player_hand.is_big_slick():
            return "Big Slick offers great potential"
        elif player_hand.is_suited():
            return "Suited cards bring flush potential"
        elif player_hand.is_connected():
            return "Connectors bring straight potential"
        else:
            return "Proceed with caution.  Your hand blows!"
            
                
        
        
        
        