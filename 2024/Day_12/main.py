# --------------------------------------------------------------------------- #
#                                                                             #
#     main.py                                        ::::      ::::::::       #
#                                                  ++: :+:   :+:    :+:       #
#     PROJECT: Advent of Code                    #:+   +:+  +:+               #
#                                              +#++:++#++: +#+                #
#                                             +#+     +#+ +#+                 #
#     AUTHOR: Jorge Lopez Puebla             ##+     #+# #+#    #+#           #
#     LAST UPDATE: 12/12/2024               ###     ###  ########             #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/12

memory: [[str]]

with open('input.txt', 'r') as file:
    memory = [list(line.strip()) for line in file.readlines()]

def get_region(visited, neighbors, pos):
    if pos not in visited:
        visited.add(pos)
        for neighbor in neighbors[pos]:
            get_region(visited, neighbors, neighbor)
    return visited

def count_common_sides(region):
    ct = 0
    for x, y in region:
        if (x - 1, y) in region:
            for y2 in [y - 1, y + 1]:
                if (x, y2) not in region and (x - 1, y2) not in region:
                    ct += 1
        if (x, y - 1) in region:
            for x2 in [x - 1, x + 1]:
                if (x2, y) not in region and (x2, y - 1) not in region:
                    ct += 1
    return ct

neighbors = {}

for y, line in enumerate(memory):
    for x, char in enumerate(line):
        matching_neighbors = set()
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if not (0 <= x2 < len(memory[0]) and 0 <= y2 < len(memory)):
                continue
            if memory[y2][x2] == memory[y][x]:
                matching_neighbors.add((x2, y2))
        neighbors[(x, y)] = matching_neighbors

result_1, result_2 = [], []
regions = []
seen = set()
for pos, cur_neighbors in neighbors.items():
    if pos in seen:
        continue
    region = get_region(set(), neighbors, pos)
    area = len(region)
    perimeter = sum([4 - len(neighbors[(x, y)]) for x, y in region])
    # FIRST PART: Find the total cost (area * perimeter) of the regions formed by adjacent characters
    result_1.append([area, perimeter])
    # SECOND PART: Find the total cost (area * nmb of sides) of the regions formed by adjacent characters
    result_2.append([area, (perimeter - count_common_sides(region))])
    seen.update(region)
    regions.append(region)

print("\n\033[37mThe total regions cost (area * perimeter) is:\033[0m\033[1m",
      sum(area * perimeter for area, perimeter in result_1))

print("\n\033[37mThe total regions cost (area * sides) is:\033[0m\033[1m",
      sum(area * sides for area, sides in result_2))
