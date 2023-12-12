# Advent of Code
# Day 6 - Part 2
# Source: https://adventofcode.com/2023/day/6#part2

## SETUP
import pathlib

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-6-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

time_str = input[0].split(':')[1].strip().split()
time_int = int("".join(time_str))
print("Time: {}".format(time_int)) # TEST

record_distance_str = input[1].split(':')[1].strip().split()
record_distance_int = int("".join(record_distance_str))
print("Record distance:{}".format(record_distance_int)) # TEST

raceData = {'time': time_int, 'record_distance': record_distance_int}

def distance(time, record_distance):
    wins = set()
    for time_held in range(time):
        distance = time_held * (time - time_held)
        if distance > record_distance:
            wins.add(time_held)
    print(len(wins))

## ENGINE
distance(raceData['time'], raceData['record_distance'])