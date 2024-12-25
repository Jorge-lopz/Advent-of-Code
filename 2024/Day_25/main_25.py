# --------------------------------------------------------------------------- #
#                                                                             #
#     main_25.py                               ::::             ::::::::      #
#                                            ++: :+:          :+:    :+:      #
#     PROJECT: Advent of Code              #:+   +:+         +:+              #
#                                        +#++:++#++:        +#+               #
#                                       +#+     +#+  ++::  +#+                #
#     AUTHOR: Jorge Lopez Puebla       ##+     #+#  #   # #+#    #+#          #
#     LAST UPDATE: 25/12/2024         ###     ###   ####  ########            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/25 🗝️

locks = []
keys = []

with open('input.txt') as f:
    memory = [line.strip() for line in f.readlines()]
    for schematic in range((len(memory) + 1) // 8):
        if "#" in memory[schematic * 8]:  # Lock
            lock = [0, 0, 0, 0, 0]
            for height in range(1, 7):
                for width in range(5):
                    if memory[schematic * 8 + height][width] == "#":
                        lock[width] += 1
            locks.append(lock)
        else:  # Key
            key = [0, 0, 0, 0, 0]
            for height in range(5, 0, -1):
                for width in range(5):
                    if memory[schematic * 8 + height][width] == "#":
                        key[width] += 1
            keys.append(key)

# FIRST PART: Get the number of unique lock/key pairs that don't overlap at all (sum of heights must be <=5)

result = set()

for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            result.add((tuple(lock), tuple(key)))

print("\n\033[37mThe number of unique lock/key pairs that don't overlap at all is:\033[0m\033[1m", len(result))
