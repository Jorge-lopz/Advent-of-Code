# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 01/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/1

left_col: [int] = []
right_col: [int] = []

# Read the input
def read_input():
    with open('input.txt', 'r') as f:
        for line in f.read().split('\n'):
            left_col.append(int(line.split('   ')[0]))
            right_col.append(int(line.split('   ')[1]))

    left_col.sort()
    right_col.sort()

# FIRST PART: Sum the differences between the smallest number on the left and right (removing already paired numbers)
read_input()
difference: int = 0
while left_col and right_col:
    difference += abs(left_col.pop(0) - right_col.pop(0))

print("\n\033[37mThe sum of the differences is:\033[0m\033[1m", difference)

# SECOND PART: Calculate the frequency of numbers in the right list manually
read_input()
right_freq: dict[int, int] = {}
for num in right_col:
    if num in right_freq:
        right_freq[num] += 1
    else:
        right_freq[num] = 1

similarity_score = 0
for num in left_col:
    similarity_score += num * right_freq.get(num, 0)

print("\n\033[0m\033[37mThe similarity score is:\033[0m\033[1m", similarity_score)
