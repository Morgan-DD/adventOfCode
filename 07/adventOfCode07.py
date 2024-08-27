#
# Advent of code 07
#
import os
import sys
from collections import Counter
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
total = 0
entry = 0
number = 0

def getCharNumberInString(string, charSearched):
    counter = 0
    for char in string:
        if char == charSearched:
            counter+=1
    return counter

def getEntryValue(entry):
#    print(entry)
    for char in entry:
        print("-# " + char)
        print(getCharNumberInString(entry, char))


for line in fileContent.split("\n"):
    entry = line.split(" ")[0]
    number = line.split(" ")[1]
    print(getEntryValue(entry))