#
# Advent of code 11-1
#
import os
import sys
from fileinput import isfirstline
from os.path import split

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()

rocksLine = fileContent

results = {'0':'1'}

def addToKeyValueArray(array, key, value):
    alreadyExist = False
    for i, arrayValues in array.items():
        if i == key:
            alreadyExist = True
            break
    if not alreadyExist:
        array.setdefault(key,value)
    # print(array)
    return array

def numberOfRock(_rocks, _blink, _results):
    _blinkCounter = 0
    while _blinkCounter <= _blink:
        # print("------------------------------")
        # print(_rocks)
        _tempRocks = ""
        for _rock in _rocks.split(" "):
            _rockDone = False
            for i, _result in _results.items():
                if i == _rock:
                    _tempRocks+=" " + _result
                    _rockDone = True
            if len(_rock)% 2 == 0 and not _rockDone:
                _newNumer = " ".join([str(int(_rock[:len(_rock) // 2])), str(int(_rock[len(_rock) // 2:]))])
                _tempRocks+=" " + _newNumer
                _results = addToKeyValueArray(_results, _rock,_newNumer)
                _rockDone = True
            elif not _rockDone:
                # print(_rock)
                _newNumer = str(int(_rock) * 2024)
                _tempRocks += " " + _newNumer
                _results = addToKeyValueArray(_results, _rock,_newNumer)
        # print(str(_blinkCounter) + "/" + str(_blink))
        _blinkCounter+=1
        _rocks = _tempRocks.lstrip()
        # print(_results)
    return _results, len(_rocks.split(" "))

tmpRocksLine = ""

blinkNeeded = 25
blinkCounter = 1
nbRocks=0
counter = 1
print("Starting...")

for singleRock in rocksLine.split(" "):
    results, nbRocksForRun = numberOfRock(singleRock, blinkNeeded, results)
    nbRocks+=nbRocksForRun
    counter+=1
    print(str(counter) + "/" + str(len(rocksLine.split(" "))))

# print(results)

print("Number of blink: " + str(blinkNeeded))
print("number of rocks: " + str(nbRocks))
print("expected resut:  183435")
# < 192366
# 183435