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

'construct player hand from scanned cards'
player_hand = PlayerHand()
player_hand.add_hole_card(hole_card_one)
player_hand.add_hole_card(hole_card_two)

print "WELCOME TO THE TEXAS HOLD-EM TUTOR"
print"-----------------------------------"
print " "
print " "

print "Please put your hole cards on the scanner:"
print "   Scanned hole cards are: ", hole_card_one, " and ", hole_card_two
print " "
print " "

'create game deck of cards'
deck = Deck()

'must remove scanned cards from deck so they do not show up in community cards'
deck.remove_card_from_deck(hole_card_one)
deck.remove_card_from_deck(hole_card_two)

analyzer = HandAnalyzer()
print "**********************************************************************"
print "***   Preflop advice:", analyzer.calculate_preflop_strength(player_hand), "    ***"
print "**********************************************************************"
print " "
print " "


print "Press any key to play the flop:"
print "Flop is:", deck.draw_card(), ",", deck.draw_card(), ",", deck.draw_card()
print "Hole cards: ", hole_card_one, " and ", hole_card_two
print "**********************************************************************"
print "***   Post flop advice:", analyzer.calculate_preflop_strength(player_hand), "   ***"
print "**********************************************************************"
print " "
print " "
print " "

print "Press any key to play the turn:"
print "Hole cards: ", hole_card_one, " and ", hole_card_two
print "Turn is:", deck.draw_card()
print "**********************************************************************"
print "***   Post Turn advice:", analyzer.calculate_preflop_strength(player_hand), "   ***"
print "**********************************************************************"
print " "
print " "
print " "

print "Press any key to play the river:"
print "Hole cards: ", hole_card_one, " and ", hole_card_two
print "River is:", deck.draw_card()
print "**********************************************************************"
print "***   Post River advice:", analyzer.calculate_preflop_strength(player_hand), "  ***"
print "**********************************************************************"
print " "


