import time
from typing import Literal, List

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day07.txt", "r") as file:
        data = file.read().strip().splitlines()
        results = []
        members = []
        for line in data:
            result, numset = line.split(": ")
            results.append(int(result))
            members.append([int(num) for num in numset.split(" ")])

    return results, members

def calibrate(results: List[int], members: List[List[int]]) -> List[int]:
    """Tests whether the operators `(+)` and `(*)` can yield the `result` (key) for a `set of numbers` (values)"""
    possible = []
    
    for target, numset in zip(results, members):
        cumulative = [numset[0]]

        for num in numset[1:]:
            next_cumulative = []
            for res in cumulative:
                next_cumulative.append(res + num)
                next_cumulative.append(res * num)

            cumulative = next_cumulative

        if target in cumulative:
            possible.append(target)

    return possible

def part_one(input_source: Literal["input", "examples"] = "input"):
    results, members = common(input_source)

    results = calibrate(results, members)

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
