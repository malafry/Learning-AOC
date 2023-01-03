# Advent of Code
# Day 5 - Part 1
# Source: https://adventofcode.com/2022/day/5

## Imports
import re

## Setup
list = []
with open(r'C:\Users\malaf\OneDrive\Desktop\Workspace\Code\Learning\2022 AOC\2022-AOC-Day-5-Puzzle-input.txt') as file:
    for line in file.readlines():
        list.append(line.replace('\n', ''))

## Make data manageable  
stacks = []
for i in range(0,8):
    for ii in range(1,35,4):
        stacks.append(list[i][ii])
#print("stacks list: {}".format(stacks)) ## TEST REMOVE

def reverseSubStacks(lst, start, end):
    sublist = lst[start:end]
    sublist.reverse()
    lst[start:end] = sublist

subStacks = []
for i in range(9):
    subStacks.append(stacks[i::9])
    reverseSubStacks(subStacks[i], 0, 9)
#print("subStacks list: {}".format(subStacks)) ## TEST REMOVE

subStacksFinal = dict(zip([*range(1,10)], [[x for x in sublist if x.isalpha()] for sublist in subStacks]))
moves = [x for x in list if 'move' in x]
#print("subStacksFinal list: {}".format(subStacksFinal)) ## TEST REMOVE
#print("moves list: {}".format(moves)) ## TEST REMOVE

## Manipulate data
for i in range(len(moves)):
    move = moveAmount, moveStart, moveEnd = [int(s) for s in re.findall(r'\d+', moves[i])]
    
    ## Identify the moving values
    moveValues = subStacksFinal[moveStart][(len(subStacksFinal[moveStart]) - moveAmount):len(subStacksFinal[moveStart])]
    #print("{}: {}".format(i, moveValues)) ## TEST REMOVE

    ## Modify starting key/stack
    moveWorkspaceStart = {moveStart: subStacksFinal[moveStart][0:(len(subStacksFinal[moveStart]) - moveAmount)]}
    subStacksFinal.update(moveWorkspaceStart)
    #print("{}: {}".format(i, moveWorkspaceStart)) ## TEST REMOVE

    ## Modify ending key/stack
    moveWorkspaceEnd = {moveEnd: ((subStacksFinal[moveEnd][:]) + moveValues)}
    subStacksFinal.update(moveWorkspaceEnd)
    #print("{}: {}".format(i, moveWorkspaceEnd)) ## TEST REMOVE

## Find last value of each key
puzzleInput = []
for i in subStacksFinal:
    puzzleInput.append(subStacksFinal[i][-1])
puzzleInput = ''.join(puzzleInput)

print("These are the values on top of each stack after moves: {}.".format(puzzleInput))

## FEEDBACK ##
#print(moves)
#print(moveValues)
#print(moveWorkspaceStart)
#print(moveWorkspaceEnd)
#print(subStacksFinal)