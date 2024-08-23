#
# Advent of code 06
#
import os
import sys
import re
import numpy 
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()
total = 0
