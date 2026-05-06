#
# Advent of code 02-1
#    28844599675
#
import os
import sys

def isValidId(myNumber):
    mid = len(myNumber) // 2
    return myNumber[mid:] == myNumber[:mid]



script_folder_path = os.path.dirname(os.path.abspath(__file__))
dataFilePath = os.path.join(script_folder_path, 'data.txt')
data = open(dataFilePath).read().split(",")

invalidIDsTotal = 0

for idRange in data :
    rangeStart, rangeEnd = idRange.split("-")
    for i in range(int(rangeStart), int(rangeEnd)):
        if(isValidId(str(i))):
            invalidIDsTotal += i

print(invalidIDsTotal)