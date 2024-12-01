import time
from typing import Literal

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day0X.txt", "r") as file:
        data = file.readlines()

    return

def part_one(input_source: Literal["input", "examples"] = "input"):
    return

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
