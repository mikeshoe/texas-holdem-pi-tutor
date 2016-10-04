'''
Created on Sep 16, 2016

@author: mike
'''
from app.deck import Deck
from app.card import Card
from app.playerhand import PlayerHand
from app.handanalyzer import HandAnalyzer
import time
import datetime
import os

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
#print "(press any key once your hole cards are in place)"
variable = raw_input('(press return once your hole cards are in place)')

utc_ts = datetime.datetime.utcnow()
utc_string = utc_ts.strftime('%Y-%m-%d-%H%M%SZ')
holecards_pict_file = "hole_cards-" + utc_string + ".jpg"
take_pic_command ='raspistill -n -t 1000 -o /home/pi/' + holecards_pict_file
print "Command:" + take_pic_command
#uncomment when running on pi
#os.system(take_pic_command)

print " "
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


