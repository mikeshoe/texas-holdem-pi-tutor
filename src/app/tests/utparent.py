'''
Created on Sep 21, 2016

@author: mike
'''
import unittest
from app.card import Card 
from app.cardsuit import CardSuit
from app.cardvalue import CardValue
from app.playerhand import PlayerHand

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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()