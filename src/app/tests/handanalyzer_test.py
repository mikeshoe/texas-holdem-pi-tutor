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


    def test_combine_cards(self):
        ha = HandAnalyzer()
        #ha.combine_cards(self.get_player_hand_AC_AD(), community_cards)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()