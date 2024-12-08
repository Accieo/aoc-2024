import time
from itertools import combinations
from typing import Literal, List, Dict, Tuple

Antenna = str
Position = Tuple[int, int]
CityScan = List[List[str]]

def common(input_source: Literal["input", "examples"] = "input") -> CityScan:
    with open(f"{input_source}/day08.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(list, data))

    return data

def read_antennas(city_scan: CityScan) -> Dict[Antenna, List[Position]]:
    antennas = {}
    for y, row in enumerate(city_scan):
        for x, item in enumerate(row):
            if item == ".":
                continue
            if item in antennas.keys():
                antennas[item].append((y, x))
            else:
                antennas[item] = [(y, x)]

    return antennas

def is_within_bounds(y: int, x: int, city_scan: CityScan) -> bool:
    return 0 <= y < len(city_scan) and 0 <= x < len(city_scan[0])

def extend_line(y1: int, x1: int, dy: int, dx: int, city_scan: CityScan) -> set:
    anti_nodes = set()
    y, x = y1, x1
    while is_within_bounds(y=y, x=x, city_scan=city_scan):
        anti_nodes.add((y, x))
        y += dy
        x += dx
    return anti_nodes

def part_one(input_source: Literal["input", "examples"] = "input"):
    city_scan = common(input_source)
    antennas = read_antennas(city_scan)

    anti_nodes = set()
    for pos in antennas.values():
        for (y1, x1), (y2, x2) in combinations(pos, 2):
            dy, dx = y2 - y1, x2 - x1
            y3, x3 = y1 - dy, x1 - dx
            y4, x4 = y2 + dy, x2 + dx
            for y, x in [(y3, x3), (y4, x4)]:
                if is_within_bounds(y=y, x=x, city_scan=city_scan):
                    d1_squared = (y1 - y) ** 2 + (x1 - x) ** 2
                    d2_squared = (y2 - y) ** 2 + (x2 - x) ** 2
                    if d1_squared == 4 * d2_squared or d2_squared == 4 * d1_squared:
                        anti_nodes.add((y, x))

    return len(anti_nodes)

def part_two(input_source: Literal["input", "examples"] = "input"):
    city_scan = common(input_source)
    antennas = read_antennas(city_scan)

    anti_nodes = set()
    for pos in antennas.values():
        for (y1, x1), (y2, x2) in combinations(pos, 2):
            dy, dx = y2 - y1, x2 - x1
            anti_nodes = anti_nodes.union(extend_line(y1=y1, x1=x1, dy=dy, dx=dx, city_scan=city_scan))
            anti_nodes = anti_nodes.union(extend_line(y1=y2, x1=x2, dy=-dy, dx=-dx, city_scan=city_scan))

    return len(anti_nodes)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
