#
# Advent of code 03
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
data = open(lineFilePath).read()
totalNumber = 0


def isNextToSpecial(numberData, dataList):
    # print("__________________________")
    lineId = numberData[0]
    start = numberData[1][0]
    end = numberData[1][1]
    for a in range(lineId - 1, lineId + 2):
        if a < len(dataList):
            """
            if a == lineId:
                print("-> | " + dataList[a])
            else:
                print(dataList[a])
            print(",,,,,,,,,,,,,")
            """
        for b in range(start - 1, end + 1):
            if 0 < a < len(dataList) and 0 < b < len(dataList[a]):
                # print(dataList[a][b])
                if dataList[a][b] in "*+=$#/&%":
                    return True
    return False


data = data.split("\n")
allNumber = []
number = [-1, -1]
lastWasNumber = False
charCount = 0
idLine = 0
printLastNumber = False
for line in data:
    for char in line:
        if char.isdigit():
            if not lastWasNumber:
                number[0] = charCount
                number[1] = charCount + 1
            else:
                number[1] = charCount + 1
            lastWasNumber = True
            printLastNumber = True
        else:
            if lastWasNumber and number[0] != -1:
                if idLine > 0 and len(allNumber) > 0:
                    if ".." in data[allNumber[-1][0]][allNumber[-1][1][0]:allNumber[-1][1][1]]:
                        number[0] = number[0] - 1
                        print()
                        print("aaaaaaaaaaaaaaaaaaaaaaa")
                        print("number: " + str(number[0]))
                        print("number[0]: " + str(number[0]))
                        print(data[allNumber[-1][0]][allNumber[-1][1][0]:allNumber[-1][1][1]])
                        print(data[idLine][number[0]:number[1]])
                        allNumber.append([idLine-1, number])
                    else:
                        allNumber.append([idLine, number])
                        lastWasNumber = False
                        number = [-1, -1]
                if printLastNumber:
                    """
                    print(allNumber[-1])
                    print(data[allNumber[-1][0]][allNumber[-1][1][0]:allNumber[-1][1][1]])"""
                    printLastNumber = False
        charCount = charCount + 1
    charCount = 0
    idLine = idLine + 1
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for singleNumber in allNumber:
    #    print(data[singleNumber[0]][singleNumber[1][0]:singleNumber[1][1]])
    if isNextToSpecial(singleNumber, data):
        #        and data[singleNumber[0]][singleNumber[1][0]:singleNumber[1][1]].isdigit()
        """
        print(data[singleNumber[0]][singleNumber[1][0]:singleNumber[1][1]])
        print("singleNumber[0]: " + str(singleNumber[0]))
        print("singleNumber[1][0]: " + str(singleNumber[1][0]))
        print("singleNumber[1][1]: " + str(singleNumber[1][1]))
        print("singleNumber: ")
        print(data[singleNumber[0]])
        """
        try:
            totalNumber = totalNumber + int(data[singleNumber[0]][singleNumber[1][0]:singleNumber[1][1]])
        except:
            print(data[singleNumber[0]][singleNumber[1][0]:singleNumber[1][1]])
            print("singleNumber[0]: " + str(singleNumber[0]))
            print("singleNumber[1][0]: " + str(singleNumber[1][0]))
            print("singleNumber[1][1]: " + str(singleNumber[1][1]))
            print("singleNumber: ")
            print(data[singleNumber[0]])
            print(data[singleNumber[0]-1])
            print("-<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>-")
print("-----")
print(str(totalNumber))
