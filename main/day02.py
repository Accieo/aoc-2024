import time
from typing import Literal, List

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day02.txt", "r") as file:
        data = file.read().splitlines()
        data = list(map(lambda x:  x.split(" "), data))
        reports = []
        for report in data:
            report = list(map(int, report))
            reports.append(report)

    return reports

def is_increasing(report: List[int]) -> bool:
    """Returns true if all elements of the array are in increasing order"""
    return all(report[n] > report[n - 1] for n in range(1, len(report)))

def is_decreasing(report: List[int]) -> bool:
    """Returns true if all elements of the array are in decreasing order"""
    return all(report[n] < report[n - 1] for n in range(1, len(report)))

def is_within_level(report: List[int]) -> bool:
    """Returns true if all adjacent elements of the array have a difference of at least 1 and max. 3"""
    return all(abs(report[n] - report[n - 1]) <= 3 for n in range(1, len(report)))

def part_one(input_source: Literal["input", "examples"] = "input") -> int:
    reports = common(input_source)

    safe = []
    for report in reports:
        if (is_increasing(report) or is_decreasing(report)) and is_within_level(report):
            safe.append(report)

    return len(safe)

def part_two(input_source: Literal["input", "examples"] = "input") -> int:
    reports = common(input_source)

    safe = [r for r in reports if (is_increasing(r) or is_decreasing(r)) and is_within_level(r)]

    possibly_safe = []
    for report in reports:
        if report in safe:
            continue

        # Brute force, worst case is O(n) and n is very small
        for n in range(0, len(report)):
            report_copy = report.copy()
            report_copy.pop(n)
            if (is_increasing(report_copy) or is_decreasing(report_copy)) and is_within_level(report_copy):
                possibly_safe.append(report)
                break

    total_safe = len(safe) + len(possibly_safe)
    return total_safe

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
