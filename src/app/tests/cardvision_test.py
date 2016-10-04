'''
Created on Sep 30, 2016

@author: mike
'''
import unittest
import os
from app.cardvision import CardVision
from app.tests.utparent import UTParent
 


class Test(UTParent):
    NUM_CARDS_IN_DECK = 52
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    TRAINING_LABELS_FILEPATH = os.path.join(THIS_DIR, '../config/training_labels.tsv')
    #print "Training Labels Filepath: ", TRAINING_LABELS_FILEPATH 
    
    TRAINING_IMAGE_FILEPATH = os.path.join(THIS_DIR, '../images/training_image.png')
    #print "Training Image Filepath: ", TRAINING_IMAGE_FILEPATH
        
    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_get_training(self):
        card_vision = CardVision()
        assert None != card_vision
        
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        assert None != training_deck
        
    def test_find_ten_clubs_and_king_diamonds(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/10c-kd.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_ten_clubs())
        assert True == player_hand.has_card (self.get_king_diamonds())
        
        
    def test_find_ten_diamonds_and_two_diamonds(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/10d-2d.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_ten_diamonds())
        assert True == player_hand.has_card (self.get_two_diamonds())
        assert False == player_hand.has_card (self.get_three_diamonds())
        
    def test_find_ten_spades_and_ace_hearts(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/10s-ah.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_ten_spades())
        assert True == player_hand.has_card (self.get_ace_hearts())
    
    def test_find_three_clubs_and_six_clubs(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/3c-6c.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)
        print player_hand.holeCards[0]
        print player_hand.holeCards[1]

        assert True == player_hand.has_card (self.get_three_clubs())
        assert True == player_hand.has_card (self.get_six_clubs())        

    def test_find_four_clubs_and_eight_hearts(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/4c-8h.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_four_clubs())
        assert True == player_hand.has_card (self.get_eight_hearts()) 

    def test_find_four_spades_and_two_spades(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/4s-2s.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_four_spades())
        assert True == player_hand.has_card (self.get_two_spades())

    def test_find_five_clubs_and_eight_diamonds(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/5c-8d.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_five_clubs())
        assert True == player_hand.has_card (self.get_eight_diamonds())
        
    def test_find_five_diamonds_and_two_hearts(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/5d-2h.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_five_diamonds())
        assert True == player_hand.has_card (self.get_two_hearts())
        
    def test_find_five_hearts_and_three_spades(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/5h-3s.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_five_hearts())
        assert True == player_hand.has_card (self.get_three_spades())
        
    def test_find_six_diamonds_and_seven_spades(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/6d-7s.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_six_diamonds())
        assert True == player_hand.has_card (self.get_seven_spades())
        
    def test_find_six_hearts_and_king_clubs(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/6h-kc.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_six_hearts())
        assert True == player_hand.has_card (self.get_king_clubs())

    def test_find_seven_clubs_and_ten_hearts(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/7c-10h.jpg')
        player_hand = card_vision.find_hole_cards(card_filepath, training_deck)

        assert True == player_hand.has_card (self.get_seven_clubs())
        assert True == player_hand.has_card (self.get_ten_hearts())        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_train_deck']
    unittest.main()