import time
from typing import Literal, Tuple
from dataclasses import dataclass

Vec2 = Tuple[int, int]

@dataclass
class ClawMachine:
    A: Vec2 = (0, 0)
    B: Vec2 = (0, 0)
    Prize: Vec2 = (0, 0)

def get_coords(line: str, key: str, operator: str) -> Tuple[int, int]:
    _, coords = line.split(key)
    x, y = coords.split(", ")
    x_val, y_val = int(x.split(operator)[1]), int(y.split(operator)[1])
    return (x_val, y_val)

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day13.txt", "r") as file:
        data = file.read().strip().splitlines()
        data.append("")

        claw_machines = []
        claw_machine = ClawMachine()
        for line in data:
            if "A:" in line:
                claw_machine.A = get_coords(line, "A: ", "+")
            elif "B:" in line:
                claw_machine.B = get_coords(line, "B: ", "+")
            elif "Prize:" in line:
                claw_machine.Prize = get_coords(line, "Prize: ", "=")
            else:
                claw_machines.append(claw_machine)
                claw_machine = ClawMachine()

    return claw_machines

def determinant(v0: Vec2, v1: Vec2) -> int:
    ax, ay = v0
    bx, by = v1
    return ax * by - bx * ay

def part_one(input_source: Literal["input", "examples"] = "input"):
    claw_machines = common(input_source)

    total = 0
    for cm in claw_machines:
        det = determinant(v0=cm.A, v1=cm.B)
        dx = determinant(v0=cm.Prize, v1=cm.B)
        dy = determinant(v0=cm.A, v1=cm.Prize)
        x = dx/det
        y = dy/det
        if x.is_integer() and y.is_integer():
            total += x * 3
            total += y

    return int(total)

def part_two(input_source: Literal["input", "examples"] = "input"):
    claw_machines = common(input_source)

    OFFSET = 10_000_000_000_000

    total = 0
    for cm in claw_machines:
        px, py = cm.Prize
        px += OFFSET
        py += OFFSET

        det = determinant(v0=cm.A, v1=cm.B)
        dx = determinant(v0=(px, py), v1=cm.B)
        dy = determinant(v0=cm.A, v1=(px, py))
        x = dx/det
        y = dy/det
        if x.is_integer() and y.is_integer():
            total += x * 3
            total += y

    return int(total)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
