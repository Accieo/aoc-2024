import re
import time
from typing import Literal, List, Tuple

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day03.txt", "r") as file:
        data = file.read().strip()

    return data

def parse_mul(data: str) -> List[Tuple[str, str]]:
    MUL_ONLY = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(MUL_ONLY, data)

def parse_all(data: str) -> List[Tuple[str, str, str]]:
    MUL_AND_CONDITIONALS = r"(mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))"
    return re.findall(MUL_AND_CONDITIONALS, data)

def part_one(input_source: Literal["input", "examples"] = "input") -> int:
    data = common(input_source)
    operations = parse_mul(data)

    products = []
    for l, r in operations:
        products.append(int(l) * int(r))

    return sum(products)

def part_two(input_source: Literal["input", "examples"] = "input"):
    data = common(input_source)
    operations = parse_all(data)

    products = []
    enabled = True
    for op, l, r in operations:
        if op == "don't()":
            enabled = False
        elif op == "do()":
            enabled = True
        elif op.startswith("mul("):
            if enabled:
                products.append(int(l) * int(r))

    return sum(products)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
