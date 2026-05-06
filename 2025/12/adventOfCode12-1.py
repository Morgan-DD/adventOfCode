#
# Advent of code 12-1
#
import os
import sys
from PIL import Image
script_folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
lineFilePath = script_folder_path + "\\data.txt"
fileContent = open(lineFilePath).read()

def getForm(initialChar):
    charsToCheck = [initialChar]
    charsCheked = []
    for charToCheck in charsToCheck:
        charsCheked += charToCheck
        results = getNearChar(charToCheck, charsCheked)
        for result in results:
            if not result in charsToCheck:
                charsToCheck += result

def getNearChar(charToFind, alreadyDoneChar):
    sameChar = []
    CharXPos = charToFind[0]
    CharYPos = charToFind[1]
    print(charToFind)
    refCharToCheck = fileContent.splitlines()[CharXPos][CharYPos]
    if CharXPos-1 >= 0:
        if fileContent.splitlines()[CharYPos][CharXPos-1] == refCharToCheck:
            sameChar += [[CharXPos-1,CharYPos]]
            print("←")
    if CharXPos+1 < len(fileContent.splitlines()[0]):
        if fileContent.splitlines()[CharYPos][CharXPos+1] == refCharToCheck:
            sameChar += [[CharXPos+1,CharYPos]]
            print("→")
    if CharYPos-1 >= 0:
        if fileContent.splitlines()[CharYPos-1][CharXPos] == refCharToCheck:
            sameChar += [[CharXPos,CharYPos-1]]
            print("↑")
    if CharYPos+1 < len(fileContent.splitlines()):
        if fileContent.splitlines()[CharYPos+1][CharXPos] == refCharToCheck:
            sameChar += [[CharXPos,CharYPos+1]]
            print("↓")
    return sameChar

def valueOnArray(_value, _array):
    for _arrayItem in _array:
        # print(_value)
        # print(_array)
        if _arrayItem == _value:
            return True
    return False

def makeImages(pixelsToColor):
    print(pixelsToColor)
    imgMultiplierAlt = 5

    imAlt = Image.new(mode="RGB",
                   size=(len(fileContent.split("\n")[0]) * imgMultiplierAlt, len(fileContent.split("\n") * imgMultiplierAlt)))

    for pixel in pixelsToColor:
        for lineIdAlt in range(imgMultiplierAlt):
            for columnAlt in range(imgMultiplierAlt):
                imAlt.putpixel((pixel[0]*imgMultiplierAlt+lineIdAlt,pixel[1]*imgMultiplierAlt+columnAlt), (255,0,0))


imgMultiplier = 5

im = Image.new(mode="RGB", size=(len(fileContent.split("\n")[0])*imgMultiplier, len(fileContent.split("\n")*imgMultiplier)))

showImage = True

scriptMod = False

colors_rgb = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (0, 255, 255),   # Cyan
    (255, 0, 255),   # Magenta
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (255, 192, 203), # Pink
    (165, 42, 42),   # Brown
    (128, 128, 128), # Gray
    (0, 0, 0),       # Black
    (255, 255, 255), # White
    (50, 205, 50),   # Lime
    (128, 128, 0),   # Olive
    (0, 128, 128),   # Teal
    (0, 0, 128),     # Navy
    (255, 215, 0),   # Gold
    (255, 127, 80),  # Coral
    (250, 128, 114), # Salmon
    (64, 224, 208),  # Turquoise
    (75, 0, 130),    # Indigo
    (245, 245, 220), # Beige
    (189, 252, 201), # Mint
    (230, 230, 250), # Lavender
    (220, 20, 60),   # Crimson
]


idPerLetter = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0,
    "Z":0
}

formFounded = []

tempForm = []

y = 0
x = 0
nbBorders = 0

actualChar = [0,0]

if scriptMod:
    for line in fileContent.splitlines():
        x = 0
        # print(line)
        for char in line:
            nbBorders = 0
            for lineId in range(imgMultiplier):
                for column in range(imgMultiplier):
                    im.putpixel((x*imgMultiplier+lineId,y*imgMultiplier+column), colors_rgb[ord(char) - 65])
                try:
                    if line[x+1] != char:
                        nbBorders+=1
                except:
                    pass
                try:
                    if line[x-1] != char:
                        nbBorders+=1
                except:
                    pass
                try:
                    if fileContent.splitlines()[y+1][x] != char:
                        nbBorders+=1
                except:
                    pass
                try:
                    if fileContent.splitlines()[y-1][x] != char:
                        nbBorders+=1
                except:
                    pass

            # idPerLetter[char]+=[[x,y]]
            x+=1
        y+=1
else:
    for line in fileContent.splitlines():
        x = 0
        for char in line:
            actualChar = [x,y]
            x+=1
        y+=1

getForm([1,1])

# print(idPerLetter)

# for letter, ids in idPerLetter.items():
    # print(letter)
    # print(ids)

if showImage:
    im.show()