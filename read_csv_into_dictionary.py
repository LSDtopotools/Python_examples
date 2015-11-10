# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:19:40 2015

@author: smudd
"""

# This reads a csv file into a dictionary
def read_csv_into_dictionary(filename):

    import csv
    with open(filename) as csvfile:
        
        # here is a reader. It will get the data from the csv file        
        reader = csv.DictReader(csvfile)
        
        # this is the disctionary into which data will be read        
        theDict = {}
        
        # loop through the rows, which are individual dicts, and append them into
        # a dict where each key points to a list
        for row in reader:
            for key, value in row.iteritems():
                
                # check to see if key exists
                if key in theDict.keys():
                    theDict[key].append(value)
                else:
                    theDict[key] = []
                    theDict[key].append(value)
                #print(row['basin_ID'])

    print theDict['basin_ID']
    #
    keyList= list(theDict.keys())
    
    print keyList
    
    
    return theDict
    
    
if __name__ == "__main__":
    Filename = "SanBern_Spawned_CRNResults.csv"
    read_csv_into_dictionary(Filename) 