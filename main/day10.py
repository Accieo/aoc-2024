import time
from collections import deque
from typing import Literal, List, Tuple

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day10.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(list, data))
        topographic_map = [list(map(int, n)) for n in data]

    return topographic_map

def get_neighbors(y: int, x: int, max_length: int) -> List[Tuple[int, int]]:
    # diffs = [down, up, left, right]
    diffs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    neighbors = list(map(lambda diff: (y + diff[0], x + diff[1]), diffs))
    neighbors = list(filter(lambda coord: (0 <= coord[0] < max_length) and (0 <= coord[1] < max_length), neighbors))

    return neighbors

def get_origins(topographic_map: List[List[int]]) -> List[Tuple[int, int]]:
    MAX_LENGTH = len(topographic_map)

    starting_points = []
    for y in range(0, MAX_LENGTH):
        for x in range(0, MAX_LENGTH):
            if topographic_map[y][x] == 0:
                starting_points.append((y, x))

    return starting_points

def part_one(input_source: Literal["input", "examples"] = "input"):
    topographic_map = common(input_source)

    MAX_LENGTH = len(topographic_map)

    starting_points = get_origins(topographic_map)

    scores = {}
    for ogy, ogx in starting_points:
        queue = deque([(ogy, ogx)])
        visited = set([(ogy, ogx)])
        nines = 0

        while queue:
            wky, wkx = queue.popleft()
            neighbors = get_neighbors(y=wky, x=wkx, max_length=MAX_LENGTH)
            for y, x in neighbors:
                current_value = topographic_map[y][x]
                if (y, x) not in visited and current_value - topographic_map[wky][wkx] == 1:
                    visited.add((y, x))
                    queue.append((y, x))

                    if current_value == 9:
                        nines += 1

        scores[(ogy, ogx)] = nines

    return sum(scores.values())

def part_two(input_source: Literal["input", "examples"] = "input"):
    topographic_map = common(input_source)

    MAX_LENGTH = len(topographic_map)

    starting_points = get_origins(topographic_map)

    ratings = {}
    for ogy, ogx in starting_points:
        queue = deque([(ogy, ogx, [])])
        visited = set([(ogy, ogx)])
        distinct = 0

        while queue:
            wky, wkx, path = queue.popleft()
            neighbors = get_neighbors(y=wky, x=wkx, max_length=MAX_LENGTH)
            for y, x in neighbors:
                current_value = topographic_map[y][x]
                if (y, x) not in path and current_value - topographic_map[wky][wkx] == 1:
                    visited.add((y, x))
                    queue.append((y, x, path + [(y, x)]))

                    if current_value == 9:
                        distinct += 1

        ratings[(ogy, ogx)] = distinct

    return sum(ratings.values())

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
