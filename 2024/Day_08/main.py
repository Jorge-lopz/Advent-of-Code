# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 08/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2022/day/8

memory: [[str]] = []
antennas: {str: [[int, int]]} = {}

# Read input file
with open('input.txt', 'r') as file:
    for row, line in enumerate(file.readlines()):
        line_chars = []
        for col, char in enumerate(line.strip()):
            line_chars.append(char)
            if char.isdigit() or char.isupper() or char.islower():
                antennas.setdefault(char, []).append([row, col])
        memory.append(line_chars)

antennas = {key: value for key, value in antennas.items() if len(value) > 1}  # Filter out single antennas

# FIRST PART: Count the number of antinodes
antinodes: ([int, int]) = set()

for freq, positions in antennas.items():
    for antenna in positions:
        for other_antenna in positions:
            if antenna == other_antenna:
                continue
            dx, dy = other_antenna[0] - antenna[0], other_antenna[1] - antenna[1]  # To check both sides
            for antinode in [[antenna[0] - dx, antenna[1] - dy], [other_antenna[0] + dx, other_antenna[1] + dy]]:
                if 0 <= antinode[0] < len(memory) and 0 <= antinode[1] < len(memory[0]):
                    antinodes.add(tuple(antinode))
                    # print(f"Antinode: {antinode} <- {antenna} {other_antenna}")

print("\n\033[37mThe number of unique antinodes is:\033[0m\033[1m", len(antinodes))

# SECOND PART: Countinf the number of antinodes while accounting for harmonics (repeating, without distance limits)
harmonics_antinodes: ([int, int]) = set()

for freq, positions in antennas.items():
    for antenna in positions:
        for other_antenna in positions:
            if antenna == other_antenna:
                continue
            vx, vy = other_antenna[0] - antenna[0], other_antenna[1] - antenna[1]
            x, y = antenna[0], antenna[1]
            while 0 <= x + vx < len(memory) and 0 <= y + vy < len(memory[0]):
                x, y = x + vx, y + vy
                harmonics_antinodes.add((x, y))
                # print(f"Antinode: [{x}, {y}] <- {antenna} {other_antenna}")

print("\n\033[0m\033[37mThe number of (infinitely repeating) antinodes is:\033[0m\033[1m", len(harmonics_antinodes))
