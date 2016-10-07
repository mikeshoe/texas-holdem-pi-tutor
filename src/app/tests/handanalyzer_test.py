'''
Created on Oct 4, 2016

@author: mike
'''
import unittest
from app.handanalyzer import HandAnalyzer
from app.tests.utparent import UTParent


class Test(UTParent):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_combine_and_get_num_cards(self):
        ha = HandAnalyzer()
        ha.combine_cards(self.get_player_hand_QS_10S(), self.get_community_cards_AS_KS_JS_10D_2H())
        assert 7 == ha.num_cards()
        
    def test_combine_with_no_community_cards(self):
        ha = HandAnalyzer()
        ha.combine_cards(self.get_player_hand_QS_10S(), None)
        assert 2 == ha.num_cards()    
        
    def test_combine_with_no_player_hand(self):
        ha = HandAnalyzer()
        ha.combine_cards(None, self.get_community_cards_AS_KS_JS_10D_2H())
        assert 5 == ha.num_cards() 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()