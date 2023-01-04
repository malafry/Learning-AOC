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
    if buffer.count(buffer[0]) > 1 or buffer.count(buffer[1]) > 1 or buffer.count(buffer[2]) > 1 or buffer.count(buffer[3]) > 1:
        return False
    else:
        return True

# Analyze buffer through iteration and function implementation
for i in range(len(list)):
    buffer = list[(i-3):(i+1)]
    if len(buffer) == 4:
        if subRoutineCheck(buffer) == True:
            print("Marker found: {}.".format(buffer))
            print("Location of buffer: {} to {}.".format((i-3),(i+1)))
            print("Number of characters processed: {}.".format((i+1)))
            break
        else:
            continue

print("Last buffer in memory: {}.".format(buffer)) ## TEST - REMOVE

## MANIPULATE DATA ##

## FEEDBACK ##
#print(list)