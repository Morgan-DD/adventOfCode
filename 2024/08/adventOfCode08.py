#
# Advent of code 08
#
import os
import sys
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
nbMove = 0

actualNode = "AAA"

isCharFinded = False

movementList = fileContent.split("\n\n")[0]
nodeList = fileContent.split("\n\n")[1].split("\n")

def getNodeFromInfo(node, movement):
    for nodeLine in nodeList:
        if node in nodeLine.split(" = ")[0]:
            return nodeLine.split(" = ")[1].split(", ")[movement].replace("(", "").replace(")", "")


while (not isCharFinded):
    for SingleMovement in movementList:
        nbMove+=1
    #    getNodeFromInfo(actualNode, SingleMovement)
        if(SingleMovement == "L"):
            actualNode = getNodeFromInfo(actualNode, 0)
        elif(SingleMovement == "R"):
            actualNode = getNodeFromInfo(actualNode, 1)
        if(actualNode == "ZZZ"):
            print("FIN !!!")
            print("nbMove: " + str(nbMove))
            isCharFinded = True
            break
        else:
            print("actualNode: [" + str(actualNode) + "] | " + "SingleMovement: [" + SingleMovement + "]")
