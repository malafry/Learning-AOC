# Advent of Code
# Day 8 - Part 2
# Source: https://adventofcode.com/2023/day/8#part2

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-8-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setup(input, begin_char, network_map, ghosts):
    for node in input[2:]:
        key = node.split('=')[0].strip()
        value_left = node.split('=')[1].split(',')[0].strip(' (')
        value_right = node.split('=')[1].split(',')[1].strip(' )')
        network_node = {key: [value_left, value_right]}
        network_map.append(network_node)
    for node in network_map:
        node_key = list(node.keys())[0]
        if begin_char in node_key:
            ghosts.append({'start': node_key, 'current': node_key, 'status': False})

def run(instructions, network_map, ghosts, step):  
    continue_loop = True
    for dir in instructions:
        for ghost in ghosts:
            if dir == 'L':
                # location = network_map[location][0]
                ghost['current'] = updateLoc(0, ghost['current'], network_map)
                step += 1
            if dir == 'R':
                # location = network_map[location][1]
                ghost['current'] = updateLoc(1, ghost['current'], network_map)
                step += 1
            if 'Z' in ghost['current']:
                ghost['status'] = True
            
        checkLoc(ghosts, step, continue_loop)
    
    if continue_loop:
        run(instructions, network_map, ghosts, step)

def updateLoc(dir, location, network_map):
    for network_node in network_map:
        if location in network_node.keys():
            return network_node[location][dir]

def checkLoc(ghosts, step, continue_loop):
    for ghost in ghosts:
        if ghost['status'] == False:
            break
        else:
            print("Total steps: {}".format(step))
            continue_loop = False

## ENGINE
begin_char = 'A' # A sample, Z real
instructions = list(input[0])
network_map = list()
ghosts = list()
step = int()
setup(input, begin_char, network_map, ghosts)
run(instructions, network_map, ghosts, step)