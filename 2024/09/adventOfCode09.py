#
# Advent of code 09
#
import os
import sys
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()

record = []
lastOasisInfo = None

ExitWhile = False

def getDifference(listToCheck):
    print("listToCheck: " + str(listToCheck))
    listToReturn = []
    lastItem = None
    for item in listToCheck:
  #      print("------------------")
  #      print("item: " + str(item))
  #      print("lastItem: " + str(lastItem))
        if not (lastItem is None):
            listToReturn.append(int(item) - int(lastItem))
        lastItem = item
    return listToReturn

for OasisInfos in fileContent.split("\n"):
    print("--------------------------------------------------")
    print(OasisInfos)
    #idaa = 0
    while not ExitWhile:
        #   print(idaa)
        #   idaa+=1
        if not record:
            record.append(getDifference(OasisInfos.split(" ")))
        elif record[-1][-1] != 0:
        #    print("record[-1]: " + str(record[-1]))
            record.append(getDifference(record[-1]))
        elif record[-1][-1] == 0:
            print("0 trouvé")
            ExitWhile = True
    print("RECORD: ")
    print(record)
    record = []
    lastOasisInfo = None
    ExitWhile = False