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
    print('LEFT ##') ## TEST
    forestSlice = []
    forestSlice[:] = forest[treeRow][:treeCol] # NOTE: [:treeCol] looks left
    print('--forestSlice: {}'.format(forestSlice)) ## TEST
    forestSliceConverted = list(map(int, forestSlice)) # NOTE: Converts to a list of integers via map
    print('--forestSliceConverted: {}'.format(forestSliceConverted)) ## TEST
    forestSliceConvertedRev = forestSliceConverted[::-1] # Reversed list to prep for iteration
    print('--forestSliceConvertedRev: {}'.format(forestSliceConvertedRev)) ## TEST
    for i in range(len(forestSliceConvertedRev)):
        if len(forestSliceConvertedRev) == 1:
            print('-- (1) length {}'.format(len(forestSliceConvertedRev[:(i+1)]))) ## TEST
            return len(forestSliceConvertedRev)
        elif treeHeight > forestSliceConvertedRev[i]:
            print('-- (2) TH {} > i {}'.format(treeHeight, forestSliceConvertedRev[i])) ## TEST
            if i == (len(forestSliceConvertedRev) - 1):
                print('-- (2a) TH {} sees over {} trees to edge'.format(treeHeight, len(forestSliceConvertedRev[:(i+1)]))) ## TEST
                return len(forestSliceConvertedRev)
                break
            else:
                continue
            continue
        else:
            print('-- (3) length {}'.format(len(forestSliceConvertedRev[:(i+1)]))) ## TEST
            return len(forestSliceConvertedRev[:(i+1)])
            break

def treeCheckerRight(treeRow, treeCol, treeHeight):
    print('RIGHT ##') ## TEST
    forestSlice = []
    forestSlice[:] = forest[treeRow][treeCol:] # NOTE: [treeCol:] looks right
    del forestSlice[0] # NOTE: Line required given syntax ([treeCol:] v [:treeCol])
    print('--forestSlice: {}'.format(forestSlice)) ## TEST
    forestSliceConverted = list(map(int, forestSlice)) # NOTE: Converts to a list of integers via map
    print('--forestSliceConverted: {}'.format(forestSliceConverted)) ## TEST
    for i in range(len(forestSliceConverted)):
        if len(forestSliceConverted) == 1:
            print('-- (1) length {}'.format(len(forestSliceConverted[:(i+1)]))) ## TEST
            return len(forestSliceConverted)
        elif treeHeight > forestSliceConverted[i]:
            print('-- (2) TH {} > i {}'.format(treeHeight, forestSliceConverted[i])) ## TEST
            if i == (len(forestSliceConverted) - 1):
                print('-- (2a) TH {} sees over {} trees to edge'.format(treeHeight, len(forestSliceConverted[:(i+1)]))) ## TEST
                return len(forestSliceConverted)
                break
            else:
                continue
            continue
        else:
            print('-- (3) length {}'.format(len(forestSliceConverted[:(i+1)]))) ## TEST
            return len(forestSliceConverted[:(i+1)])
            break

def treeCheckerUp(treeRow, treeCol, treeHeight):
    print('UP ##') ## TEST
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[:treeRow] # NOTE: [:treeRow] looks up (over rows, not across columns)
    print('--forestSlice: {}'.format(forestSlice))
    forestSliceConverted = list(map(int, forestSlice))
    print('--forestSliceConverted: {}'.format(forestSliceConverted))
    forestSliceConvertedRev = forestSliceConverted[::-1] # Reversed list to prep for iteration
    print('--forestSliceConvertedRev: {}'.format(forestSliceConvertedRev)) ## TEST
    for i in range(len(forestSliceConvertedRev)):
        if len(forestSliceConvertedRev) == 1:
            print('-- (1) length {}'.format(len(forestSliceConvertedRev[:(i+1)]))) ## TEST
            return len(forestSliceConvertedRev)
        elif treeHeight > forestSliceConvertedRev[i]:
            print('-- (2) TH {} > i {}'.format(treeHeight, forestSliceConvertedRev[i])) ## TEST
            if i == (len(forestSliceConvertedRev) - 1):
                print('-- (2a) TH {} sees over {} trees to edge'.format(treeHeight, len(forestSliceConvertedRev[:(i+1)]))) ## TEST
                return len(forestSliceConvertedRev)
                break
            else:
                continue
            continue
        else:
            print('-- (3) length {}'.format(len(forestSliceConvertedRev[:(i+1)]))) ## TEST
            return len(forestSliceConvertedRev[:(i+1)])
            break

def treeCheckerDown(treeRow, treeCol, treeHeight):
    print('DOWN ##') ## TEST
    forestSliceFull = []
    forestSlice = []
    for row in range(len(forest)):
        forestSliceFull += forest[row][treeCol]
    forestSlice[:] = forestSliceFull[treeRow:] # NOTE: [treeRow:] looks down (over rows, not across columns)
    del forestSlice[0] # NOTE: Line required given syntax ([treeCol:] v [:treeCol])    
    print('--forestSlice: {}'.format(forestSlice))
    forestSliceConverted = list(map(int, forestSlice))
    print('--forestSliceConverted: {}'.format(forestSliceConverted))
    for i in range(len(forestSliceConverted)):
        if len(forestSliceConverted) == 1:
            print('-- (1) length {}'.format(len(forestSliceConverted[:(i+1)]))) ## TEST
            return len(forestSliceConverted)
        elif treeHeight > forestSliceConverted[i]:
            print('-- (2) TH {} > i {}'.format(treeHeight, forestSliceConverted[i])) ## TEST
            if i == (len(forestSliceConverted) - 1):
                print('-- (2a) TH {} sees over {} trees to edge'.format(treeHeight, len(forestSliceConverted[:(i+1)]))) ## TEST
                return len(forestSliceConverted)
                break
            else:
                continue
            continue
        else:
            print('-- (3) length {}'.format(len(forestSliceConverted[:(i+1)]))) ## TEST
            return len(forestSliceConverted[:(i+1)])
            break

'''
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
'''
## FUNCTION CALLS ##
scenicScoreTotals = []
for row in range(1, (len(forest) - 1)):
    for col in range(1, (len(forest[row]) - 1)):
        treeRow = row
        treeCol = col
        treeHeight = int(forest[row][col])
        print('# LOC - R: {}, C: {}, H: {}.'.format(treeRow, treeCol, treeHeight)) ## TEST
        viewL = treeCheckerLeft(treeRow, treeCol, treeHeight)
        viewR = treeCheckerRight(treeRow, treeCol, treeHeight)
        viewU = treeCheckerUp(treeRow, treeCol, treeHeight)
        viewD = treeCheckerDown(treeRow, treeCol, treeHeight)
        # NOTE: Could express as viewL, viewR, viewU, viewD = treeCheckerLeft(treeRow, treeCol, treeHeight), treeCheckerRight(treeRow, treeCol, treeHeight), treeCheckerUp(treeRow, treeCol, treeHeight), treeCheckerDown(treeRow, treeCol, treeHeight)
        
        scenicScore = viewL * viewR * viewU * viewD
        scenicScoreTotals.append(scenicScore)
        print('## Scenic score: {}\n'.format(scenicScore))

## EDGE COUNT ##
'''COMMENTS: Don't know how to consider edges; functions are called only for interior trees'''

## OUTPUT ##
'''COMMENTS: Need to take the individual scenicScore from function calls to compare and find largest'''
#print('Visible trees: {}.\nHidden trees: {}.'.format(visible, notVisible)) ## NOTE: Will need to change.
print(max(scenicScoreTotals))

## FEEDBACK ##

## COMMENTS ##