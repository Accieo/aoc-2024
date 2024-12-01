import time
from collections import Counter
from typing import List, Literal, Tuple

def common(input_source: Literal["input", "examples"] = "input") -> Tuple[List[int], List[int]]:
    with open(f"{input_source}/day01.txt", "r") as file:
        data = file.readlines()
        left_locations = []
        right_locations = []
        for line in data:
            left, right = line.strip().split("   ")
            left_locations.append(int(left))
            right_locations.append(int(right))

        left_locations.sort()
        right_locations.sort()

    return left_locations, right_locations

def part_one(input_source: Literal["input", "examples"] = "input") -> int:
    left_locations, right_locations = common(input_source)

    pair_distances = []
    for l, r in zip(left_locations, right_locations):
        pair_distances.append(abs(l - r))

    return sum(pair_distances)

def part_two(input_source: Literal["input", "examples"] = "input") -> int:
    left_locations, right_locations = common(input_source)
    locations_count = Counter(right_locations)

    similarity_scores = []
    for l in left_locations:
        if l in locations_count.keys():
            similarity_scores.append(l * locations_count[l])

    return sum(similarity_scores)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
