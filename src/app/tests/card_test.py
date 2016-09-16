'''
Created on Sep 14, 2016

@author: mike
'''
import unittest
from app.card import Card 
from app.cardsuit import CardSuit
from app.cardvalue import CardValue


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNewCard(self):
        myCard = Card(CardSuit.HEART, CardValue.ACE)
        assert myCard != None
        
    def testCardsEqual(self):
        tenHeartsCard1 = Card(CardSuit.HEART, CardValue.TEN)
        tenHeartsCard2 = Card(CardSuit.HEART, CardValue.TEN)
        assert tenHeartsCard1 == tenHeartsCard2
        
        
    def testCardsNotEqual(self):
        tenHeartsCard = Card(CardSuit.HEART, CardValue.TEN)
        jackHeartsCard = Card(CardSuit.HEART, CardValue.JACK)
        assert tenHeartsCard != jackHeartsCard


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNewCard']
    unittest.main()