'''
Created on Sep 20, 2016

@author: mike
'''
from app.playerhand import PlayerHand
from app.communitycards import CommunityCards
from app.handstrength import HandStrength
from app.cardvalue import CardValue
from app.cardsuit import CardSuit



class HandAnalyzer(object):
    'Class that contains the hand analyzer logic'
    
    'class variable lists containing all values & suits'
    cardValueList = [CardValue.ACE, CardValue.KING, CardValue.QUEEN, CardValue.JACK, CardValue.TEN, CardValue.NINE, CardValue.EIGHT, CardValue.SEVEN, CardValue.SIX, CardValue.FIVE, CardValue.FOUR, CardValue.THREE, CardValue.TWO]
    cardSuitList = [CardSuit.CLUB, CardSuit.DIAMOND, CardSuit.HEART, CardSuit.SPADE]
        
    def analyze_preflop(self, player_hand):
        hand_strength = HandStrength()
        hand_strength.step = HandStrength.STEP_PRE_FLOP
        
        if player_hand.is_pocket_rockets():  #1 best possible
            hand_strength.advice = HandStrength.ADVICE_MUST_PLAY
            hand_strength.message = "No better starting hand than Pocket Rockets!"
            return "No better starting hand than Pocket Rockets!"
        elif player_hand.is_face_pair(): #2 should play
            hand_strength.advice = HandStrength.ADVICE_SHOULD_PLAY
            hand_strength.message = "Pocket pair of face cards is very strong"
            return "Pocket pair of face cards is very strong"
        elif player_hand.is_pair(): #2 should play
            hand_strength.advice = HandStrength.ADVICE_SHOULD_PLAY
            hand_strength.message = "A pocket pair is a great way to start"
            return "A pocket pair is a great way to start"
        elif player_hand.is_big_slick(): #2 should play
            hand_strength.advice = HandStrength.ADVICE_SHOULD_PLAY
            hand_strength.message = "Big Slick offers great potential"            
            return "Big Slick offers great potential"
        elif player_hand.is_connected_and_suited(): #2 should play
            hand_strength.advice = HandStrength.ADVICE_SHOULD_PLAY
            hand_strength.message = "Suited connectors offer great potential"  
            return "Suited connectors offer great potential"
        elif player_hand.is_suited(): #3 may play
            hand_strength.advice = HandStrength.ADVICE_MAY_PLAY
            hand_strength.message = "Suited cards are flush with possibility"  
            return "Suited cards are flush with possibility" 
        elif player_hand.is_connected(): #3 may play
            hand_strength.advice = HandStrength.ADVICE_MAY_PLAY
            hand_strength.message = "Connectors offer straight potential"
            return "Connectors offer straight potential"
        elif player_hand.is_seven_two(): #5 worst starting hand
            hand_strength.advice = HandStrength.ADVICE_NEVER_PLAY
            hand_strength.message = "Worst starting hand in hold em. Run!!!!"
            return "Worst starting hand in hold em.  Run!!!!"
        else: #4 advise against
            hand_strength.advice = HandStrength.ADVICE_SHOULD_NOT_PLAY
            hand_strength.message = "A good word for of your hand is milk toast. Beware!!!"
            return "A good word for of your hand is milk toast. Beware!!!"
        
            
    def analyze_hand(self, player_hand, community_cards):
        self.combine_cards(player_hand, community_cards)
        return self.best_hand()
                
    
    def combine_cards(self, player_hand, community_cards):
        if player_hand != None:
            for phcard in player_hand.get_player_hole_cards():
                self.all_cards_list.append(phcard)
        if community_cards != None:
            for cccard in community_cards.get_community_cards():
                self.all_cards_list.append(cccard)       
        return self.all_cards_list
    
    def num_cards(self):
        return len(self.all_cards_list)
        
    def best_hand(self):
        hand_strength = HandStrength()
        
        if self.num_cards() == 5:  #2 player hole cards + 3 community cards
            hand_strength.step = HandStrength.STEP_POST_FLOP
        elif self.num_cards() == 6: #2 player hole cards + 4 community cards
            hand_strength.step = HandStrength.STEP_POST_TURN
        elif self.num_cards() == 7: #2 player hole cards + 5 community cards
            hand_strength.step = HandStrength.STEP_POST_RIVER
            
        if self.is_royal_flush():
            return HandStrength.HAND_ROYAL_FLUSH
        elif self.is_straight_flush():
            return HandStrength.HAND_STRAIGHT_FLUSH
        elif self.is_four_of_a_kind():
            return HandStrength.HAND_FOUR_OF_A_KIND
        elif self.is_full_house():
            return HandStrength.HAND_FULL_HOUSE
        elif self.is_flush():
            return HandStrength.HAND_FLUSH
        elif self.is_straight():
            return HandStrength.HAND_STRAIGHT
        elif self.is_three_of_a_kind():
            return HandStrength.HAND_THREE_0F_A_KIND
        elif self.is_two_pair():
            return HandStrength.HAND_TWO_PAIR
        elif self.is_pair():
            return HandStrength.HAND_PAIR
        else:
            return HandStrength.HAND_HIGH_CARD
          
    def is_royal_flush(self):
        return False 
    
    def is_straight_flush(self):
        return False    
    
    def is_four_of_a_kind(self):
        for cval in self.cardValueList:
            #print "is_four_of_a_kind cval:", cval
            cardvalue_count = self.occurences_by_value(cval)
            if cardvalue_count == 4:
                return True
            
        return False   
    
    def is_full_house(self):
        return False  
    
    def is_flush(self):
        for csuit in self.cardSuitList:
            #print "is_three_of_a_kind cval:", cval
            cardsuit_count = self.occurences_by_suit(csuit)
            if cardsuit_count >= 5:
                return True
            
        return False
    
    def is_straight(self):
        return False     
    
    def is_three_of_a_kind(self):
        for cval in self.cardValueList:
            #print "is_three_of_a_kind cval:", cval
            cardvalue_count = self.occurences_by_value(cval)
            if cardvalue_count >= 3:
                return True
            
        return False          

    def is_two_pair(self):
        return False  
    
    def is_pair(self):
        for cval in self.cardValueList:
            #print "is_pair cval:", cval
            cardvalue_count = self.occurences_by_value(cval)
            if cardvalue_count >= 2:
                return True
            
        return False
                
            
    
    def occurences_by_value(self, card_value):
        value_count = 0
        for card in self.all_cards_list:
            #print "occurences_by_value card:", card
            if card_value == card.cardValue:
                value_count = value_count + 1
        
        return value_count
    
    def occurences_by_suit(self, card_suit):
        suit_count = 0
        for card in self.all_cards_list:
            #print "occurences_by_suit card:", card
            if card_suit == card.cardSuit:
                suit_count = suit_count + 1
        #print "occurrences_by_suit:", card_suit, "count:", suit_count
        return suit_count
        
    
    
         
    def __init__(self):
        self.all_cards_list = list()
        
        
        
        