# Advent of Code
# Day 1
# Source: https://adventofcode.com/2022/day/1

## Imports
import openpyxl

## Setup / Assignments
wb = openpyxl.load_workbook(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-1-Puzzle-input.xlsx')
ws = wb['Sheet1']

## Setup / Structure and variables
cCList = [] # Calorie count list
cCListValues = []
cCDict = {} # Calorie count dictionary
cCDictFinal = {}
cCCount = 0
cCCountElves = 0 # Number of elves / number of keys
cCCountTemp = 0

## Import Excel data into Python for data manipulation
for row in ws.values:
    for value in row:
        cCList.append(value)
cCList.append(None) # Appending value to end of list to support Summation iterative

## Determine the number of unique entities (i.e. elves)
cCCountElves = cCList.count(None)

## Number of elves added to the dictionary
for i in range(cCCountElves):
    cCDict[i+1] = 0

## Summation iterative
for i in range(len(cCList)):
    if type(cCList[i]) == int:
        cCCountTemp += cCList[i]
    else:
        cCListValues.append(cCCountTemp)
        cCCountTemp = 0

# Zipper cCList and cCDict into cCDictFinal
cCDictFinal = dict(zip(cCDict, cCListValues)) # (key, value)

# Find key with maximum value in cCDictFinal
max_val = max(cCDictFinal, key=cCDictFinal.get)
print(max_val, cCDictFinal[max_val])


## Tests
#print(cCList)
#print(cCDict)
#print(cCDictFinal)
#print('There are ' + str(cCCountElves) + ' elves.')
#print('There are ' + str(len(cCListValues)) + ' bags of calories accounted for.')

'''
if cCountElves == len(cCListValues):
    print('All elves accounted for.')
else:
    print('Not all elves are accounted for.')
    if int(cCountElves) > len(cCListValues):
        print('There are ' + int(cCountElves - len(cCListValues)) + ' more elves than data points!')
    elif int(cCountElves) < len(cCListValues):
        print('There are ' + abs(int(cCountElves - len(cCListValues))) + ' more data points than elves!') 
    else:
        break
'''