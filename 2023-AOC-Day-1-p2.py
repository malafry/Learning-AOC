# Advent of Code
# Day 1 - Part 2
# Source: https://adventofcode.com/2023/day/1#part2

## Imports
import pathlib
import re

## Setup and assignments
input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-1-Puzzle-input.txt'

with open(input, "r") as file:
    data = [line.strip() for line in file]

with open(input, "r") as file:
    data2 = [line.strip() for line in file]

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
    print("frontValue for {}: {}".format(i, frontValue))
    return frontValue

def backNum(data, i):
    word = ''
    backValue = ''
    if len(data[i]) == 1:
        backValue = data[i]
    else:
        for l in range(len(data[i])-1,0,-1):
            word = data[i][l] + word # Handles reverse
            for w in range(len(lookUp)):
                if lookUp[w][1] in word:
                    backValue = lookUp[w][1]
                    break
                elif lookUp[w][0] in word:
                    backValue = lookUp[w][1]
                    break
            if backValue != '':
                break
    print("backValue for {}: {}".format(i, backValue))
    return backValue

sum = 0

for i in range(len(data)):
    dataEnds = frontNum(data, i) + backNum(data, i)
    print(dataEnds)
    sum += int(dataEnds)

print(sum) # ANSWER WRONG: 54607 (too high) 53021 (too low)

# TEST LOG
#for i in range(len(data)):
#    print("{} => {} => {}:{}".format(data2[i], data[i], data[i][0], data[i][-1]))

## KEEP
'''for i in range(len(data)):
    word = ''
    for l in range(len(data[i])):
        word += data[i][l]
        for w in range(len(lookUp)):
            if lookUp[w][0] in word:
                word = word.replace(lookUp[w][0], lookUp[w][1])
    data[i] = word
    data[i] = re.findall(r"\d+", data[i])
    data[i] = ''.join(data[i])
    dataEnds = int(str(data[i][0]) + str(data[i][-1]))
    sum += dataEnds'''

## KEEP
'''    for l in range(len(data[i]),0,-1):
        word += data[i][l]
        print(word)
        wordRev = word[::-1]
        print(wordRev)
        for w in range(len(lookUp)):
            if lookUp[w][0] in wordRev:
                wordRev = wordRev.replace(lookUp[w][0], lookUp[w][1])
                print("REV!: {}".format(wordRev))'''