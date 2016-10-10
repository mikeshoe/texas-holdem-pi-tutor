'''
Created on Sep 21, 2016

@author: mike
'''
import unittest
from app.card import Card 
from app.cardsuit import CardSuit
from app.cardvalue import CardValue
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards

class UTParent(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    'CLUBS'   
    
    def get_two_clubs(self):
        return Card(CardSuit.CLUB, CardValue.TWO)
    
    def get_three_clubs(self):
        return Card(CardSuit.CLUB, CardValue.THREE)
    
    def get_four_clubs(self):
        return Card(CardSuit.CLUB, CardValue.FOUR)
    
    def get_five_clubs(self):
        return Card(CardSuit.CLUB, CardValue.FIVE)
     
    def get_six_clubs(self):
        return Card(CardSuit.CLUB, CardValue.SIX)
    
    def get_seven_clubs(self):
        return Card(CardSuit.CLUB, CardValue.SEVEN)
    
    def get_eight_clubs(self):
        return Card(CardSuit.CLUB, CardValue.EIGHT)
    
    def get_nine_clubs(self):
        return Card(CardSuit.CLUB, CardValue.NINE)
    
    def get_ten_clubs(self):
        return Card(CardSuit.CLUB, CardValue.TEN)
    
    def get_jack_clubs(self):
        return Card(CardSuit.CLUB, CardValue.JACK)
     
    def get_queen_clubs(self):
        return Card(CardSuit.CLUB, CardValue.QUEEN)
    
    def get_king_clubs(self):
        return Card(CardSuit.CLUB, CardValue.KING)
    
    def get_ace_clubs(self):
        return Card(CardSuit.CLUB, CardValue.ACE)
    
    'DIAMONDS'
    def get_two_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.TWO)
    
    def get_three_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.THREE)
    
    def get_four_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.FOUR)
    
    def get_five_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.FIVE)
    
    def get_six_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.SIX)
    
    def get_seven_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.SEVEN)
    
    def get_eight_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.EIGHT)
    
    def get_nine_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.NINE)
    
    def get_ten_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.TEN)
    
    def get_jack_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.JACK)
    
    def get_queen_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.QUEEN)
    
    def get_king_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.KING)
    
    def get_ace_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.ACE)
    
    'HEARTS'    
    def get_two_hearts(self):
        return Card(CardSuit.HEART, CardValue.TWO)

    def get_three_hearts(self):
        return Card(CardSuit.HEART, CardValue.THREE)
    
    def get_four_hearts(self):
        return Card(CardSuit.HEART, CardValue.FOUR)

    def get_five_hearts(self):
        return Card(CardSuit.HEART, CardValue.FIVE)
    
    def get_six_hearts(self):
        return Card(CardSuit.HEART, CardValue.SIX)
    
    def get_seven_hearts(self):
        return Card(CardSuit.HEART, CardValue.SEVEN)   

    def get_eight_hearts(self):
        return Card(CardSuit.HEART, CardValue.EIGHT)
            
    def get_nine_hearts(self):
        return Card(CardSuit.HEART, CardValue.NINE)
    
    def get_ten_hearts(self):
        return Card(CardSuit.HEART, CardValue.TEN)
    
    def get_jack_hearts(self):
        return Card(CardSuit.HEART, CardValue.JACK)
    
    def get_queen_hearts(self):
        return Card(CardSuit.HEART, CardValue.QUEEN)   

    def get_king_hearts(self):
        return Card(CardSuit.HEART, CardValue.KING)
            
    def get_ace_hearts(self):
        return Card(CardSuit.HEART, CardValue.ACE)

    'SPADES'  
    def get_two_spades(self):
        return Card(CardSuit.SPADE, CardValue.TWO)  
    
    def get_three_spades(self):
        return Card(CardSuit.SPADE, CardValue.THREE)
        
    def get_four_spades(self):
        return Card(CardSuit.SPADE, CardValue.FOUR)
     
    def get_five_spades(self):
        return Card(CardSuit.SPADE, CardValue.FIVE)  
    
    def get_six_spades(self):
        return Card(CardSuit.SPADE, CardValue.SIX)
        
    def get_seven_spades(self):
        return Card(CardSuit.SPADE, CardValue.SEVEN)
          
    def get_eight_spades(self):
        return Card(CardSuit.SPADE, CardValue.EIGHT)
    
    def get_nine_spades(self):
        return Card(CardSuit.SPADE, CardValue.NINE)
          
    def get_ten_spades(self):
        return Card(CardSuit.SPADE, CardValue.TEN)
    
    def get_jack_spades(self):
        return Card(CardSuit.SPADE, CardValue.JACK)
          
    def get_queen_spades(self):
        return Card(CardSuit.SPADE, CardValue.QUEEN)
    
    def get_king_spades(self):
        return Card(CardSuit.SPADE, CardValue.KING)
          
    def get_ace_spades(self):
        return Card(CardSuit.SPADE, CardValue.ACE)    

    # Player Hands
    def get_player_hand_AC_AD(self):
        ph = PlayerHand()
        ph.add_hole_card(self.get_ace_clubs())
        ph.add_hole_card(self.get_ace_diamonds())
        return ph
    
    def get_player_hand_QS_10S(self):
        ph = PlayerHand()
        ph.add_hole_card(self.get_queen_spades())
        ph.add_hole_card(self.get_ten_spades())
        return ph
    
    def get_player_hand_7S_2D(self):
        ph = PlayerHand()
        ph.add_hole_card(self.get_seven_spades())
        ph.add_hole_card(self.get_two_diamonds())
        return ph
    
    def get_player_hand_3C_4C(self):
        ph = PlayerHand()
        ph.add_hole_card(self.get_three_clubs())
        ph.add_hole_card(self.get_four_clubs())
        return ph

    def get_player_hand_2S_2D(self):
        ph = PlayerHand()
        ph.add_hole_card(self.get_two_spades())
        ph.add_hole_card(self.get_two_diamonds())
        return ph
        
    # Community Cards
    def get_community_cards_AS_KS_JS_10D_2H(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_ten_diamonds())
        community_cards.add_community_card(self.get_two_hearts())
        return community_cards
    
    def get_community_cards_AS_KS_JS_7D_2H(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_seven_diamonds())
        community_cards.add_community_card(self.get_two_hearts())
        return community_cards
    
    def get_community_cards_AS_KS_JS_10D_9H(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_ten_diamonds())
        community_cards.add_community_card(self.get_nine_hearts())
        return community_cards  
    
    def get_community_cards_AS_KS_JS_7D_9H(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_seven_diamonds())
        community_cards.add_community_card(self.get_nine_hearts())
        return community_cards 
    
    def get_community_cards_AS_KS_JS_2C_2H(self): 
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_two_clubs())
        community_cards.add_community_card(self.get_two_hearts())
        return community_cards   
    
    def get_community_cards_AS_KS_7S_2C_2H(self): 
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_seven_spades())
        community_cards.add_community_card(self.get_two_clubs())
        community_cards.add_community_card(self.get_two_hearts())
        return community_cards  
    
    def get_community_cards_AS_KS_JS_2S_2H(self): 
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_two_spades())
        community_cards.add_community_card(self.get_two_hearts())
        return community_cards  
    
    def get_community_cards_AS_KS_QD_JD_10S(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_ace_spades())
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_queen_diamonds())
        community_cards.add_community_card(self.get_jack_diamonds())
        community_cards.add_community_card(self.get_ten_spades())
        return community_cards 
    
    def get_community_cards_KS_QS_JS_10S_9S(self):
        community_cards = CommunityCards()
        community_cards.add_community_card(self.get_king_spades())
        community_cards.add_community_card(self.get_queen_spades())
        community_cards.add_community_card(self.get_jack_spades())
        community_cards.add_community_card(self.get_ten_spades())
        community_cards.add_community_card(self.get_nine_spades())
        return community_cards        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()