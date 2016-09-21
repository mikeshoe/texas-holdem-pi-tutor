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


    def get_ten_hearts(self):
        return Card(CardSuit.HEART, CardValue.TEN)
    
    def get_jack_hearts(self):
        return Card(CardSuit.HEART, CardValue.JACK)
        
    def get_ace_hearts(self):
        return Card(CardSuit.HEART, CardValue.ACE)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()