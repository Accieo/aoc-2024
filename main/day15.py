import time
from typing import Literal, NamedTuple, List, Tuple

Neighbors = Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]

class Symbols(NamedTuple):
    UP = "^"
    RIGHT = ">"
    LEFT = "<"
    DOWN = "v"
    BOX = "O"
    WALL = "#"
    FREE = "."
    ROBOT = "@"

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day15.txt", "r") as file:
        data = file.read().strip().splitlines()
        warehouse = []
        moves = []
        for line in data:
            if "#" in line:
                warehouse.append(list(line))
            elif line == "":
                continue
            else:
                moves.extend(list(line))

    return warehouse, moves

def attempt_move(y: int, x: int, max_y: int, max_x: int, move: str, warehouse: List[List[str]]):
    delta = {
        Symbols.UP: (-1, 0),
        Symbols.DOWN: (1, 0),
        Symbols.LEFT: (0, -1),
        Symbols.RIGHT: (0, 1),
    }
    dy, dx = delta[move]
    new_y, new_x = y + dy, x + dx

    if not (0 <= new_y < max_y and 0 <= new_x < max_x):
        return y, x

    boxes_to_push = []
    current_y, current_x = new_y, new_x

    while 0 <= current_y < max_y and 0 <= current_x < max_x:
        target = warehouse[current_y][current_x]

        if target == Symbols.FREE:
            break
        elif target == Symbols.BOX:
            boxes_to_push.append((current_y, current_x))
        else:
            return y, x

        current_y += dy
        current_x += dx

    if len(boxes_to_push) > 0:
        final_y, final_x = current_y, current_x
        if not (0 <= final_y < max_y and 0 <= final_x < max_x and warehouse[final_y][final_x] == Symbols.FREE):
            return y, x

        for by, bx in reversed(boxes_to_push):
            warehouse[by + dy][bx + dx] = Symbols.BOX
            warehouse[by][bx] = Symbols.FREE

        warehouse[y][x] = Symbols.FREE
        warehouse[new_y][new_x] = Symbols.ROBOT
        return new_y, new_x

    if warehouse[new_y][new_x] == Symbols.FREE:
        warehouse[y][x] = Symbols.FREE
        warehouse[new_y][new_x] = Symbols.ROBOT
        return new_y, new_x

    return y, x

def get_robot_position(warehouse: List[List[str]]) -> Tuple[int, int]:
    y, x = 0, 0
    for ldx, line in enumerate(warehouse):
        if Symbols.ROBOT in line:
            y = ldx
            x = line.index(Symbols.ROBOT)

    return (y, x)

def get_boxes_coords(warehouse: List[List[str]]) -> List[int]:
    gps_coords = []
    for ldx, line in enumerate(warehouse):
        for odx, obj in enumerate(line):
            if obj == Symbols.BOX:
                gps_coords.append(100 * ldx + odx)

    return gps_coords

def widen_warehouse(warehouse: List[List[str]]) -> List[List[str]]:
    wide_warehouse = []
    for line in warehouse:
        wide_line = []
        for obj in line:
            if obj == Symbols.WALL:
                wide_line.extend(["#", "#"])
            elif obj == Symbols.BOX:
                wide_line.extend(["[", "]"])
            elif obj == Symbols.FREE:
                wide_line.extend([".", "."])
            elif obj == Symbols.ROBOT:
                wide_line.extend(["@", "."])
        wide_warehouse.append(wide_line)

    return wide_warehouse

def part_one(input_source: Literal["input", "examples"] = "input"):
    warehouse, moves = common(input_source)

    max_y, max_x = len(warehouse), len(warehouse[0])
    y, x = get_robot_position(warehouse)

    for move in moves:
        y, x = attempt_move(y, x, max_y, max_x, move, warehouse)

    gps_coords = get_boxes_coords(warehouse)

    return sum(gps_coords)

def part_two(input_source: Literal["input", "examples"] = "input"):
    warehouse, moves = common(input_source)
    warehouse = widen_warehouse(warehouse)

    max_y, max_x = len(warehouse), len(warehouse[0])
    y, x = get_robot_position(warehouse)

    # TODO

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
