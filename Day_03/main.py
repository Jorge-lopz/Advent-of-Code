# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 03/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/3

# IMPORTS
import re  # -> Regular expressions

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_dont_pattern = r"(do\(\)|don't\(\))"

# Read the input
with open('input.txt', 'r') as file:
    memory = file.read()

# FIRST PART: Sum the results of all valid 'mul(X,Y)' instructions
result = sum(int(x) * int(y) for x, y in re.findall(mul_pattern, memory))

print("\n\033[37mThe sum of valid mul results is:\033[0m\033[1m", result)

# SECOND PART: Consider valid 'do()' and 'don't()' instructions toggle future mul instructions
enabled = True
result = 0

for token in re.split(f"({mul_pattern}|{do_dont_pattern})", memory):
    if not token:
        continue

    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False

    match = re.match(mul_pattern, token)
    if enabled and match:
        x, y = map(int, match.groups())
        result += x * y

print("\n\033[0m\033[37mThe sum of valid mul results (with do/don't toggling) is:\033[0m\033[1m", result)
