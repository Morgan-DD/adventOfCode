#
# Advent of code 07
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
rolls = [[], [], [], [], [], [], []]
total = 0
entry = 0
number = 0

def getCharNumberInString(string, charSearched):
    counter = 0
    for char in string:
        if char == charSearched:
            counter+=1
    return counter

def getEntryValue(entry):
#    print(entry)
    char = entry[0]
    entryModify = entry
   # print("-# " + char)
    match getCharNumberInString(entry, char):
        case 5:
            rolls[0].append([entry, number]) 
        case 4:
            rolls[1].append([entry, number]) 
        case 3:
            if(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 2):
                rolls[2].append([entry, number]) 
            else:
                rolls[3].append([entry, number]) 
        case 2:
            if(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 3):
                rolls[2].append([entry, number]) 
            elif(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 2):
                rolls[4].append([entry, number]) 
            else:
                rolls[5].append([entry, number]) 
        case 1:
            if(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 4):
                rolls[1].append([entry, number]) 
            elif(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 3):
                rolls[3].append([entry, number])  
            elif(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 2):
                if(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 3):
                    rolls[2].append([entry, number]) 
                elif(getCharNumberInString(entryModify.replace(char, ""), entryModify.replace(char, "")[0]) == 2):
                    rolls[4].append([entry, number]) 
                else:
                    rolls[5].append([entry, number]) 
            else:
                rolls[6].append([entry, number]) 

      

for line in fileContent.split("\n"):
    #print(line)
    entry = line.split(" ")[0]
    number = line.split(" ")[1]
    getEntryValue(entry, number)

idtem = 0
for roll in rolls:
    print("|------------------------" + str(idtem) + "------------------------|")
    idtem+=1
    for line in roll:
        print(line)