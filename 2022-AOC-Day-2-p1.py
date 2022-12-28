# Advent of Code
# Day 2 - Part 1
# Source: https://adventofcode.com/2022/day/2

## Imports
import openpyxl
import operator as op

## Setup and assignments
wb = openpyxl.load_workbook(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-2-Puzzle-input.xlsx')
ws = wb['Sheet1']

## Import data into a Python list
list1 = []
for row in ws.values:
    for value in row:
        list1.append(value)

## Scoring guide
'''
A X = 1 + 3 = 4
A Y = 2 + 6 = 8
A Z = 3 + 0 = 3
B X = 1 + 0 = 1
B Y = 2 + 3 = 5
B Z = 3 + 6 = 9
C X = 1 + 6 = 7
C Y = 2 + 0 = 2
C Z = 3 + 3 = 6
'''
totalValue = 0
totalValue = (op.countOf(list1, "A X") * 4) + (op.countOf(list1, "A Y") * 8) + (op.countOf(list1, "A Z") * 3) + (op.countOf(list1, "B X") * 1) + (op.countOf(list1, "B Y") * 5) + (op.countOf(list1, "B Z") * 9) + (op.countOf(list1, "C X") * 7) + (op.countOf(list1, "C Y") * 2) + (op.countOf(list1, "C Z") * 6)
print(totalValue)

## Tests
#print(list1)
#print(len(list1[1]))
