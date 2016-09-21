'''
Created on Sep 16, 2016

@author: mike
'''
import unittest
from app.card import Card
from app.cardvalue import CardValue
from app.cardsuit import CardSuit
from app.playerhand import PlayerHand
from app.tests.utparent import UTParent



class Test(UTParent):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_add_player_hole_cards(self):
        black_bullet = self.get_ace_spades()
        bloody_duece = self.get_two_diamonds()
        hand = PlayerHand()
        assert 0 == hand.num_hole_cards()
        hand.add_hole_card(black_bullet)
        assert 1 == hand.num_hole_cards()
        hand.add_hole_card(bloody_duece)
        assert 2 == hand.num_hole_cards()
        
    @unittest.expectedFailure   
    def test_too_many_hole_cards(self):
        black_bullet = self.get_ace_spades()
        bloody_duece = self.get_two_diamonds()
        three_hearts = self.get_three_hearts()
        hand = PlayerHand()
        assert 0 == hand.num_hole_cards()
        hand.add_hole_card(black_bullet)
        assert 1 == hand.num_hole_cards()
        hand.add_hole_card(bloody_duece)
        assert 2 == hand.num_hole_cards()
        
        'This should throw an exception & fail as a player is limited to two hole cards'
        hand.add_hole_card(three_hearts)
    
    @unittest.expectedFailure    
    def test_player_hole_cards_must_be_different(self):
        black_bullet = self.get_ace_spades()
        hand = PlayerHand()
        hand.add_hole_card(black_bullet)
        'This should throw an exception & fail - hole cards must be different'
        hand.add_hole_card(black_bullet)
        
    def test_is_not_pocket_rockets(self):
        black_bullet = self.get_ace_spades()
        red_king = self.get_king_diamonds()
        hand = PlayerHand()
        hand.add_hole_card(black_bullet)
        hand.add_hole_card(red_king)
        
        assert False == hand.is_pocket_rockets()
               
         
    def test_is_pocket_rockets(self):
        black_bullet = self.get_ace_spades()
        red_bullet = self.get_ace_diamonds()

        hand = PlayerHand()
        hand.add_hole_card(black_bullet)
        hand.add_hole_card(red_bullet) 
        
        assert True == hand.is_pocket_rockets()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add_one_player_hole_card']
    unittest.main()