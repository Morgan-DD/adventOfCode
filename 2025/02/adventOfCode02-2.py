#
# Advent of code 02-1
#
import os
import sys


def hasEvenDigits(myNumber):
    return len(myNumber) % 2 == 0

def isValidId(myNumber):
    mid = len(myNumber) // 2
    if(myNumber[mid:] == myNumber[:mid]):
        return True
    

script_folder_path = os.path.dirname(os.path.abspath(__file__))
dataFilePath = os.path.join(script_folder_path, 'data.txt')
data = open(dataFilePath).read().split(",")

invalidIDsTotal = 0

for idRange in data :
    rangeStart, rangeEnd = idRange.split("-")
    for i in range(int(rangeStart), int(rangeEnd)):
        if(hasEvenDigits(i)):
            if(isValidId(str(i))):
                invalidIDsTotal += i

print(invalidIDsTotal)