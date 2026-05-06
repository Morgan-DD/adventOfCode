#
# Advent of code 11-1
#
import os
import sys
from fileinput import isfirstline

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()

rocksLine = fileContent

tmpRocksLine = ""
isfirstnumber = True

blinkNeeded = 25
blinkCounter = 1

while blinkCounter<=blinkNeeded:
    # print("------------------------------------------")
    # print(rocksLine)
    tmpRocksLine = ""
    isfirstnumber = True
    for rock in rocksLine.split(" "):
        if int(rock) == 0:
            # print(str(rock) + " 0")
            if isfirstnumber:
                tmpRocksLine+="1"
            else:
                tmpRocksLine += " 1"
        elif len(rock)% 2 == 0:
            # print(str(rock) + " paire")
            if isfirstnumber:
                tmpRocksLine+=str(int(rock[:len(rock) // 2]))
                tmpRocksLine+=" " + str(int(rock[len(rock) // 2:]))
            else:
                tmpRocksLine+=" " + str(int(rock[:len(rock) // 2]))
                tmpRocksLine+=" " + str(int(rock[len(rock) // 2:]))
        else:
            if isfirstnumber:
                tmpRocksLine += str(int(rock) * 2024)
            else:
                tmpRocksLine +=" " +  str(int(rock) * 2024)
            # print(str(rock) + " *2024")
        rocksLine=tmpRocksLine
        isfirstnumber = False
    # print(str(blinkCounter) + ", " + str(len(tmpRocksLine)))
    print(str(blinkCounter) + "/" + str(blinkNeeded))
    blinkCounter+=1

print("Number of blink: " + str(blinkNeeded))
print("number of rocks: " + str(len(tmpRocksLine.split(" "))))
print("expected resut:  183435")
# < 192366
# 183435