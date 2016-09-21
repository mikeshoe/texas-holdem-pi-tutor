'''
Created on Sep 14, 2016

@author: mike
'''
import unittest
from app.tests.utparent import UTParent


class Test(UTParent):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_new_card(self):
        myCard = self.get_ace_hearts()
        assert myCard != None
        
    def test_cards_equal(self):
        tenHeartsCard1 = self.get_ten_hearts()
        tenHeartsCard2 = self.get_ten_hearts()
        assert tenHeartsCard1 == tenHeartsCard2
        
        
    def test_cards_not_equal(self):
        tenHeartsCard = self.get_ten_hearts()
        jackHeartsCard = self.get_jack_hearts()
        assert tenHeartsCard != jackHeartsCard
        
    def test_card_is_face(self):
        testcard = self.get_king_diamonds()
        assert True == testcard.is_face()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNewCard']
    unittest.main()