#!/usr/bin/env python
"""Authors: Andrew Wentz, Adrian Jania, Emily McMinn
CSCE100 Final Project
"""
import csv

#open data file
file = open("alcoholfile.csv")
csv_file = csv.reader(file)

dictionary = {}
#sorts file into dictionary
for row in csv_file:
    key = row[0]
    if key in dictionary:
        pass
    dictionary[key] = [row[1], row[2]]

#search dictionary for location and time input
print("UNL Alcohol Violations Database - Fall 2016")
location = input("Enter campus building closest to your location: ")
time = input("Enter your current time (XX:XX): ")
time = time.replace(":", "")
time = int(time)
x = dictionary[location]
if 500 <= time <= 2100:
    print("Number of daytime violations this semester at {}: {}".format(location, x[0]))
else:
    print("Number of nighttime violations this semester at {}: {}".format(location, x[1]))