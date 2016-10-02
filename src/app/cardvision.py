'''
Created on Sep 30, 2016

@author: mike
'''

import os
import numpy as np
import cv2



class CardVision(object):
    'Class responsible for computer vision operations'
    

    ###############################################################################
    # Utility code from 
    # http://git.io/vGi60A
    # Thanks to author of the sudoku example for the wonderful blog posts!
    ###############################################################################

    def rectify(self, h):
        h = h.reshape((4,2))
        hnew = np.zeros((4,2),dtype = np.float32)
    
        add = h.sum(1)
        hnew[0] = h[np.argmin(add)]
        hnew[2] = h[np.argmax(add)]
       
        diff = np.diff(h,axis = 1)
        hnew[1] = h[np.argmin(diff)]
        hnew[3] = h[np.argmax(diff)]
    
        return hnew
    
    ###############################################################################
    # Image Matching
    ###############################################################################
    def preprocess(self, img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),2 )
        
        # Not sure which of the following works better.  More testing needed.
        # thresh = cv2.adaptiveThreshold(blur,255,1,1,11,1)
        tmp, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        return thresh
      
    def imgdiff(self, img1,img2):
        img1 = cv2.GaussianBlur(img1,(5,5),5)
        img2 = cv2.GaussianBlur(img2,(5,5),5)    
        diff = cv2.absdiff(img1,img2)  
        diff = cv2.GaussianBlur(diff,(5,5),5)    
        flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY) 
        return np.sum(diff)  
    
    def find_closest_card(self, training,img):
        features = self.preprocess(img)
        return sorted(training.values(), key=lambda x:self.imgdiff(x[1],features))[0][0]
    
    
    ###############################################################################
    # Card Extraction
    ###############################################################################  
    def getCards(self, im, numcards=2):
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(1,1),1000)
        flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY) 
           
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
        contours = sorted(contours, key=cv2.contourArea,reverse=True)[:numcards]  
    
        for card in contours:
            peri = cv2.arcLength(card,True)
            approx = self.rectify(cv2.approxPolyDP(card,0.02*peri,True))
    
            # DEBUG - uncomment to see cycle through training image
            # box = np.int0(approx)
            # cv2.drawContours(im,[box],0,(255,255,0),6)
            # imx = cv2.resize(im,(1000,600))
            # cv2.imshow('a',imx) 
            # cv2.waitKey(0)      
            
            h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
        
            transform = cv2.getPerspectiveTransform(approx,h)
            warp = cv2.warpPerspective(im,transform,(450,450))
        
            
            yield warp
    
    
    def get_training(self, training_label_path, training_image_path, num_cards_in_deck):
        
        avoid_cards=None
        
        training = {}
    
        labels = {}
        for line in file(training_label_path): 
            key, num, suit = line.strip().split()
            labels[int(key)] = (num,suit)
            # print "labels:",  labels[int(key)]
    
        #print "Training"
    
        im = cv2.imread(training_image_path)
        
        for i,c in enumerate(self.getCards(im,num_cards_in_deck)):
            if avoid_cards is None or (labels[i][0] not in avoid_cards[0] and labels[i][1] not in avoid_cards[1]):
                training[i] = (labels[i], self.preprocess(c))
    
    
        #print "Done training"
        return training
    
    def find_hole_cards(self, hole_card_image_path, training):
        NUM_HOLE_CARDS = 2
        
        #training = self.get_training()
        
        im = cv2.imread(hole_card_image_path)
        
        #ToDo - Should be able to remove this logic if we force the cards to be scanned by camera in a consistent way
        width = im.shape[0]
        height = im.shape[1]
        if width < height:
            im = cv2.transpose(im)
            im = cv2.flip(im,1)
      
        cards = [self.find_closest_card(training, c) for c in self.getCards(im, NUM_HOLE_CARDS)]
        # print cards
          
    def __init__(self):
        self
    
    
    
    
    
