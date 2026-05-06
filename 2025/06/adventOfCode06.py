#
# Advent of code 06-1
#
import os, sys
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
data = open(lineFilePath).read().split("\n")

movementCounter = 0

Direction = 0
# 0: ↑
# 1: →
# 2: ↓
# 3: ←

IDLine=-1
IDChar=-1
NearBorder = 0

exitWhile = False
hitBorder = False

for i, row in enumerate(data):
    if '^' in row:
        IDLine=i
        IDChar=row.index('^')

# print("IDLine: " + str(IDLine))
# print("IDChar: " + str(IDChar))

print("Doing Stuff...")

while not exitWhile:
    match Direction:
        case 0:
            print("↑ | IDLine:" + str(IDLine) + " IDChar: " + str(IDChar))
            if IDLine-1 >= 0:
                if data[IDLine-1][IDChar] != "#":
                    IDLine-=1
                    movementCounter+=1
                    hitBorder = False
                else:
                    if hitBorder:
                        break
                    Direction = 1
            else:
                if hitBorder:
                    break
                Direction = 1
                hitBorder = True
        case 1:
            # print("→ | IDLine:" + str(IDLine) + " IDChar: " + str(IDChar))
            if IDChar+1 < len(data[IDLine]):
                if data[IDLine][IDChar+1] != "#":
                    IDChar+=1
                    movementCounter+=1
                    hitBorder = False
                else:
                    if hitBorder:
                        break
                    Direction = 2
            else:
                if hitBorder:
                    break
                Direction = 2
                hitBorder = True
        case 2:
            print("↓ | IDLine:" + str(IDLine) + " IDChar: " + str(IDChar))
            if IDLine+1 < len(data):
                if data[IDLine+1][IDChar] != "#":
                    IDLine+=1
                    movementCounter+=1
                    hitBorder = False
                else:
                    if hitBorder:
                        break
                    Direction = 3
            else:
                if hitBorder:
                    break
                Direction = 3
                hitBorder = True
        case 3:
            print("← | IDLine:" + str(IDLine) + " IDChar: " + str(IDChar))
            if IDChar-1 >= 0:
                if data[IDLine][IDChar-1] != "#":
                    IDChar-=1
                    movementCounter-=1
                    hitBorder = False
                else:
                    if hitBorder:
                        break
                    Direction = 0
            else:
                if hitBorder:
                    break
                Direction = 0
                hitBorder = True
print("movementCounter: " + str(movementCounter))
# > 2698