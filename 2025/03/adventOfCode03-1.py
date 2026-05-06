#
# Advent of code 03-1
#
import os
import sys
import re

script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
data = open(dataFilePath).read()

total = 0

regex = r'(mul\(([0-9]+)\,([0-9]+)\))'

matchingMul = re.findall(regex, data)

for mul in matchingMul:
    total += int(mul[1])*int(mul[2])

print("Total: " + str(total))