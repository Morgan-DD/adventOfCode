#
# Advent of code 05-2
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

def getRulesForUpdate(_update):
    _allRulesForUpdate = []
    for _number in _update.split(","):
        _tempRules = getAllRules(_number)
        # print(_tempRules)
        for _tempRule in _tempRules:
            if _tempRule.split("|")[0] in _update and _tempRule.split("|")[1] in _update:
                _allRulesForUpdate+=[_tempRule]
    return _allRulesForUpdate

def checkLine(line):
    isLineRight = True
    rulesWrong = []
    for pageUpdate in update.split(","):
        matches = 0
        numberOfRulesTrue = 0
        allRules = getAllRules(pageUpdate)
        for singleRule in allRules:
            charZero = re.escape(singleRule.split('|')[0])
            charOne = re.escape(singleRule.split('|')[1])
            if charOne in update and charZero in update:
                numberOfRulesTrue += 1
                regex = r"(" + charZero + r"\,.*?" + charOne + r")"
                if len(re.findall(regex, update)) > 0:
                    matches += 1
                else:
                    rulesWrong+=[singleRule]
        if not (matches == numberOfRulesTrue):
            isLineRight = False
    return isLineRight

# print(rules)
matches = 0
numberOfRulesTrue = 0
areAllNumberRights = True
updateId = 0
nbUpdates = len(updates.split("\n"))
print("Doing Stuff...")
rulesChecked = []
for update in updates.split("\n"):
    rulesChecked = []
    print(str(updateId) + "/" + str(nbUpdates))
    if not checkLine(update):
        joinedNewLine = update
        while True:
            print("--------------")
            rulesForUpdate = getRulesForUpdate(joinedNewLine)
            newLine = []
            for ruleForUpdate in rulesForUpdate:
                if not ruleForUpdate in rulesChecked:
                    print(rulesChecked)
                    NoOne = ruleForUpdate.split("|")[0]
                    NoTwo = ruleForUpdate.split("|")[1]
                    if not NoOne in newLine and NoTwo in newLine:
                        newLine = [NoOne] + newLine
                    elif not NoOne in newLine:
                        newLine+=[NoOne]
                    if not NoTwo in newLine:
                        newLine+=[NoTwo]
                rulesChecked+= [ruleForUpdate]
            joinedNewLine = ','.join(newLine)
            if checkLine(joinedNewLine):
                print(joinedNewLine)
                total+=int(joinedNewLine.split(",")[math.floor(len(joinedNewLine.split(","))/2)])
                break
            else:
                print(joinedNewLine + " FALSE")
                update=joinedNewLine

print("total: " + str(total))
# > 3974
# > 4112