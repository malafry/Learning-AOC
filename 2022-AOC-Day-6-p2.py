# Advent of Code
# Day 6
# Source: https://adventofcode.com/2022/day/6

## IMPORTS AND SETUP ##
list = ''
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-6-Puzzle-input.txt') as file:
    for line in file.readlines():
        list = line

## MANAGE DATA ##
buffer = []

# Function to analyze buffer
def subRoutineCheck(buffer):
    for i in range(len(buffer)):
        for ii in range(14):
            if buffer.count(buffer[ii]) > 1:
                return False
    else:
        return True

# Analyze buffer through iteration and function implementation
for i in range(len(list)):
    buffer = list[(i-13):(i+1)]
    if len(buffer) == 14:
        if subRoutineCheck(buffer) == True:
            print("Marker found: {}.".format(buffer))
            print("Location of buffer: {} to {}.".format((i-13),(i+1)))
            print("Number of characters processed: {}.".format((i+1)))
            break
        else:
            continue

print("Last buffer in memory: {}.".format(buffer)) ## TEST - REMOVE

## MANIPULATE DATA ##

## FEEDBACK ##
#print(list)