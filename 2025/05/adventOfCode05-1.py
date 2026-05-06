#
# Advent of code 05-1
#
import os
import sys
import re
import math
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
data = open(lineFilePath).read()

rules = data.split("\n\n")[0]
updates = data.split("\n\n")[1]

total = 0

def getAllRules(number):
    allRules = []
    for rule in rules.split("\n"):
        if number in rule:
            allRules+=[rule]
    return allRules


# print(rules)
matches = 0
numberOfRulesTrue = 0
areAllNumberRights = True

for update in updates.split("\n"):
    areAllNumberRights = True
    for pageUpdate in update.split(","):
        matches = 0
        numberOfRulesTrue = 0
        allRules = getAllRules(pageUpdate)
        for singleRule in allRules:
            charZero = re.escape(singleRule.split('|')[0])
            charOne = re.escape(singleRule.split('|')[1])
            if charOne in update and charZero in update:
                numberOfRulesTrue+=1
                regex = r"(" + charZero + r"\,.*?" + charOne + r")"
                if len(re.findall(regex, update)) > 0:
                    matches += 1
        if not (matches == numberOfRulesTrue):
            areAllNumberRights = False
    if areAllNumberRights:
        total+=int(update.split(",")[math.floor(len(update.split(","))/2)])

print("total: " + str(total))
# < 82302
# < 5790
# was 5762