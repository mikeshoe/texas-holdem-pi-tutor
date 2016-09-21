'''
Created on Sep 14, 2016

@author: mike
'''
import unittest
from app.card import Card 
from app.cardsuit import CardSuit
from app.cardvalue import CardValue
from app.tests.utparent import UTParent


class Test(UTParent):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNewCard(self):
        myCard = self.get_ace_hearts()
        assert myCard != None
        
    def testCardsEqual(self):
        tenHeartsCard1 = self.get_ten_hearts()
        tenHeartsCard2 = self.get_ten_hearts()
        assert tenHeartsCard1 == tenHeartsCard2
        
        
    def testCardsNotEqual(self):
        tenHeartsCard = self.get_ten_hearts()
        jackHeartsCard = self.get_jack_hearts()
        assert tenHeartsCard != jackHeartsCard


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNewCard']
    unittest.main()