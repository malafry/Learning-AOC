# Advent of Code
# Day 7 - Part 1
# Source: https://adventofcode.com/2023/day/7

## SETUP
import pathlib
from collections import Counter

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-7-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setupPlays(input):
    global plays
    for i in range(len(input)):
        cardData = {'id': i, 'rank': int(), 'hand': input[i].split()[0], 'type': str(), 'hand_strength': list(), 'bet': int(input[i].split()[1]), 'raw_score': int(), 'score': int()}
        plays.append(cardData)
    
    for i in range(len(plays)):
        handType(plays[i])
        cardStrength(plays[i])

    for i in range(len(plays)):
        plays[i]['raw_score'] = int(''.join(plays[i]['hand_strength']))

def handType(hand):
    handType = Counter(hand['hand'])
    if 5 in handType.values():
        hand['type'] = '5kind'
        hand['hand_strength'].append('7')
    elif 4 in handType.values():
        hand['type'] = '4kind'
        hand['hand_strength'].append('6')
    elif 3 in handType.values():
        if 2 in handType.values():
            hand['type'] = 'fullhouse'
            hand['hand_strength'].append('5')
        else:
            hand['type'] = '3kind'
            hand['hand_strength'].append('4')
    elif 2 in handType.values():
        num_pairs = sum(1 for count in handType.values() if count == 2)
        if num_pairs == 2:
            hand['type'] = '2pair'
            hand['hand_strength'].append('3')
        elif num_pairs == 1:
            hand['type'] = '1pair'
            hand['hand_strength'].append('2')
    else:
        hand['type'] = 'highcard'
        hand['hand_strength'].append('1')

def cardStrength(hand):
    for i in range(len(hand['hand'])):
        if 'A' in hand['hand'][i]:
            hand['hand_strength'].append('14')
        elif 'K' in hand['hand'][i]:
            hand['hand_strength'].append('13')
        elif 'Q' in hand['hand'][i]:
            hand['hand_strength'].append('12')
        elif 'J' in hand['hand'][i]:
            hand['hand_strength'].append('11')
        elif 'T' in hand['hand'][i]:
            hand['hand_strength'].append('10')
        elif '9' in hand['hand'][i]:
            hand['hand_strength'].append('09')
        elif '8' in hand['hand'][i]:
            hand['hand_strength'].append('08')
        elif '7' in hand['hand'][i]:
            hand['hand_strength'].append('07')
        elif '6' in hand['hand'][i]:
            hand['hand_strength'].append('06')
        elif '5' in hand['hand'][i]:
            hand['hand_strength'].append('05')
        elif '4' in hand['hand'][i]:
            hand['hand_strength'].append('04')
        elif '3' in hand['hand'][i]:
            hand['hand_strength'].append('03')
        elif '2' in hand['hand'][i]:
            hand['hand_strength'].append('02')

def rankPlays(plays):
    raw_rank = list()
    for i in range(len(plays)):
        raw_rank.append(plays[i]['raw_score'])
    raw_rank.sort(reverse=False)
    for i in range(len(raw_rank)):
        for j in range(len(plays)):
            if raw_rank[i] == plays[j]['raw_score']:
                if plays[j]['rank'] != 0: # i.e., not empty
                    continue
                else:
                    plays[j]['rank'] = i + 1

def scorePlays(plays):
    totalWinnings = int()
    for i in range(len(plays)):
        plays[i]['score'] = plays[i]['rank'] * plays[i]['bet']
        totalWinnings += plays[i]['score']
        print("Hand {} - Rank {} with Score {} that bet {}.".format(i, plays[i]['rank'], plays[i]['score'], plays[i]['bet']))
    print("Total winnings: {}".format(totalWinnings))
                
## ENGINE
plays = list()
setupPlays(input)
rankPlays(plays)
scorePlays(plays)