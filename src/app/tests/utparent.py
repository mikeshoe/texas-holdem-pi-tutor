'''
Created on Sep 21, 2016

@author: mike
'''
import unittest
from app.card import Card 
from app.cardsuit import CardSuit
from app.cardvalue import CardValue

class UTParent(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    'CLUBS'    
    def get_four_clubs(self):
        return Card(CardSuit.CLUB, CardValue.FOUR)
    
    'DIAMONDS'
    def get_two_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.TWO)
    
    def get_three_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.THREE)
    
    def get_six_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.SIX)
    
    def get_king_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.KING)
    
    def get_ace_diamonds(self):
        return Card(CardSuit.DIAMOND, CardValue.ACE)
    
    'HEARTS'    
    def get_three_hearts(self):
        return Card(CardSuit.HEART, CardValue.THREE)

    def get_ten_hearts(self):
        return Card(CardSuit.HEART, CardValue.TEN)
    
    def get_jack_hearts(self):
        return Card(CardSuit.HEART, CardValue.JACK)
    
    def get_queen_hearts(self):
        return Card(CardSuit.HEART, CardValue.QUEEN)   
        
    def get_ace_hearts(self):
        return Card(CardSuit.HEART, CardValue.ACE)

    'SPADES'   
    def get_five_spades(self):
        return Card(CardSuit.SPADE, CardValue.FIVE)  
      
    def get_ace_spades(self):
        return Card(CardSuit.SPADE, CardValue.ACE)    



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()