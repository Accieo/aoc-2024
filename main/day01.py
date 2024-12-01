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
    print(part_one())
    print(part_two())
