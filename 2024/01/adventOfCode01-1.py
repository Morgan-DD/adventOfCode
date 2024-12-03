#
# Advent of code 01
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
datas = open(dataFilePath).read()

totalDistance = 0

Right = []
Left = []

for line in datas.split("\n"):
    Left+=[line.split("   ")[0]]
    Right+=[line.split("   ")[1]]

Left.sort()
Right.sort()

for i, LineLeft in enumerate(Left):
    diffrence = int(Right[i])-int(LineLeft)
    if(diffrence < 0):
        diffrence = diffrence*-1
    totalDistance+=diffrence

print("Resut:" + str(totalDistance))