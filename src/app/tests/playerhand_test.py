'''
Created on Sep 16, 2016

@author: mike
'''
import unittest
from app.card import Card
from app.cardvalue import CardValue
from app.cardsuit import CardSuit
from app.playerhand import PlayerHand




class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_add_player_hole_cards(self):
        black_bullet = Card(CardSuit.SPADE, CardValue.ACE)
        bloody_duece = Card(CardSuit.DIAMOND, CardValue.TWO)
        hand = PlayerHand()
        assert 0 == hand.num_hole_cards()
        hand.add_hole_card(black_bullet)
        assert 1 == hand.num_hole_cards()
        hand.add_hole_card(bloody_duece)
        assert 2 == hand.num_hole_cards()
        
    @unittest.expectedFailure   
    def test_too_many_hole_cards(self):
        black_bullet = Card(CardSuit.SPADE, CardValue.ACE)
        bloody_duece = Card(CardSuit.DIAMOND, CardValue.TWO)
        hand = PlayerHand()
        assert 0 == hand.num_hole_cards()
        hand.add_hole_card(black_bullet)
        assert 1 == hand.num_hole_cards()
        hand.add_hole_card(bloody_duece)
        assert 2 == hand.num_hole_cards()
        
        'This should throw an exception & fail as a player is limited to two hole cards'
        hand.add_hole_card(bloody_duece)
    
    @unittest.expectedFailure    
    def test_player_hole_cards_must_be_different(self):
        black_bullet = Card(CardSuit.SPADE, CardValue.ACE)
        hand = PlayerHand()
        hand.add_hole_card(black_bullet)
        'This should throw an exception & fail - hole cards must be different'
        hand.add_hole_card(black_bullet)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add_one_player_hole_card']
    unittest.main()