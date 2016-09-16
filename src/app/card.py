'''
Created on Sep 14, 2016

@author: mike
'''


class Card(object):
    'Class that represents an individual playing card'
    

    def __init__(self, cardSuit, cardValue):
        self.cardSuit = cardSuit
        self.cardValue = cardValue
        
    def __eq__(self,other):
        return self.cardSuit == other.cardSuit and self.cardValue == other.cardValue
    
    def __str__(self):
        return self.cardValue + " of " +  self.cardSuit
