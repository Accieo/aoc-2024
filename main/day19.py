import time
from collections import deque
from typing import Literal, List

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day19.txt", "r") as file:
        data = file.read().strip().splitlines()
        patterns = list(map(str.strip, data[0].split(",")))
        onsen_designs = [d for d in data[2:]]

    return patterns, onsen_designs

def can_be_made(design: str, patterns: List[str]) -> bool:
    queue = deque([design])
    checked = set()

    while queue:
        c = queue.popleft()
        if c == "":
            return True

        if c in checked:
            continue
        checked.add(c)

        for p in patterns:
            if c.startswith(p):
                queue.append(c[len(p):])

    return False

def part_one(input_source: Literal["input", "examples"] = "input"):
    patterns, onsen_designs = common(input_source)

    c = 0
    for d in onsen_designs:
        if can_be_made(design=d, patterns=patterns):
            c += 1

    return c

def part_two(input_source: Literal["input", "examples"] = "input"):
    return

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
