import time
from collections import deque
from typing import Literal, List, Tuple

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day12.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(list, data))

    return data

def get_neighbors(y: int, x: int, max_length: int = 0) -> List[Tuple[int, int]]:
    # diffs = [down, up, left, right]
    diffs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    neighbors = list(map(lambda diff: (y + diff[0], x + diff[1]), diffs))
    if max_length:
        neighbors = list(filter(lambda coord: (0 <= coord[0] < max_length) and (0 <= coord[1] < max_length), neighbors))

    return neighbors

def find_clusters(garden: List[List[str]]):
    MAX_LENGTH = len(garden)
    visited = set()
    clusters = []

    for y in range(MAX_LENGTH):
        for x in range(MAX_LENGTH):
            if (y, x) not in visited:
                plant = garden[y][x]
                queue = deque([(y, x)])
                cluster = []
                while queue:
                    cy, cx = queue.popleft()
                    if (cy, cx) in visited:
                        continue
                    visited.add((cy, cx))

                    if garden[y][x] == plant:
                        cluster.append((cy, cx))
                        neighbors = get_neighbors(y=cy, x=cx, max_length=MAX_LENGTH)
                        for ny, nx in neighbors:
                            if (ny, nx) not in visited and garden[ny][nx] == plant:
                                queue.append((ny, nx))

                clusters.append((plant, cluster))

    return clusters

def calculate_perimeter(cluster: List[Tuple[int, int]]) -> int:
    perimeter = 0
    for y, x in cluster:
        for neighbor in get_neighbors(y=y, x=x):
            if neighbor not in cluster:
                perimeter += 1

    return perimeter

def part_one(input_source: Literal["input", "examples"] = "input"):
    garden = common(input_source)

    clusters = find_clusters(garden)

    total = 0
    for _, cluster in clusters:
        area = len(cluster)
        perimeter = calculate_perimeter(cluster)
        total += area * perimeter
    
    return total

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
