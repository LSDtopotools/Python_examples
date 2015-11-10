# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:12:12 2015

@author: smudd
"""

from read_csv_into_dictionary import *
import re

# This changes lists of strings into flaots or ints, depending on their contents. 
def detect_floats_and_ints_in_lists_and_change_accordingly(DataDict):
    
    # go through every key in the dictionary and retrieve the list
    for key, thisList in DataDict.iteritems():
        
        # first we are goung to check if there is an alphanumeric character in the list
        has_a_letter = False
        for item in thisList:
            if re.search('[a-zA-Z]', item):
                has_a_letter = True
                #print "Key is: " + key +" and I found a letter"
                
        # if has a letter is False, the list is a number
        # you can check to see if it is a float or an int using is a digit
        if has_a_letter == False:
            newList = []
            has_a_decimal = False
            for item in thisList:
                if '.' in item:
                    newList.append(float(item))
                    has_a_decimal = True
                else:
                    newList.append(int(item))
            #print "This is a number, I am modifying to float"
            #print "key is: " + key
            DataDict[key] = newList
        
    for key, thisList in DataDict.iteritems():        
        print "Key is: " + key
        print thisList
                    
                    
        
    
    
    
if __name__ == "__main__":
    Filename = "SanBern_Spawned_CRNResults.csv"
    DataDict = read_csv_into_dictionary(Filename) 
    
    detect_floats_and_ints_in_lists_and_change_accordingly(DataDict)