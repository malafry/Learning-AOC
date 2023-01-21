# Advent of Code
# Day 8 - Part 1
# Source: https://adventofcode.com/2022/day/8

## IMPORTS AND SETUP ##
forest = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-8-Puzzle-input.txt') as file:
    for line in file.readlines():
        forest.append(line.replace('\n',''))

## FUNCTIONS ##
visible = 0
notVisible = 0

def treeCheckerLeft(treeRow, treeCol, treeHeight):
    forestSlice = []
    forestSlice[:] = forest[treeRow][:treeCol]
    forestSliceConverted = list(map(int, forestSlice))
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        return False
    else:
        return True

def treeCheckerRight(treeRow, treeCol, treeHeight):
    forestSlice = []
    forestSlice[:] = forest[treeRow][treeCol:]
    del forestSlice[0]
    forestSliceConverted = list(map(int, forestSlice))
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        return False
    else:
        return True

def treeCheckerUp(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[:treeRow]
    forestSliceConverted = list(map(int, forestSlice))
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        return False
    else:
        return True

def treeCheckerDown(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[treeRow:]
    del forestSlice[0]
    forestSliceConverted = list(map(int, forestSlice))
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        return False
    else:
        return True

## FUNCTION CALLS ##
for row in range(1, (len(forest) - 1)):
    for col in range(1, (len(forest[row]) - 1)):
        treeRow = row
        treeCol = col
        treeHeight = int(forest[row][col])
        if treeCheckerLeft(treeRow, treeCol, treeHeight) or treeCheckerRight(treeRow, treeCol, treeHeight) or treeCheckerUp(treeRow, treeCol, treeHeight) or treeCheckerDown(treeRow, treeCol, treeHeight) == True:
            visible += 1
        else:
            notVisible += 1

## EDGE COUNT ##
visible += 98*4

## OUTPUT ##
print('Visible trees: {}.\nHidden trees: {}.'.format(visible, notVisible))

## FEEDBACK ##

## COMMENTS ##
