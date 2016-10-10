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
    
    def test_one_pair_hand(self):
        assert HandStrength.HAND_PAIR == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_10D_2H())    
    
    def test_not_one_pair_hand(self):
        assert HandStrength.HAND_PAIR != self.ha.analyze_hand(self.get_player_hand_3C_4C(), self.get_community_cards_AS_KS_JS_10D_2H())
     
    def test_two_pair_hand(self):
        assert HandStrength.HAND_TWO_PAIR == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_7D_2H())    
    
    def test_not_two_pair_hand(self):
        assert HandStrength.HAND_TWO_PAIR != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_10D_2H())    
     
    def test_three_of_kind_hand(self):
        assert HandStrength.HAND_THREE_0F_A_KIND == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    
    
    def test_not_three_of_a_kind_hand(self):
        assert HandStrength.HAND_THREE_0F_A_KIND != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_10D_2H())

    def test_four_of_kind_hand(self):
        assert HandStrength.HAND_FOUR_OF_A_KIND == self.ha.analyze_hand(self.get_player_hand_2S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    
    
    def test_not_four_of_a_kind_hand(self):
        assert HandStrength.HAND_FOUR_OF_A_KIND != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())
    
    def test_not_flush(self): 
        assert HandStrength.HAND_FLUSH != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    
        
    def test_flush(self): 
        assert HandStrength.HAND_FLUSH == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2S_2H())    

    def test_full_house_hand(self):
        assert HandStrength.HAND_FULL_HOUSE == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_7S_2C_2H())    

    def test_not_full_house_hand(self):
        assert HandStrength.HAND_FULL_HOUSE != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    
     
    def test_straight_hand(self):
        assert HandStrength.HAND_STRAIGHT == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_QD_JD_10S())    

    def test_not_straight_hand(self):
        assert HandStrength.HAND_STRAIGHT != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    

    def test_straight_flush_hand(self):
        assert HandStrength.HAND_STRAIGHT_FLUSH == self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_KS_QS_JS_10S_9S())    

    def test_not_straight_flush_hand(self):
        assert HandStrength.HAND_STRAIGHT_FLUSH != self.ha.analyze_hand(self.get_player_hand_7S_2D(), self.get_community_cards_AS_KS_JS_2C_2H())    
            
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()