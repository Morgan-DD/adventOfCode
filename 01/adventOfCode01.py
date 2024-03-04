import shutil
import platform
import os
import glob
import sys
import re
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dataFilePath = script_folder_path + "\\data.txt"
datas = open(dataFilePath).read()
finalNumber=0

datas=datas.split("\n")
for data in datas:
    number = re.sub("[A-z]","",data)
    number = int(number[0]) * 10 + int(number[-1])
    finalNumber=finalNumber+number
print(finalNumber)