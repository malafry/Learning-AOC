# Advent of Code
# Day 4 - Part 1
# Source: https://adventofcode.com/2022/day/4

## Imports

## Setup and assignments
list = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-4-Puzzle-input.txt') as file:
    for line in file.readlines():
        list.append(line.replace('\n', ''))

## Import data into a data structure
assignmentPairs = 0
kCount = 0

for i in range(len(list)):
    # Parse for numbers and setup values for enumeration
    kCount = kCount + 1
    item = list[i].split(',')
    itemA = (item[0]).split('-')
    itemB = (item[1]).split('-')
    
    # Enumerate ranges
    itemRangeA = []
    itemRangeB = []
    for i in range(int(itemA[0]),(int(itemA[1]) + 1)):
        itemRangeA.append(i)
    for i in range(int(itemB[0]),(int(itemB[1]) + 1)):
        itemRangeB.append(i)
    
    # Check and record range overlap (A in B or B in A)
    checkRange = 0
    checkRange = (set(itemRangeA) & set(itemRangeB))
    if len(checkRange) == len(itemRangeA):
        assignmentPairs = assignmentPairs + 1
    elif len(checkRange) == len(itemRangeB):
        assignmentPairs = assignmentPairs + 1
    else:
        continue

    '''
    #### THE PROBLEM IS IN THE VETTING -- TRY TO WORK WITH set() METHOD and compare LENGTH of SET to ranges?
    checkRange = all(item in itemRangeA for item in itemRangeB)
    if checkRange is True:
        assignmentPairs = assignmentPairs + 1
        overlapTestYes.append(kCount) # TEST CODE - REMOVE
    else:
        overlapTestNo.append(kCount) # TEST CODE - REMOVE
        continue

    checkRange = all(item in itemRangeB for item in itemRangeA)
    if checkRange is True:
        assignmentPairs = assignmentPairs + 1
        overlapTestYes.append(kCount) # TEST CODE - REMOVE
    else:
        overlapTestNo.append(kCount) # TEST CODE - REMOVE
        continue
'''
print("Assignment pairs with one complete overlap: {}.".format(str(assignmentPairs)))

## Make data manageable  

## Manipulate data

##

## Test
#print(list)
#print(len(list))
print(itemA)
print(itemB)
print(itemRangeA)
print(itemRangeB)
print(checkRange)
#print(valueRange)
#print(item)
#print(itemA)
#print(itemB)
print(kCount)
'''
print("Overlap Test Yes: {}.".format(overlapTestYes))
print("Overlap Test No: {}.".format(overlapTestNo))
print("/n/n/n")
print(set(overlapTestYes) & set(overlapTestNo))
print(len(set(overlapTestYes) & set(overlapTestNo)))
'''