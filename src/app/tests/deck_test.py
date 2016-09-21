'''
Created on Sep 14, 2016

@author: mike
'''
import unittest
from app.deck import Deck
from app.card import Card
from app.cardsuit import CardSuit
from app.cardvalue import CardValue
from test.test_deque import fail
from app.tests.utparent import UTParent




class Test(UTParent):
       
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
        
    def test_deck_contains_juice_newton_card(self):
        mydeck = Deck()
        juice_card = self.get_queen_hearts()
        current_card = None
        
        for x in range(0,51):
            current_card = mydeck.draw_card()
            if juice_card == current_card:
                return
            else:
                current_card = None
                
        assert current_card is not None
                
    def test_removal_of_juice_newton_card(self):
        mydeck = Deck()
        juice_card = self.get_queen_hearts()
        
        mydeck.remove_card_from_deck(juice_card)   
       
        while mydeck.num_cards_remaining() > 0:
            current_card = mydeck.draw_card()
            if juice_card == current_card:
                fail
                
        pass
                
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()