from sys import argv

with open(argv[1]) as f:
    lines = [l.strip() for l in f]

dimx, dimy = len(lines[0]), len(lines)
track = tuple("".join(lines))
start, end = track.index("S"), track.index("E")
dirs = [-dimx, 1, dimx, -1]

cost = {start: 0}
path = [start]
pos = start

while pos != end:
    for d in dirs:
        if track[pos + d] != "#" and pos + d not in cost:
            cost[pos + d] = cost[pos] + 1
            path.append(pos + d)
            pos = pos + d

print(f"Length of path: {len(path)}")

cheatcost = int(argv[2])
cheats = 0
for pos in path:
    for d in dirs:
        wall, space = (pos + d, pos + 2 * d)
        if space >= 0 and space < len(track) and \
                track[wall] == "#" and track[space] != "#" and \
                cost[space] >= cost[pos] + 2 + cheatcost:
            cheats += 1

print(f"part 1: {cheats} cheats")

cheats2 = 0
checknodes = [list() for _ in path]
checkvalid = [list() for _ in path]
valid = 0
for node in path[cheatcost:]:
    dist = abs(node % dimx - start % dimx) + abs(node // dimx - start // dimx)
    if dist - 20 > 0:  # too far, check again when we might be closer
        checknodes[dist - 20].append(node)
    elif (advantage := cost[node] - dist - cheatcost) >= 0:  # valid shortcut; keep observing
        checkvalid[min(20 - dist, advantage // 2) + 1].append(node)
        valid += 1

for pos in path[:-cheatcost]:
    for node in checkvalid[cost[pos]]:
        dist = abs(node % dimx - pos % dimx) + abs(node // dimx - pos // dimx)
        if dist - 20 > 0:  # too far, check again when we might be closer
            checknodes[cost[pos] + dist - 20].append(node)
            valid -= 1
        elif (advantage := cost[node] - cost[pos] - dist - cheatcost) >= 0:  # valid shortcut; keep observing
            checkvalid[cost[pos] + min(20 - dist, advantage // 2) + 1].append(node)
        else:  # no longer valid
            valid -= 1

    for node in checknodes[cost[pos]]:
        dist = abs(node % dimx - pos % dimx) + abs(node // dimx - pos // dimx)
        if dist - 20 > 0:  # too far, check again when we might be closer
            checknodes[cost[pos] + dist - 20].append(node)
        elif (advantage := cost[node] - cost[pos] - dist - cheatcost) >= 0:  # valid shortcut; keep observing
            checkvalid[cost[pos] + min(20 - dist, advantage // 2) + 1].append(node)
            valid += 1
    cheats2 += valid

print(f"part 2: {cheats2} cheats")
