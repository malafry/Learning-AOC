# Advent of Code
# Day 6 - Part 1
# Source: https://adventofcode.com/2023/day/6

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-6-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

time_str = input[0].split(':')[1].strip().split()
time_int = [int(x) for x in time_str]
distance_str = input[1].split(':')[1].strip().split()
distance_int = [int(x) for x in distance_str]

raceData = {'time': time_int, 'distance': distance_int}

print(raceData)
## ENGINE