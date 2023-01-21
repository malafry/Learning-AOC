# Advent of Code
# Day 8 - Part 2
# Source: https://adventofcode.com/2022/day/8#part2

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
    forestSliceConvertedRev = forestSliceConverted[::-1]
    for i in range(len(forestSliceConvertedRev)):
        if len(forestSliceConvertedRev) == 1:
            return len(forestSliceConvertedRev)
        elif treeHeight > forestSliceConvertedRev[i]:
            if i == (len(forestSliceConvertedRev) - 1):
                return len(forestSliceConvertedRev)
                break
            else:
                continue
            continue
        else:
            return len(forestSliceConvertedRev[:(i+1)])
            break

def treeCheckerRight(treeRow, treeCol, treeHeight):
    forestSlice = []
    forestSlice[:] = forest[treeRow][treeCol:]
    del forestSlice[0]
    forestSliceConverted = list(map(int, forestSlice))
    for i in range(len(forestSliceConverted)):
        if len(forestSliceConverted) == 1:
            return len(forestSliceConverted)
        elif treeHeight > forestSliceConverted[i]:
            if i == (len(forestSliceConverted) - 1):
                return len(forestSliceConverted)
                break
            else:
                continue
            continue
        else:
            return len(forestSliceConverted[:(i+1)])
            break

def treeCheckerUp(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[:treeRow]
    forestSliceConverted = list(map(int, forestSlice))
    forestSliceConvertedRev = forestSliceConverted[::-1]
    for i in range(len(forestSliceConvertedRev)):
        if len(forestSliceConvertedRev) == 1:
            return len(forestSliceConvertedRev)
        elif treeHeight > forestSliceConvertedRev[i]:
            if i == (len(forestSliceConvertedRev) - 1):
                return len(forestSliceConvertedRev)
                break
            else:
                continue
            continue
        else:
            return len(forestSliceConvertedRev[:(i+1)])
            break

def treeCheckerDown(treeRow, treeCol, treeHeight):
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[treeRow:]
    del forestSlice[0] 
    forestSliceConverted = list(map(int, forestSlice))
    for i in range(len(forestSliceConverted)):
        if len(forestSliceConverted) == 1:
            return len(forestSliceConverted)
        elif treeHeight > forestSliceConverted[i]:
            if i == (len(forestSliceConverted) - 1):
                return len(forestSliceConverted)
                break
            else:
                continue
            continue
        else:
            return len(forestSliceConverted[:(i+1)])
            break

## FUNCTION CALLS ##
scenicScoreTotals = []
for row in range(1, (len(forest) - 1)):
    for col in range(1, (len(forest[row]) - 1)):
        treeRow = row
        treeCol = col
        treeHeight = int(forest[row][col])
        viewL, viewR, viewU, viewD = treeCheckerLeft(treeRow, treeCol, treeHeight), treeCheckerRight(treeRow, treeCol, treeHeight), treeCheckerUp(treeRow, treeCol, treeHeight), treeCheckerDown(treeRow, treeCol, treeHeight)
        scenicScore = viewL * viewR * viewU * viewD
        scenicScoreTotals.append(scenicScore)

## OUTPUT ##
print(max(scenicScoreTotals))

## FEEDBACK ##

## COMMENTS ##
