from functools import cache

with open('input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

patterns = set(lines[0].split(', '))
designs = lines[2:]
pattern_max_len = max(map(len, patterns))

@cache
def get_subdesigns(design):
    if not can_start_design(design):
        return 0
    count = 0
    for pattern_len in reversed(range(1, min(len(design) + 1, pattern_max_len + 1))):
        sub_design = design[:pattern_len]
        if sub_design in patterns:
            if pattern_len == len(design):
                count += 1
            else:
                count += get_subdesigns(design[pattern_len:])
    return count

@cache
def can_start_design(design):
    can_start = False
    for i in range(1, min(len(design) + 1, pattern_max_len + 1)):
        if design[:i] in patterns:
            can_start = True
            break
    if not can_start:
        return False
    can_start = False
    for i in range(1, min(len(design) + 1, pattern_max_len + 1)):
        if design[-i:] in patterns:
            can_start = True
            break
    return can_start

distinct_count = 0
count = 0

for design in designs:
    subdesigns = get_subdesigns(design)
    count += subdesigns
    if subdesigns > 0:
        distinct_count += 1

print('Part 1 Answer:', distinct_count)
print('Part 2 Answer:', count)
