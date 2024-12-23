import time
from typing import Literal

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day23.txt", "r") as file:
        data = file.read().strip().splitlines()
        computers = {}
        for con in data:
            l, r = con.split("-")
            if l not in computers.keys():
                computers[l] = []
            if r not in computers.keys():
                computers[r] = []
            computers[l].append(r)
            computers[r].append(l)

    return computers

def startswithx(triplet: list, x: str) -> bool:
    for x in triplet:
        if x.startswith("t"):
            return True
    return False

def part_one(input_source: Literal["input", "examples"] = "input"):
    computers = common(input_source)
    triplets = set()

    for k, v in computers.items():
        for idx, c in enumerate(v):
            for z in v[idx + 1:]:
                if c in v and z in computers[c]:
                    t = [k, c, z]
                    if startswithx(t, "t"):
                        s = tuple(sorted([k, c, z]))
                        triplets.add(s)

    return len(triplets)

def part_two(input_source: Literal["input", "examples"] = "input"):
    computers = common(input_source)

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
