from collections import deque
import time
from typing import Literal

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day09.txt", "r") as file:
        data = file.read().strip()
        data = list(map(int, list(data)))

    return data

def part_one(input_source: Literal["input", "examples"] = "input"):
    disk_map = common(input_source)

    decompressed = []
    for idx, n in enumerate(disk_map):
        if idx % 2 == 0:
            decompressed.extend([idx // 2] * n)
        else:
            decompressed.extend([-1] * n)

    queue = deque(decompressed)
    while queue:
        queue.pop()
        pop_idx = len(queue)
        slot_idx = decompressed.index(-1)

        decompressed[pop_idx], decompressed[slot_idx] = decompressed[slot_idx], decompressed[pop_idx]

    checksum = 0
    no_slots = list(filter(lambda x: x != -1, decompressed[1:]))
    for idx, n in enumerate(no_slots):
        checksum += idx * n

    return checksum

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
