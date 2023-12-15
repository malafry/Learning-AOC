# Advent of Code
# Day 8 - Part 2
# Source: https://adventofcode.com/2023/day/8#part2

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-8-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setup(input, start, directions, networkStartList):
    directions = input[0]
    network = list()
    for node in input[2:]:
        key = node.split('=')[0].strip()
        valueLeft = node.split('=')[1].split(',')[0].strip(' (')
        valueRight = node.split('=')[1].split(',')[1].strip(' )')
        networkDict[key] = [valueLeft, valueRight]
        tempDict = {key: [valueLeft, valueRight]}
        network.append(tempDict)

    # INIT START LIST - network not used
    for node in network:
        nodeKey = list(node.keys())[0]
        if start in nodeKey:
            networkStartList.append(nodeKey)

def run(directions, networkStartList, step, totalSteps):  
    for i, key in enumerate(networkStartList):
        location = key
        for dir in directions[:]:
            if dir == 'L':
                location = networkDict[location][0]
                print(location) # TEST
                step += 1
            if dir == 'R':
                location = networkDict[location][1]
                print(location) # TEST
                step += 1
            if 'Z' in location:
                networkStartList.pop(i)
                totalSteps.append(step)
                step = int()
                break

    if networkStartList:
        run(directions, networkStartList, step, totalSteps)
    else:
        return(totalSteps)

## ENGINE
start = 'A' # A sample, Z real
directions = list()
networkStartList = list()
step = int()
totalSteps = list()
networkDict = dict()

setup(input, start, directions, networkStartList)
run(directions, networkStartList, step, totalSteps)