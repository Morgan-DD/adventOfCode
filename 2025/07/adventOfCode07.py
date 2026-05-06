#
# Advent of code 07-1
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
data = open(lineFilePath).read().split("\n")

total = 0

exitWhile = False
exitAdditionWhile = False

triesdone = []

idNumber=0

tries = 0

for line in data:
    triesdone=[]
    goal = line.split(":")[0]
    numbers = line.split(":")[1].split(" ")
    patern=[]
    temptry=[]
    baseID=0
    while not exitWhile:
        operationNumber = len(numbers)-1
        for i in range(1,operationNumber):
            patern += ["*"]

        exitWhile = True


        triesdone+=[patern]


        # print("mathDoing: " + str(mathDoing))
        print("goal: " + str(goal))
        print(triesdone)
