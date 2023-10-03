# Advent of Code
# 2021 - Day 1 - Part 1
# Source: https://adventofcode.com/2021/day/1

## IMPORTS ##
my_file = (r'2021 AOC\2021-AOC-Day-1-Puzzle-input.txt')
with open(my_file, "r") as file:
    data = [int(line.strip()) for line in file]

## SETUP
depthInc = 0

## ENGINE
for num in range(len(data)):
    if num == 0:
        continue
    if data[num] > data[num - 1]:
        depthInc += 1

## RESULT
print(depthInc)
