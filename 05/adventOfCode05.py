#
# Advent of code 03
#
import os
import sys
import re
import numpy 
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
minLocation = 0
block = fileContent.split("\n\n")

def findSimillarInList(block, valueSearch):
    for line in block.split(":")[-1].split("\n"):
        if(line != None and line!= ""):
            print("-| " + str(valueSearch))
            if(int(line.split(" ")[0]) < valueSearch and int(line.split(" ")[0])+int(line.split(" ")[2]) > valueSearch):
                return int(int(line.split(" ")[1]) + int(valueSearch - int(line.split(" ")[0])))


for seed in block[0].split(":")[-1].split(" "):
    if(seed != ""):
        print(findSimillarInList(block[2],findSimillarInList(block[1], int(seed))))