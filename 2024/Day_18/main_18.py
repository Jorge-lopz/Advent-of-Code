from collections import deque
from typing import TypeAlias

Position: TypeAlias = tuple[int, int]

def solve(rows: int, cols: int, obstructions: list[Position]):
    end_row, end_col = rows - 1, cols - 1

    queue = deque([(0, 0, 0)])  # row, col, distance
    seen = {(0, 0)} | set(obstructions)

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == (end_row, end_col):
            return dist

        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in seen:
                seen.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))

    return -1

def part_1() -> int:
    obstructions: list[Position] = [
        Position(map(int, x.split(",")[::-1]))  # row, col
        for x in open("input.txt").read().splitlines()
    ]

    return solve(71, 71, obstructions[:1024])

def part_2() -> str:
    obstructions: list[Position] = [
        Position(map(int, x.split(",")[::-1]))  # row, col
        for x in open("input.txt").read().splitlines()
    ]

    start_at = 1024

    initial = obstructions[:start_at]
    remaining = obstructions[start_at:]

    left, right = 0, len(obstructions) - 1
    last_working = start_at

    while left <= right:
        mid = (left + right) // 2
        current_obstructions = initial + remaining[: mid + 1]

        r = solve(71, 71, current_obstructions)

        if r != -1:
            left = mid + 1
            last_working = mid + start_at  # +start_at to get the correct index
        else:
            right = mid - 1

    row, col = obstructions[last_working + 1]
    return f"{col},{row}"

print(part_1())
print(part_2())
