import time
from typing import Literal
from collections import deque

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day09.txt", "r") as file:
        data = file.read().strip()
        data = list(map(int, list(data)))

        decompressed = []
        for idx, n in enumerate(data):
            if idx % 2 == 0:
                decompressed.extend([idx // 2] * n)
            else:
                decompressed.extend([-1] * n)

    return decompressed

def part_one(input_source: Literal["input", "examples"] = "input"):
    disk_map = common(input_source)

    free_space = deque([idx for idx, n in enumerate(disk_map) if n == -1])
    queue = deque(disk_map)
    while queue:
        v = queue.pop()

        if v == -1:
            continue

        pop_idx = len(queue)
        slot_idx = free_space.popleft()

        disk_map[pop_idx], disk_map[slot_idx] = disk_map[slot_idx], disk_map[pop_idx]

        # Consecutive free space windows can be max. 9, so we check if the next 10 are -1 to be sure
        # that we've hit the limit
        if all(val == -1 for val in disk_map[slot_idx + 1:slot_idx + 10]):
            break

    checksum = 0
    no_slots = list(filter(lambda x: x != -1, disk_map))
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
