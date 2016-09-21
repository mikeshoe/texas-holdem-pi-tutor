'''
Created on Sep 16, 2016

@author: mike
'''
from app.deck import Deck
from app.card import Card
from app.playerhand import PlayerHand
from app.handanalyzer import HandAnalyzer

if __name__ == '__main__':
    pass

'mocking out scanned cards - KEVIN SHIT PLUGS IN HERE'
mock_deck = Deck()
hole_card_one = mock_deck.draw_card()
hole_card_two = mock_deck.draw_card()


print "Please scan 1st hole card:"
print "   Scanner found: ", hole_card_one
print "Please scan 2nd hole card:"
print "   Scanner found: ", hole_card_two

'construct player hand from scanned cards'
player_hand = PlayerHand()
player_hand.add_hole_card(hole_card_one)
player_hand.add_hole_card(hole_card_two)

'create game deck of cards'
deck = Deck()

'must remove scanned cards from deck so they do not show up in community cards'
deck.remove_card_from_deck(hole_card_one)
deck.remove_card_from_deck(hole_card_two)

analyzer = HandAnalyzer()
print "Preflop hand strength:  ", analyzer.preflop_strength(player_hand)


