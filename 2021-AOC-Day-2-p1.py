# Advent of Code
# 2021 - Day 2 - Part 1
# Source: https://adventofcode.com/2021/day/2

## IMPORTS ##
import re
my_file = (r'2021 AOC\2021-AOC-Day-2-Puzzle-input.txt')
with open(my_file, "r") as file:
    data = [line.strip() for line in file]

## ENGINES ##
instructions = []
def instructionEngine(list):
    for i in range(len(list)):
        value = re.search(r'\d+', list[i])
        if 'forward' in list[i]:
            instructions.append(['forward', int(value.group())])
        if 'down' in list[i]:
            instructions.append(['down', int(value.group())])
        if 'up' in list[i]:
            instructions.append(['up', int(value.group())])
    
moveHorizontal = 0
moveDepth = 0
def movementEngine(list):
    global moveHorizontal
    global moveDepth
    for i in range(len(list)):
        if list[i][0] == "forward":
            moveHorizontal += list[i][1]
        if list[i][0] == "down":
            moveDepth += list[i][1]
        if list[i][0] == "up":
            moveDepth -= list[i][1]

def valueEngine(hor, dep):
    print(hor * dep) # Correct answer: 1868935

def callEngine():
    instructionEngine(data)
    movementEngine(instructions)
    valueEngine(moveHorizontal, moveDepth)

## RUN ##
callEngine()

## PSEUDO ##
'''
> Take input and create a list (data) where each command is its own element
> Declare two types of variables: depth and horizontal
> Create a function to interpret each instruction (list index)
    > Create a nested list
        > The command is the first index of a nested list
        > The amount is the second index of a nested list
> Create a function to interpret the nested list
    > Forward adds to the Horizontal variable
    > Down adds to the Depth variable
    > Up subtracts from the Depth variable
> Return the multiplication of Horizonal and Depth variables.
'''
