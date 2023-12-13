# Advent of Code
# Day 7 - Part 2
# Source: https://adventofcode.com/2023/day/7#part2

## SETUP
import pathlib
from collections import Counter

input = pathlib.Path('Learning') / '2023 AOC' / '2023-AOC-Day-7-Puzzle-input.txt'

with open(input, 'r') as file:
    input = [line.strip() for line in file]

def setupPlays(input):
    global plays
    for i, line in enumerate(input):
        cardData = {'id': i, 'rank': int(), 'hand': line.split()[0], 'type': str(), 'hand_strength': list(), 'bet': int(line.split()[1]), 'raw_score': int(), 'score': int()}
        plays.append(cardData)
    
    for hand in plays:
        handType(hand)
        cardStrength(hand)
        hand['raw_score'] = int(''.join(hand['hand_strength']))

def handType(hand):
    # REVISED
    # Changed dictionary name
    handTypeRaw = Counter(hand['hand'])
    
    # REVISED
    # Added call for new function
    if 'J' in handTypeRaw:
        handType = handModify(handTypeRaw, 'J')
    else:
        handType = handTypeRaw

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

# NEW FUNCTION
def handModify(handCount, card):
    if handCount[card] == 5:
        return handCount
    else:
        card_value = handCount.pop(card)
        max_value = max(handCount.items(), key=lambda x: x[1])[1]
        max_keys = [k for k, v in handCount.items() if v == max_value]
        if max_keys:
            handCount[max_keys[0]] += card_value
        else:
            handCount[next(iter(handCount))] += card_value
    return handCount

def cardStrength(hand):
    for card in hand['hand']:
        if 'A' == card:
            hand['hand_strength'].append('14')
        elif 'K' == card:
            hand['hand_strength'].append('13')
        elif 'Q' == card:
            hand['hand_strength'].append('12')
        # REVISED
        # J value modified from '11' to '01'
        elif 'J' == card:
            hand['hand_strength'].append('01')
        elif 'T' == card:
            hand['hand_strength'].append('10')
        elif '9' == card:
            hand['hand_strength'].append('09')
        elif '8' == card:
            hand['hand_strength'].append('08')
        elif '7' == card:
            hand['hand_strength'].append('07')
        elif '6' == card:
            hand['hand_strength'].append('06')
        elif '5' == card:
            hand['hand_strength'].append('05')
        elif '4' == card:
            hand['hand_strength'].append('04')
        elif '3' == card:
            hand['hand_strength'].append('03')
        elif '2' == card:
            hand['hand_strength'].append('02')

def rankPlays(plays):
    raw_rank = list()
    for hand in plays:
        raw_rank.append(hand['raw_score'])
    raw_rank.sort(reverse=False)
    for i, rank in enumerate(raw_rank):
        for hand in plays:
            if rank == hand['raw_score']:
                if hand['rank'] != 0: # i.e., not empty
                    continue
                else:
                    hand['rank'] = i + 1

def scorePlays(plays):
    totalWinnings = int()
    for i, hand in enumerate(plays):
        hand['score'] = hand['rank'] * hand['bet']
        totalWinnings += hand['score']
        print("Hand {} - Rank {} with Score {} that bet {}.".format(i, hand['rank'], hand['score'], hand['bet']))
    print("Total winnings: {}".format(totalWinnings))
                
## ENGINE
plays = list()
setupPlays(input)
rankPlays(plays)
scorePlays(plays)