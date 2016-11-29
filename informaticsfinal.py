#!/usr/bin/env python
"""Author: Andrew Wentz
CSCE100 Final Project
"""
import csv
file = open("reports.csv")
csv_file = csv.reader(file)

dictionary = {
    
}

#location = input("Enter your current location: ")
#time = input("Enter time: ")
loclist = []
count = 0
for row in csv_file:
    loclist.append(row[7])
print(list(set(sorted(loclist))))
    #if time in row:
        #print(row)
    #if location in row:
        #count = count+1
        #print(row)
        #print("{}, {}, {}".format(row[1], row[2], row[10]))
#print(count)