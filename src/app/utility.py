'''
Created on Oct 7, 2016

@author: kevin
'''
class Output(object):
    pass
    @staticmethod
    def printWelcomeBanner():
        print "WELCOME TO THE TEXAS HOLD-EM TUTOR"
        print"-----------------------------------"
        print " "
        print " "
        
    @staticmethod
    def printSeparator(self):
        print "**********************************************************************"

    @staticmethod
    def printMessage(self, message):
        print "***   %s    ***" %message
 