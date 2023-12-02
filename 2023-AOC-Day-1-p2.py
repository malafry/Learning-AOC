# Advent of Code
# Day 1 - Part 2
# Source: https://adventofcode.com/2023/day/1#part2

## Imports
import pathlib

## Setup and assignments
input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-1-Puzzle-input.txt'

with open(input, "r") as file:
    data = [line.strip() for line in file]

lookUp = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]

sum = 0

def frontNum(data, i):
    word = ''
    frontValue = ''
    for l in range(len(data[i])):
        word += data[i][l]
        for w in range(len(lookUp)):
            if lookUp[w][1] in word:
                frontValue = lookUp[w][1]
                break
            elif lookUp[w][0] in word:
                frontValue = lookUp[w][1]
                break
        if frontValue != '':
            break
    return frontValue

def backNum(data, i):
    word = ''
    backValue = ''
    for l in range(len(data[i]) - 1,-1,-1):
        word = data[i][l] + word
        for w in range(len(lookUp)):
            if lookUp[w][1] in word:
                backValue = lookUp[w][1]
                break
            elif lookUp[w][0] in word:
                backValue = lookUp[w][1]
                break
        if backValue != '':
            break
    return backValue

sum = 0

for i in range(len(data)):
    dataEnds = frontNum(data, i) + backNum(data, i)
    print("{}: {}".format(i+1, dataEnds))
    sum += int(dataEnds)

print(sum)