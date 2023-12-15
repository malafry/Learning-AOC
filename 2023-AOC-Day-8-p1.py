# Advent of Code
# Day 8 - Part 1
# Source: https://adventofcode.com/2023/day/8

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-8-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setup(input):
    global directions, network
    directions = input[0]
    for node in input[2:]:
        key = node.split('=')[0].strip()
        valueLeft = node.split('=')[1].split(',')[0].strip(' (')
        valueRight = node.split('=')[1].split(',')[1].strip(' )')
        network[key] = [valueLeft, valueRight]

def run(directions, network, location, step):
    for dir in directions[:]:
        if dir == 'L':
            location = network[location][0]
            step += 1
        if dir == 'R':
            location = network[location][1]
            step += 1
        if location == 'ZZZ':
            break
    if location != 'ZZZ':
        run(directions, network, location, step)
    if location == 'ZZZ':
        print(step)

## ENGINE
directions = list()
network = dict()
location = 'AAA'
step = int()
setup(input)
run(directions, network, location, step)