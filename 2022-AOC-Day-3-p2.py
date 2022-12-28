# Advent of Code
# Day 3 - Part 2
# Source: https://adventofcode.com/2022/day/3#part2

## Imports
import string

## Setup and assignments

## Import data into a list
list = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-3-Puzzle-input.txt') as file:
    for line in file.readlines():
        list.append(line.replace('\n', ''))

## Separate items into a dictionary; two values (compartments) to a key (bag)
listSplit = {}
iCounter = 1
kCounter = 0
for i in range(len(list)):
    if iCounter == 1:
        iCounter = iCounter + 1
        item1 = list[i]
    elif iCounter == 2:
        iCounter = iCounter + 1
        item2 = list[i]
    else:
        iCounter = iCounter + 1
        item3 = list[i]

        iCounter = 1
        kCounter = kCounter + 1
        listSplit[kCounter] = [item1, item2, item3]

## Compare a key's two values for character intersects and add to list
listOverlap = []
def intersection(a, b, c):
    itemCompABC = [x for x in a if x in b and x in c]
    listOverlap.append(str(itemCompABC[0]))

for k,v in listSplit.items():
    itemCompA = [x for x in v[0]]
    itemCompB = [x for x in v[1]]
    itemCompC = [x for x in v[2]]
    intersection(itemCompA, itemCompB, itemCompC)

## Prioritize items
guideFinal = dict.fromkeys(string.ascii_lowercase, 0)
guideTemp = dict.fromkeys(string.ascii_uppercase, 0)
guideFinal.update(guideTemp)

updateV = 0
for k,v in guideFinal.items():
    updateV = updateV + 1
    guideFinal.update({k: updateV})
  
## Sum of priorities
sumPri = 0
for x in listOverlap:
    sumPri = sumPri + int(guideFinal.get(x))

## Test
#print(list)
#print(item1)
#print(item1Len)
#print(listSplit)
#print(listOverlap)
#print(itemCompA)
#print(itemCompB)
#print(itemCompAB)
#print(listSplit[1][0])
#print(len(list))
#print(len(listOverlap)) # Should be 300, but is currently 90,000 (300x300)
#print(guideFinal)
print(sumPri)