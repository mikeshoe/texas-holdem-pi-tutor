'''
Created on Sep 20, 2016

@author: mike
'''
import unittest
from app.card import Card
from app.cardvalue import CardValue
from app.cardsuit import CardSuit
from app.communitycards import CommunityCards
from app.tests.utparent import UTParent


class Test(UTParent):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_add_community_cards(self):
        ace_spades = self.get_ace_spades()
        two_diamonds = self.get_two_diamonds()
        three_hearts = self.get_three_hearts()
        four_clubs = self.get_four_clubs()
        five_spades = self.get_five_spades()
        
        community_cards = CommunityCards()
        assert 0 == community_cards.num_community_cards()
        community_cards.add_community_card(ace_spades)
        assert 1 == community_cards.num_community_cards()
        community_cards.add_community_card(two_diamonds)
        assert 2 == community_cards.num_community_cards()
        community_cards.add_community_card(three_hearts)
        assert 3 == community_cards.num_community_cards()
        community_cards.add_community_card(four_clubs)
        assert 4 == community_cards.num_community_cards()
        community_cards.add_community_card(five_spades)
        assert 5 == community_cards.num_community_cards()

    @unittest.expectedFailure   
    def test_too_many_community_cards(self):
        ace_spades = self.get_ace_spades()
        two_diamonds = self.get_two_diamonds()
        three_hearts = self.get_three_hearts()
        four_clubs = self.get_four_clubs()
        five_spades = self.get_five_spades()
        six_diamonds = self.get_six_diamonds()
        
        community_cards = CommunityCards()
        assert 0 == community_cards.num_community_cards()
        community_cards.add_community_card(ace_spades)
        assert 1 == community_cards.num_community_cards()
        community_cards.add_community_card(two_diamonds)
        assert 2 == community_cards.num_community_cards()
        community_cards.add_community_card(three_hearts)
        assert 3 == community_cards.num_community_cards()
        community_cards.add_community_card(four_clubs)
        assert 4 == community_cards.num_community_cards()
        community_cards.add_community_card(five_spades)
        assert 5 == community_cards.num_community_cards()
        
        
        'This should throw an exception & fail as hold-em is limited to 5 community cards'
        community_cards.add_community_card(six_diamonds)
        
    @unittest.expectedFailure    
    def test_community_cards_must_be_different(self):
        black_bullet = self.get_ace_spades()
        community_cards = CommunityCards()
        community_cards.add_community_card(black_bullet)
        
        'This should throw an exception & fail - community cards must be different'
        community_cards.add_community_card(black_bullet)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()