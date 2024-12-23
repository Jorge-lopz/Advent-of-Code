# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 11/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/11

stones: [int]

with open('input.txt', 'r') as f:
    stones = list(map(int, f.read().split()))

def blink(times: int) -> [int]:
    counts = {}
    for stone in stones:
        counts[stone] = counts.get(stone, 0) + 1

    for _ in range(times):
        temp_counts = {}

        # Iterate over each stone and its count in the current counts dictionary
        for stone, count in counts.items():
            if stone == 0:
                new_stone = 1
                temp_counts[new_stone] = temp_counts.get(new_stone, 0) + count
            elif len(str(stone)) % 2 == 0:
                divisor = 10 ** (len(str(stone)) // 2)  # Divisor to split the stone into two parts
                # Add each part to new_counts with the same frequency as the original stone
                for new_stone in (stone // divisor, stone % divisor):
                    temp_counts[new_stone] = temp_counts.get(new_stone, 0) + count
            else:
                new_stone = stone * 2024
                temp_counts[new_stone] = temp_counts.get(new_stone, 0) + count
        # Update counts with the newly transformed counts for the next iteration
        counts = temp_counts

    return counts

# FIRST PART: Get the number of stones after 25 blinks (every blink causes a change in stones number and value)

print("\n\033[37mThe number of stones after 25 blinks is:\033[0m\033[1m", sum(blink(25).values()))

# SECOND PART: Get the number of stones after 75 blinks

print("\n\033[37mThe number of stones after 75 blinks is:\033[0m\033[1m", sum(blink(75).values()))
