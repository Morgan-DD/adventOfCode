#
# Advent of code 01
#
import os
import sys
import re
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
datas = open(dataFilePath).read()
finalNumber=0

# part one
datas=datas.split("\n")
for data in datas:
    number = re.sub("[A-z]","",data)
    number = int(number[0]) * 10 + int(number[-1])
    finalNumber=finalNumber+number
print(finalNumber)

#part two
finalNumber=0
for data in datas:
    print(data)
    data=data.replace("one", "1")
    data=data.replace("two", "2")
    data=data.replace("three", "3")
    data=data.replace("four", "4")
    data=data.replace("five", "5")
    data=data.replace("six", "6")
    data=data.replace("seven", "7")
    data=data.replace("eight", "8")
    data=data.replace("nine", "9")
    number = re.sub("[A-z]","",data)
    number = int(number[0]) * 10 + int(number[-1])
    print(number)
    finalNumber=finalNumber+number
print("----------")
print(finalNumber)
