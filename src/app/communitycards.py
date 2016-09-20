'''
Created on Sep 20, 2016

@author: mike
'''

class CommunityCards(object):
    'Class that represents a single players hand (hole cards)'
   

    def __init__(self):
        self.communityCards = []
        
    def add_community_card(self, card):
        if self.num_community_cards() < 5:
            if self.communityCards.count(card) == 0:
                self.communityCards.append(card)
            else:
                raise Exception("Cards must be different")
        else:
            raise Exception("Community cards are limited to 5")
        
    def num_community_cards(self):
        return len(self.communityCards)
    
        