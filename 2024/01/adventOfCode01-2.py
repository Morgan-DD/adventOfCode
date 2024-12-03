#
# Advent of code 01-2
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
data = open(dataFilePath).read()

similarityScore = 0

Right = []
Left = []

for line in data.split("\n"):
    Left+=[line.split("   ")[0]]
    Right+=[line.split("   ")[1]]

Left.sort()
Right.sort()

multiplier = 0
for LineLeft in Left:
    multiplier = 0
    for LineRight in Right:
        if(LineRight == LineLeft):
            multiplier+=1
        if(LineRight > LineLeft):
            break
    similarityScore += int(LineLeft)*multiplier
    print(LineLeft)

print("similarity score: " + str(similarityScore))

