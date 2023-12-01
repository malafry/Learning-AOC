# Advent of Code
# Day 1 - Part 1
# Source: https://adventofcode.com/2023/day/1

## Imports
import pathlib
import re

## Setup and assignments
input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-1-Puzzle-input.txt'

with open(input, "r") as file:
    data = [line.strip() for line in file]

sum = 0

for i in range(len(data)):
    data[i] = re.findall(r"\d+", data[i])
    data[i] = ''.join(data[i])
    dataEnds = str(data[i][0]) + str(data[i][-1])
    sum += (int(dataEnds))

print(sum)