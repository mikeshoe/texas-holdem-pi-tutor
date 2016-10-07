'''
Created on Oct 7, 2016

@author: kevin
'''
class Output(object):
        
    @staticmethod
    def printWelcomeBanner():
        print """\
    Welcome to...
    
  _______                   _    _       _     _                        _______    _             
 |__   __|                 | |  | |     | |   | |                      |__   __|  | |            
    | | _____  ____ _ ___  | |__| | ___ | | __| |______ ___ _ __ ___      | |_   _| |_ ___  _ __ 
    | |/ _ \ \/ / _` / __| |  __  |/ _ \| |/ _` |______/ _ \ '_ ` _ \     | | | | | __/ _ \| '__|
    | |  __/>  < (_| \__ \ | |  | | (_) | | (_| |     |  __/ | | | | |    | | |_| | || (_) | |   
    |_|\___/_/\_\__,_|___/ |_|  |_|\___/|_|\__,_|      \___|_| |_| |_|    |_|\__,_|\__\___/|_|   
                                                                                                 
                                                                                                 
"""
        
    @staticmethod
    def printSeparator(self):
        print "**********************************************************************"

    @staticmethod
    def printMessage(self, message):
        print "***   %s    ***" %message
 