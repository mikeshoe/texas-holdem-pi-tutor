'''
Created on Sep 14, 2016

@author: mike
'''
import unittest
from app.deck import Deck
from app.card import Card


class Test(unittest.TestCase):
       
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_new_deck(self):
        mydeck = Deck()
        assert mydeck != None 
        
    def test_deck_is_not_shuffled(self):
        mydeck = Deck()
        assert mydeck.is_shuffled() == False
        
    def test_draw_card_not_null(self):
        mydeck = Deck()
        mycard = mydeck.draw_card()
        assert mycard != None
        
    def test_two_draws_not_same_card(self):
        mydeck = Deck()
        mycard1 = mydeck.draw_card()
        mycard2 = mydeck.draw_card()
        assert mycard1 != mycard2
        
    def test_deck_starts_with_52_cards(self):
        mydeck = Deck()
        assert 52 == mydeck.num_cards_remaining()
        
    def test_deck_has_51_cards_after_one_draw(self):
        mydeck = Deck()
        mycard = mydeck.draw_card()
        assert 51 == mydeck.num_cards_remaining()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()