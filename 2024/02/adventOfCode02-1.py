#
# Advent of code 02
#
import os
import sys
import re
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
lines = open(lineFilePath).read()

maxRedCube = 12
maxGreenCube = 13
maxBlueCube = 14

tempRed = 0
tempGreen = 0
tempBlue = 0

idGame = 1

totalId = 0

lines=lines.split("\n")
test=""

for line in lines:
    line = line.split(":")[1]
    line = line.replace(",", ";")
    line = line.split(";")
    print(line)
    for cube in line:
        number=re.sub("[A-z]","",cube)
        cube=re.sub("[0-9 ]","",cube)
        match (cube):
            case ("green"):
                if(int(number) > tempGreen):
                    tempGreen=int(number)
                test=test+" | green"
            case("red"):
                if(int(number) > tempRed):
                    tempRed=int(number)
                test=test+" | red"
            case("blue"):
                if(int(number) > tempBlue):
                    tempBlue=int(number)
                test=test+" | blue"
    print(test)
    if(tempRed <= maxRedCube and tempGreen <= maxGreenCube and tempBlue <= maxBlueCube):
        totalId=totalId+idGame
        print("possible, ID: " + str(idGame))
        print("red: " + str(tempRed))
        print("green: " + str(tempGreen))
        print("blue: " + str(tempBlue))
    tempRed = 0
    tempGreen = 0
    tempBlue = 0
    idGame=idGame+1
    test=""

print("---------")
print(totalId)
