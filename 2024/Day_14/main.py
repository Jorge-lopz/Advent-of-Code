# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 14/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/14

# IMPORTS
import re  # -> Regular expressions
from copy import deepcopy  # -> Deep copy a list

size = (101, 103)
robots: [[[int], list[int]]] = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.split(" ")
        position = [int(re.sub(r"[^0-9-]", "", part)) for part in line[0].split(",")]
        speed = [int(re.sub(r"[^0-9-]", "", part)) for part in line[1].split(",")]
        robots.append([position, tuple(speed)])

robots_2 = deepcopy(robots)

def move_robots(robots: []):
    for robot in robots:
        robot[0][0] += robot[1][0]
        robot[0][1] += robot[1][1]
        if robot[0][0] < 0:
            robot[0][0] += size[0]
        elif robot[0][0] >= size[0]:
            robot[0][0] -= size[0]
        if robot[0][1] < 0:
            robot[0][1] += size[1]
        elif robot[0][1] >= size[1]:
            robot[0][1] -= size[1]

# FIRST PART: Get the quadrant with the least robots after 100 seconds
for _ in range(100):
    move_robots(robots)

quadrants = [0] * 4  # Top-left, Top-right, Bottom-left, Bottom-right
for robot in robots:
    if robot[0][0] == size[0] // 2 or robot[0][1] == size[1] // 2:
        continue
    quadrants[(robot[0][0] > size[0] // 2) + (robot[0][1] > size[1] // 2) * 2] += 1

safety_factor = 1
for quadrant in quadrants:
    safety_factor *= quadrant

print("\n\033[37mThe safety factor after 100 seconds is:\033[0m\033[1m", safety_factor)

# SECOND PART: Get the minimum number of seconds for most of the robots to form a Christmas tree
def treeness() -> int:
    # Calculate tree-like structure based on robot proximity
    points = {complex(robot[0][0], robot[0][1]) for robot in robots_2}
    return sum(len({
                       p + 1,
                       p - 1,
                       p + 1j,
                       p - 1j,
                       p + 1 + 1j,
                       p + 1 - 1j,
                       p - 1 + 1j,
                       p - 1 - 1j,
                   } & points) for p in points)  # & -> Intersection between the neighbors position and the robots'

max_score = 0
seconds = 0
for second in range(1, size[0] * size[1]):
    move_robots(robots_2)
    score = treeness()
    if score > max_score:
        max_score = score
        seconds = second

    # Stop early if the score stabilizes
    if max_score > 500:  # Arbitrary limit
        break

print("\n\033[0m\033[37mThe min number of seconds for the robots to form a Christmas tree is:\033[0m\033[1m", seconds)
