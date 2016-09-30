'''
Created on Sep 30, 2016

@author: mike
'''
import unittest
import os
from app.cardvision import CardVision
 


class Test(unittest.TestCase):
    NUM_CARDS_IN_DECK = 52
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    TRAINING_LABELS_FILEPATH = os.path.join(THIS_DIR, '../config/training_labels.tsv')
    print "Training Labels Filepath: ", TRAINING_LABELS_FILEPATH 
    
    TRAINING_IMAGE_FILEPATH = os.path.join(THIS_DIR, '../images/training_image.png')
    print "Training Image Filepath: ", TRAINING_IMAGE_FILEPATH
        
    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_get_training(self):
        card_vision = CardVision()
        assert None != card_vision
        
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        assert None != training_deck
        
    def test_find_queen_diamond_and_seven_hearts(self):
        card_vision = CardVision()
        training_deck = card_vision.get_training(self.TRAINING_LABELS_FILEPATH, self.TRAINING_IMAGE_FILEPATH, self.NUM_CARDS_IN_DECK)
        
        card_filepath = os.path.join(self.THIS_DIR, '../images/qd-7h.jpg')
        cards = card_vision.find_hole_cards(card_filepath, training_deck)
        print cards
        pass
        
        
        

    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_train_deck']
    unittest.main()