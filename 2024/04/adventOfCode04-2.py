#
# Advent of code 04-2
#
import os
import sys
import re
import numpy 
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()

print(fileContent)

winningNumbers = []
myNumbers = []
pointOfLine = 0

totalPoints = 0

for line in fileContent.split("\n"):
    winningNumbers = line.split(":")[-1].split("|")[0].split(" ")
    myNumbers = line.split(":")[-1].split("|")[1].split(" ")
    for myNumber in myNumbers:
        if(myNumber.isnumeric()):
            for winningNumber in winningNumbers:
                if(winningNumber == myNumber):
                    if(pointOfLine == 0):
                        pointOfLine = 1
                    else:
                        pointOfLine*=2
    totalPoints+=pointOfLine
    pointOfLine = 0
print(totalPoints)
