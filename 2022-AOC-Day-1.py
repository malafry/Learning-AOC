# Advent of Code
# Day 1
# Source: https://adventofcode.com/2022/day/1

## Imports
import openpyxl

## Setup and assignments
wb = openpyxl.load_workbook(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-1-Puzzle-input.xlsx')
ws = wb['Sheet1']

## Import data into a Python list
cCList = []
for row in ws.values:
    for value in row:
        cCList.append(value)

## Determine number of groups (determined by "None" data type, which are empty cells after each group)
cCList.append(None)
cCCountElves = cCList.count(None)

## Create data structure with a Python dictionary ("key" part of key-value pair)
cCDict = {}
for i in range(cCCountElves):
    cCDict[i+1] = 0 # +1 added to adjust keys, accounting for zero-based numbering (i.e. start at 1, not 0)

## Summation iterative
cCListValues = []
cCCountTemp = 0
for i in range(len(cCList)):
    if type(cCList[i]) == int:
        cCCountTemp += cCList[i]
    else:
        cCListValues.append(cCCountTemp)
        cCCountTemp = 0

## Zip cCList and cCDict into cCDictFinal
cCDictFinal = {}
cCDictFinal = dict(zip(cCDict, cCListValues)) # (key, value)

## Find key with maximum value in cCDictFinal
max_val = max(cCDictFinal, key=cCDictFinal.get)
print(max_val, cCDictFinal[max_val])

## Tests
#print(cCList)
#print(cCDict)
#print(cCDictFinal)
