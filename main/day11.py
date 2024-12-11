import time
from typing import Literal
from collections import Counter

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day11.txt", "r") as file:
        data = file.read().strip()
        data = data.split(" ")
        stones = [int(x) for x in data]

    return stones

def blink(stones: Counter) -> Counter:
    new_counts = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            strone = str(stone)
            l, r = strone[0: len(strone) // 2], strone[len(strone) // 2: len(strone)]
            new_counts[int(l)] += count
            new_counts[int(r)] += count
        else:
            new_counts[stone * 2024] += count

    return new_counts

def part_one(input_source: Literal["input", "examples"] = "input"):
    stones = common(input_source)
    stone_counts = Counter(stones)

    for _ in range(25):
        stone_counts = blink(stones=stone_counts)

    return sum(stone_counts.values())

def part_two(input_source: Literal["input", "examples"] = "input"):
    stones = common(input_source)
    stone_counts = Counter(stones)

    for _ in range(75):
        stone_counts = blink(stones=stone_counts)

    return sum(stone_counts.values())

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
