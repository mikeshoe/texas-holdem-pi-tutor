'''
Created on Oct 4, 2016

@author: mike
'''
import unittest
from app.handanalyzer import HandAnalyzer
from app.tests.utparent import UTParent
from app.handstrength import HandStrength


class Test(UTParent):


    def setUp(self):
        self.ha = HandAnalyzer()
        pass


    def tearDown(self):
        pass


    def test_combine_and_get_num_cards(self):
        self.ha.combine_cards(self.get_player_hand_QS_10S(), self.get_community_cards_AS_KS_JS_10D_2H())
        assert 7 == self.ha.num_cards()
        
    def test_combine_with_no_community_cards(self):
        self.ha.combine_cards(self.get_player_hand_QS_10S(), None)
        assert 2 == self.ha.num_cards()    
        
    def test_combine_with_no_player_hand(self):
        self.ha.combine_cards(None, self.get_community_cards_AS_KS_JS_10D_2H())
        assert 5 == self.ha.num_cards() 
        
    def test_high_card_hand(self):
        assert HandStrength.HAND_HIGH_CARD == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_10D_9H())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()