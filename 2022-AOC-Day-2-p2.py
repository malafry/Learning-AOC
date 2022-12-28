# Advent of Code
# Day 2 - Part 2
# Source: https://adventofcode.com/2022/day/2#part2

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
A X = 3 + 0 = 3
A Y = 1 + 3 = 4
A Z = 2 + 6 = 8
B X = 1 + 0 = 1
B Y = 2 + 3 = 5
B Z = 3 + 6 = 9
C X = 2 + 0 = 2
C Y = 3 + 3 = 6
C Z = 1 + 6 = 7
'''
totalValue = 0
totalValue = (op.countOf(list1, "A X") * 3) + (op.countOf(list1, "A Y") * 4) + (op.countOf(list1, "A Z") * 8) + (op.countOf(list1, "B X") * 1) + (op.countOf(list1, "B Y") * 5) + (op.countOf(list1, "B Z") * 9) + (op.countOf(list1, "C X") * 2) + (op.countOf(list1, "C Y") * 6) + (op.countOf(list1, "C Z") * 7)
print(totalValue)

## Tests
#print(list1)
#print(len(list1[1]))