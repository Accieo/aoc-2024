import time
from typing import Literal

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day22.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(int, data))

    return data

def next_snum(num: int) -> int:
    mod_coeff = 16_777_216
    num ^= (num * 64) % mod_coeff
    num ^= (num // 32) % mod_coeff
    num ^= (num * 2048) % mod_coeff

    return num

def simulate(num: int, steps: int) -> int:
    new_num = num
    for _ in range(steps):
        new_num = next_snum(new_num)

    return new_num

def part_one(input_source: Literal["input", "examples"] = "input"):
    numbers = common(input_source)

    results = []
    for n in numbers:
        results.append(simulate(n, 2000))

    return sum(results)

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
