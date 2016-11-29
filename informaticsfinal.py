#!/usr/bin/env python
"""Authors: Andrew Wentz, Adrian Jania, Emmie Grimmie
CSCE100 Final Project
"""
import csv
#open original data file
file = open("reports.csv")
csv_file = csv.reader(file)
#open edited data file
newfile = open("alcohols.csv")
csv_newfile = csv.reader(newfile)

dictionary = {
    
}

#location = input("Enter your current location: ")

#function for removing duplicate locations
"""def locationparse():
    loclist = []
    count = 0
    for row in csv_file:
        loclist.append(row[7])
    print(list(set(sorted(loclist))))"""
    
    #function for returning whole rows of info
    """if location in row:
        count = count+1
        print("{}, {}, {}".format(row[1], row[2], row[10]))
print(count)"""