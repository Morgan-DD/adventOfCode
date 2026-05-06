#
# Advent of code 04-1
#
import os
import sys
import re
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
data = open(lineFilePath).read()

XMASCounter = 0

XMASCounter+=data.count("XMAS")+data.count("SAMX")

idLine = 0
idChar = 0
allLines=data.split("\n")
columnString = ""
for column in range(len(allLines)):
    columnString = ""
    for line in range(len(allLines[0])):
        columnString += allLines[line][column]
    print(columnString)
    XMASCounter += columnString.count("XMAS") + columnString.count("SAMX")

for lineSecond in range(len(allLines[0])):
    for column in range(len(allLines)):
        if column+3 <= len(allLines[lineSecond])-1 and lineSecond+3 <= len(allLines)-1:
            if allLines[lineSecond][column] == "X" and allLines[lineSecond+1][column+1] == "M" and allLines[lineSecond+2][column+2] == "A" and allLines[lineSecond+3][column+3] == "S":
                XMASCounter += 1
            if allLines[lineSecond][column] == "S" and allLines[lineSecond+1][column+1] == "A" and allLines[lineSecond+2][column+2] == "M" and allLines[lineSecond+3][column+3] == "X":
                XMASCounter += 1
        if column-3 >= 0 and lineSecond-3 >= 0:
            if allLines[lineSecond][column] == "X" and allLines[lineSecond-1][column-1] == "M" and allLines[lineSecond-2][column-2] == "A" and allLines[lineSecond-3][column-3] == "S":
                XMASCounter += 1
            if allLines[lineSecond][column] == "S" and allLines[lineSecond-1][column-1] == "A" and allLines[lineSecond-2][column-2] == "M" and allLines[lineSecond-3][column-3] == "X":
                XMASCounter += 1

print("XMASCounter: " + str(XMASCounter))
# > 2487