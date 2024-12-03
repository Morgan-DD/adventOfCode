#
# Advent of code 02-1
#
import os
import sys

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
data = open(dataFilePath).read().split("\n")

NbSafeReport = 0
NbNotSafeReport = 0
isLineSafe = True

Increase = True
LC = 0
for line in data:
    isLineSafe = True
    Increase = True
    numbers = line.split(" ")
    for i in range(0, len(numbers)):
        if i>0:
            if int(numbers[i]) > int(numbers[i-1]) and Increase:
                if not ((int(numbers[i]) - int(numbers[i-1])) in [1,2,3]):
                    isLineSafe = False
                    # print("/!\\ numbers[i] > numbers[i-1]")
                    break
            elif int(numbers[i]) < int(numbers[i-1]) and not Increase:
                if not ((int(numbers[i-1]) - int(numbers[i])) in [1,2,3]):
                    isLineSafe = False
                    # print("/!\\ numbers[i] < numbers[i-1]")
                    break
            else:
                isLineSafe = False
                break
        else:
            if int(numbers[i+1]) < int(numbers[i]):
                Increase = False

    if isLineSafe:
        NbSafeReport+=1
    else:
        print(line)
        # print(Increase)
        NbNotSafeReport+=1

print("Number of Safe Reports: " + str(NbSafeReport))
print("Number of Unsafe Reports: " + str(NbNotSafeReport))