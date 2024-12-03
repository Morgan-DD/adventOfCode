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
total = 0

def GetWholeNumberAndId(idChar, idLine):
    exitLoop = True
    id = idChar+1
    fullNumber = str(fileContent.split("\n")[idLine][idChar])
    while(exitLoop):
        if(id >= len(fileContent.split("\n")[idLine])):
            exitLoop = False
            break
        if((fileContent.split("\n")[idLine])[id].isnumeric()):
            fullNumber += str((fileContent.split("\n")[idLine])[id])
        else:
            exitLoop = False
        id+= 1
    return fullNumber

def isNumberNearSymbols(idChar, idLine, char):
    isNumberNearSymbolsResult = False
    regex = re.compile(r'[^0-9.]+')
    stringToCheck = ""
    charToCheck = [0,0]
    if (int(idChar + len(char)) <= len(fileContent.split("\n")[idLine])-1):
        charToCheck[1] = int(idChar + len(char))
        stringToCheck += fileContent.split("\n")[idLine][charToCheck[1]]
    if(charId-1 >= 0):
        charToCheck[0] = charId-1
        stringToCheck += fileContent.split("\n")[idLine][charToCheck[0]]
    if(idLine > 0):
        stringToCheck += fileContent.split("\n")[idLine-1][charToCheck[0]:charToCheck[1]+1]
    if(idLine < len(fileContent.split("\n"))-1):
        stringToCheck += fileContent.split("\n")[idLine+1][charToCheck[0]:charToCheck[1]+1]
    if((re.search(regex,stringToCheck))):
       isNumberNearSymbolsResult = True
    return isNumberNearSymbolsResult

lineId = 0
charId = 0
lastIsNum = False
for Line in fileContent.split("\n"):
    for char in Line:
        if char.isnumeric():
            if(not Line[charId-1].isnumeric()):
                if(isNumberNearSymbols(charId, lineId,GetWholeNumberAndId(charId, lineId))):
                    total+=int(GetWholeNumberAndId(charId, lineId))
                lastIsNum = True
        charId+=1
    lastIsNum = False
    lineId+=1
    charId=0

print("total: " + str(total))