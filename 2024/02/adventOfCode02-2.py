#
# Advent of code 02-2
#
import os
import sys


def CheckLine(_line, _SecondTry):
    # print("_SecondTry: " + str(_SecondTry))
    # print("_line: " + " ".join(_line))
    _Increase = True
    _Error = 0
    _ErrorsIds = []
    for tempi in range(0, len(_line)):
        _TempLine = _line[:tempi] + _line[tempi+1:]
        for i in range(0, len(_TempLine)):
            if i>0:
                if int(_TempLine[i]) > int(_TempLine[i-1]) and _Increase:
                    if not ((int(_TempLine[i]) - int(_TempLine[i-1])) in [1,2,3]):
                        _Error+=1
                        _ErrorsIds.extend([i])
                elif int(_TempLine[i]) < int(_TempLine[i-1]) and not _Increase:
                    if not ((int(_TempLine[i-1]) - int(_TempLine[i])) in [1,2,3]):
                        _Error+=1
                        _ErrorsIds.extend([i])
                else:
                    _Error+=1
                    _ErrorsIds.extend([i])
            else:
                if int(_TempLine[i+1]) < int(_TempLine[i]):
                    _Increase = False

        if _Error<1:
            return True
        elif _Error==1 and _SecondTry and False:
            for _ErrorId in _ErrorsIds:
                _testLine = _line
                del _testLine[_ErrorId]
                if CheckLine(_testLine, False):
                    # print(_ErrorsIds)
                    # print(_line)
                    return True
            return False
        else:
            return False

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
data = open(dataFilePath).read().split("\n")

NbSafeReport = 0
NbNotSafeReport = 0
isLineSafe = True
Error = 0

Increase = True
LC = 0
for line in data:
    Error = 0
    _TempLine = line.split(" ")
    if CheckLine(_TempLine, True):
        NbSafeReport += 1
    else:
        print(line)
        NbNotSafeReport += 1


print("Number of Safe Reports: " + str(NbSafeReport))
print("Number of Unsafe Reports: " + str(NbNotSafeReport))