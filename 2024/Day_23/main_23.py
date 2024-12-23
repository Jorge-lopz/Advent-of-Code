# --------------------------------------------------------------------------- #
#                                                                             #
#     main_23.py                               ::::             ::::::::      #
#                                            ++: :+:          :+:    :+:      #
#     PROJECT: Advent of Code              #:+   +:+         +:+              #
#                                        +#++:++#++:        +#+               #
#                                       +#+     +#+  ++::  +#+                #
#     AUTHOR: Jorge Lopez Puebla       ##+     #+#  #   # #+#    #+#          #
#     LAST UPDATE: 23/12/2024         ###     ###   ####  ########            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SRC: https://adventofcode.com/2024/day/23 🛜

# IMPORTS
from itertools import combinations  # -> Get combinations

with open('input.txt') as f:
    connections = [line.strip() for line in f.readlines()]

pcs = dict()

chief_pc = "t"
for connection in connections:
    connected = connection.split('-')
    pcs.setdefault(connected[0], set()).add(connected[1])
    pcs.setdefault(connected[1], set()).add(connected[0])

# FIRST PART: Find the number of 3-way interconnected pcs with the chief pc in it

def is_triangle(pcs, a, b, c):
    return b in pcs[a] and c in pcs[a] and c in pcs[b]

chief_3way_connections = set()
for chief in [pc for pc in pcs if pc.startswith(chief_pc)]:  # Filter only the chief pc connections
    for b, c in combinations(pcs[chief], 2):
        if is_triangle(pcs, chief, b, c):
            chief_3way_connections.add(tuple(sorted([chief, b, c])))  # To save them all sorted and check duplicated

print("\n\033[37mNumber of 3-way interconnected PCs with the chief PC:\033[0m\033[1m", len(chief_3way_connections))

# SECOND PART: Find the password to the LAN party (the biggest interconnected group)

def bron_kerbosch(graph, r, p, x):
    def get_highest_degree_node(nodes):
        return max(nodes, key=lambda node: len(graph[node]))

    # Base case: If P and X are both empty, R is a maximal clique
    if not p and not x:
        yield r
        return

    # Choose a pivot node to reduce the number of recursive calls
    pivot = get_highest_degree_node(p | x)

    # Iterate over nodes in P that are not neighbors of the pivot
    for v in p - graph[pivot]:
        neighbors = graph[v]
        # Recursive call to expand the clique
        yield from bron_kerbosch(graph, r | {v}, p & neighbors, x & neighbors)
        # Move the node v from P to X after processing
        p.remove(v)
        x.add(v)

max_clique = max(bron_kerbosch(pcs, set(), set(pcs.keys()), set()), key=len)

print("\n\033[0m\033[37mPassword to the LAN party is:\033[0m\033[1m", ",".join(sorted(max_clique)))
