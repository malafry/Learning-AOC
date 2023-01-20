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

'''COMMENTS: Logic working with new functions; adapt to up and down next, but first figure out right function problem (see below)'''

def treeCheckerLeft(treeRow, treeCol, treeHeight):
    forestSlice = []
    forestSlice[:] = forest[treeRow][:treeCol] # NOTE: [:treeCol] looks left
    forestSliceConverted = list(map(int, forestSlice))
    print('LEFT - {} is max of {}.'.format(max(forestSliceConverted), forestSliceConverted)) ## TEST
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        print('LEFT - TH {} <= maxH {}. FALSE (= hidden).\n'.format(treeHeight, maxH)) ## TEST
        return False # "Is it visible? False: Not visible."
    else:
        print('LEFT - TH {} is not <= maxH {}. TRUE (= visible).\n'.format(treeHeight, maxH)) ## TEST
        return True # "Is it visible? True: Visible."

'''COMMENTS: CURRENT problem: the slice [treeCol:] includes the tree under inspection;
the slice above [:treeCol] excludes the tree under inspection based on syntax, which avoids the problem of self reference;
need to determine how to resolve this issue'''

def treeCheckerRight(treeRow, treeCol, treeHeight):
    forestSlice = []
    forestSlice[:] = forest[treeRow][treeCol:] # NOTE: [treeCol:] looks right - [(int(treeCol) + 1):] may work, instead of del statement
    del forestSlice[0] # NOTE: Can adjust the forestSlice above, maybe -- both are causing the same max() arg empty error
    forestSliceConverted = list(map(int, forestSlice))
    print('RIGHT - {} is max of {}.'.format(max(forestSliceConverted), forestSliceConverted)) ## TEST
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        print('RIGHT - TH {} <= maxH {}. FALSE (= hidden).\n'.format(treeHeight, maxH)) ## TEST
        return False
    else:
        print('RIGHT - TH {} is not <= maxH {}. TRUE (= visible).\n'.format(treeHeight, maxH)) ## TEST
        return True

def treeCheckerUp(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]#[:treeCol]
    forestSlice[:] = forestSliceFull[:treeRow] # NOTE: [:treeRow] looks up (over rows, not across columns)
    forestSliceConverted = list(map(int, forestSlice))
    print('UP - {} is max of {}.'.format(max(forestSliceConverted), forestSliceConverted)) ## TEST
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        print('UP - TH {} <= maxH {}. FALSE (= hidden).\n'.format(treeHeight, maxH)) ## TEST
        return False
    else:
        print('UP - TH {} is not <= maxH {}. TRUE (= visible).\n'.format(treeHeight, maxH)) ## TEST
        return True

def treeCheckerDown(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]#[:treeCol]
    forestSlice[:] = forestSliceFull[treeRow:] # NOTE: [:treeRow] looks down (over rows, not across columns)
    del forestSlice[0]
    forestSliceConverted = list(map(int, forestSlice))
    print('DOWN - {} is max of {}.'.format(max(forestSliceConverted), forestSliceConverted)) ## TEST
    maxH = max(forestSliceConverted)
    if treeHeight <= maxH:
        print('DOWN - TH {} <= maxH {}. FALSE (= hidden).\n'.format(treeHeight, maxH)) ## TEST
        return False
    else:
        print('DOWN - TH {} is not <= maxH {}. TRUE (= visible).\n'.format(treeHeight, maxH)) ## TEST
        return True

## FUNCTION CALLS ##
for row in range(1, (len(forest) - 1)): ## NOTE: May need to subtract 1 from len(forest) to exclude bottom row
    for col in range(1, (len(forest[row]) - 1)):
        treeRow = row
        treeCol = col
        treeHeight = int(forest[row][col])
        print('R: {}, C: {}, H: {}.'.format(treeRow, treeCol, treeHeight)) ## TEST
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
# Legacy code
'''
    for i in range(len(forestSlice[:treeCol])):
        print('LEFT: {} - forestSlice: {}.'.format(i, forestSlice[:treeCol])) ## TEST
        print('{} compared to {}.'.format((forestSlice[i]), treeHeight)) ## TEST
        if treeHeight <= int(forestSlice[i]):
            treeHidden += 1
            print('treeHidden +1 because {} <= {}.'.format({treeHeight}, {forestSlice[i]}))
            continue
        else:
            print('visible because {} is > {}.'.format({treeHeight}, {forestSlice[i]}))
            continue
    if treeHidden > 0:
        return False
    else:
        return True

def treeCheckerRight(treeRow, treeCol, treeHeight):
    treeHidden = 0
    forestSliceRev = forest[treeRow][1:-1:-1]

    for i in range(len(forestSliceRev[:treeCol])):
        print('RIGHT: {} - forestSliceRev: {}.'.format(i, forestSliceRev[:treeCol])) ## TEST
        if treeHeight <= int(forestSliceRev[i]):
            treeHidden += 1
            continue
        else:
            continue
    if treeHidden > 0:
        return False
    else:
        return True

def treeCheckerUp(treeRow, treeCol, treeHeight):
    treeHidden = 0
    forestSlice = ''
    for row in range(len(forest)):
        forestSlice += forest[row][treeCol][1:-1]
    print('UP1 - forestSlice: {}.'.format(forestSlice)) ## TEST
    
    for i in range(len(forestSlice[:treeCol])):
        print('UP2: {} - forestSlice: {}.'.format(i, forestSlice[:treeCol])) ## TEST
        if treeHeight <= int(forestSlice[i]):
            treeHidden += 1
            continue
        else:
            continue
    if treeHidden > 0:
        return False
    else:
        return True

def treeCheckerDown(treeRow, treeCol, treeHeight):
    treeHidden = 0
    forestSlice = ''
    global visible
    visible += 1
    for row in range(len(forest)):
        forestSlice += forest[row][treeCol][1:-1]
    forestSliceRev = forestSlice[::-1]
    print('DOWN1a - forestSlice: {}.'.format(forestSlice)) ## TEST
    print('DOWN1b - forestSliceRev: {}.'.format(forestSliceRev)) ## TEST

    for i in range(len(forestSliceRev[:treeCol])):
        print('DOWN2 - forestSlice: {}.'.format(forestSlice)) ## TEST
        if treeHeight <= int(forestSliceRev[i]):
            treeHidden += 1
            continue
        else:
            continue
    if treeHidden > 0:
        return False
    else:
        return True
'''