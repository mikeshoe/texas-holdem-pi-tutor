'''
Created on Oct 7, 2016

@author: kevin
'''
from app.tests.utparent import UTParent
import unittest
from app.utility import Output


class Test(UTParent):


    def testPrintWelcomeBanner(self):
        Output.printWelcomeBanner()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()