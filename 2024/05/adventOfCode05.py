#
# Advent of code 05
#
import os
import sys
import re
import numpy 
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
minLocation = -1
blocks = fileContent.split("\n\n")
def findSimillarInList(blocks, valueSearch):
  #  print("valueSearch: " + str(valueSearch))
    if(valueSearch != None and valueSearch != ""):
        for line in blocks.split(":")[-1].split("\n"):
            if(line != ""):
                if(int(line.split(" ")[1]) < int(valueSearch)):
                    if(int(line.split(" ")[1]) + int(line.split(" ")[2]) > int(valueSearch)):
                      #  print(line.split(" ")[0] + " < " + str(valueSearch))
                        return int(line.split(" ")[0]) + (valueSearch - int(line.split(" ")[1]))
    return valueSearch

for seed in blocks[0].split(":")[-1].split(" "):
    print(seed)
    if(seed != ""):
  #      print("*---------------SEED---------------*")
        actualNumber = int(seed)
        for block in blocks[1:]:
         #   print("*---------------Block[" + block.split(":")[0] + "]---------------*")
            if (actualNumber != "" and actualNumber != None):
                actualNumber = findSimillarInList(block, actualNumber)
        if (actualNumber != "" and actualNumber != None):
         #   print("seed:" + str(seed) + " | actualNumber: " + str(actualNumber) + " | nom block: " + block.split(":")[0])
            print("FINAL: " + str(actualNumber))
        if(int(minLocation) < 0 or int(minLocation) > int(actualNumber)):
            minLocation = actualNumber
    print("+---------------+")
print(minLocation)