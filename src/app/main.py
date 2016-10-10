# /usr/bin/python

'''
Created on Sep 16, 2016

@author: mike
'''
#import sys
#sys.path.insert(0, "/usr/local/lib/python2.7/site-packages")
#sys.path.insert(0, "/home/pi/git/texas/holdem-tutor/src")

from app.deck import Deck
from app.card import Card
from app.playerhand import PlayerHand
from app.handanalyzer import HandAnalyzer
from app.cardvision import CardVision
from app.communitycards import CommunityCards
import time
import datetime
import os
from app.utility import Output

if __name__ == '__main__':
    pass

NUM_CARDS_IN_DECK = 52
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINING_LABELS_FILEPATH = os.path.join(THIS_DIR, './config/training_labels.tsv')
#print "Training Labels Filepath: ", TRAINING_LABELS_FILEPATH 


utc_ts = datetime.datetime.utcnow()
utc_string = utc_ts.strftime('%Y-%m-%d-%H%M%SZ')
holecards_pict_file = "/home/pi/hole_cards-" + utc_string + ".jpg"
take_pic_command ='raspistill -n -t 1000 -o ' + holecards_pict_file
#print "Raspi Command:" + take_pic_command
#uncomment when running on pi
#os.system(take_pic_command)

TRAINING_IMAGE_FILEPATH = os.path.join(THIS_DIR, './images/training_image.png')
#print "Training Image Filepath: ", TRAINING_IMAGE_FILEPATH

print "Loading card deck..."
card_vision = CardVision()
training_deck = card_vision.get_training(TRAINING_LABELS_FILEPATH, TRAINING_IMAGE_FILEPATH, NUM_CARDS_IN_DECK)

print "Ready to begin.  Press ctrl-c at any time to quit."

try:
    while True:
        
        Output.printWelcomeBanner()



        print "Please put your hole cards on the scanner:"
        #print "(press any key once your hole cards are in place)"
        raw_input('(press return once your hole cards are in place)')
        
        #card_filepath = os.path.join(THIS_DIR, holecards_pict_file)
        
        # real implementation 
        #print 'hole cards filepath:', holecards_pict_file
        #player_hand = card_vision.find_hole_cards(holecards_pict_file, training_deck)
        #hole_card_one = player_hand.holeCards[0]
        #hole_card_two = player_hand.holeCards[1]
        
        #mock implementation - comment out this or the above
        mock_deck = Deck()
        mock_hole_card_one = mock_deck.draw_card()
        mock_hole_card_two = mock_deck.draw_card()
        mock_player_hand = PlayerHand()
        mock_player_hand.add_hole_card(mock_hole_card_one)
        mock_player_hand.add_hole_card(mock_hole_card_two)
        player_hand = mock_player_hand
        hole_card_one = mock_hole_card_one
        hole_card_two = mock_hole_card_two
        
        Output.printSeparator()
        print " "
        print " "
        #print "   Scanned hole cards are: ", hole_card_one, " and ", hole_card_two
        print "***   Scanned hole cards are: ", hole_card_one, " and ", hole_card_two
        print " "
        print " "
        Output.printSeparator()

        
        'create game deck of cards'
        deck = Deck()
        
        'must remove scanned cards from deck so they do not show up in community cards'
        deck.remove_card_from_deck(hole_card_one)
        deck.remove_card_from_deck(hole_card_two)
        
        communityCards = CommunityCards()
        communityCards.add_community_card(deck.draw_card())
        communityCards.add_community_card(deck.draw_card())
        communityCards.add_community_card(deck.draw_card())
        
        analyzer = HandAnalyzer()
        Output.printSeparator()
        print "***   Preflop advice:", analyzer.analyze_preflop(player_hand), "    ***"
        Output.printSeparator()
        print " "
        print " "
        
        
        raw_input( "Press any key to play the flop:")
        print " "
        print " "
        print "Flop is:", communityCards
        print "Hole cards: ", hole_card_one, " and ", hole_card_two
        Output.printSeparator()
        print "***   Post flop advice:", analyzer.analyze_hand(player_hand, communityCards).message, "   ***"
        Output.printSeparator()
        print " "
        print " "
        print " "
        
       
        raw_input("Press any key to play the turn:")
        print "Hole cards: ", hole_card_one, " and ", hole_card_two
        turnCard = deck.draw_card()
        print "Turn is:", turnCard
        communityCards.add_community_card(turnCard)
        print "Community Cards: ", communityCards
        print "**********************************************************************"
        print "***   Post Turn advice:", analyzer.analyze_hand(player_hand, communityCards).message, "   ***"
        print "**********************************************************************"
        print " "
        print " "
        print " "
        
        raw_input("Press any key to play the river:")
        print "Hole cards: ", hole_card_one, " and ", hole_card_two
        riverCard = deck.draw_card()
        print "River is:", riverCard
        communityCards.add_community_card(riverCard)
        print "Community Cards: ", communityCards
        print "**********************************************************************"
        print "***   Post River advice:", analyzer.analyze_hand(player_hand, communityCards).message, "   ***"
        print "**********************************************************************"
        print " "
        quitString = raw_input("Press q to quit, otherwise replace hole cards and press any other key to continue.")
        if(quitString.lower() == "q"):
            raise KeyboardInterrupt("Thanks for playing!")
        os.system('clear')

except KeyboardInterrupt:
    print 'Quitting game.' 
