import time
from typing import Literal, List

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day11.txt", "r") as file:
        data = file.read().strip()
        data = data.split(" ")
        stones = [int(x) for x in data]

    return stones

def blink(stones: List[int]) -> List[int]:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            strone = str(stone)
            l, r = strone[0: len(strone) // 2], strone[len(strone) // 2: len(strone)]
            new_stones.extend([int(l), int(r)])
        else:
            new_stones.append(stone * 2024)

    return new_stones

def part_one(input_source: Literal["input", "examples"] = "input"):
    stones = common(input_source)

    for _ in range(25):
        stones = blink(stones=stones)

    return len(stones)

def part_two(input_source: Literal["input", "examples"] = "input"):
    stones = common(input_source)

    # for _ in range(75):
    #     stones = blink(stones=stones)

    return len(stones)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
