import time
from copy import deepcopy
from typing import Literal, List, Tuple
from concurrent.futures import ProcessPoolExecutor

Direction = str
Map = List[List[str]]
Position = Tuple[int, int]
WalkedPath = List[List[int]]

UP, DOWN, LEFT, RIGHT = "^", "v", "<", ">"
OBSTACLE = "#"
NOTHING = "."
WALKED = "X"

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day06.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(list, data))

    return data

def move_guard(lab_map: Map, start_y: int, start_x: int, current_direction: Direction) -> Tuple[WalkedPath, Map]:
    """
    Moves the guard within the lab map.

    Coordinates are represented as (y, x).

        y
        ^
        |
        ⋅--> x

    """
    walked_path = [[start_y, start_x]]
    if current_direction == UP:
        path = "".join([lab_map[y][start_x] for y in range(start_y - 1, -1, -1)])
        obstacle_idx = path.find(OBSTACLE)
        for walked_y in range(start_y - 1, start_y - obstacle_idx - 1, -1):
            walked_path.append([walked_y, start_x])
    elif current_direction == DOWN:
        path = "".join([lab_map[y][start_x] for y in range(start_y + 1, len(lab_map))])
        obstacle_idx = path.find(OBSTACLE)
        for walked_y in range(start_y + 1, start_y + obstacle_idx + 1):
            walked_path.append([walked_y, start_x])
    elif current_direction == LEFT:
        path = "".join([lab_map[start_y][x] for x in range(start_x - 1, -1, -1)])
        obstacle_idx = path.find(OBSTACLE)
        for walked_x in range(start_x - 1, start_x - obstacle_idx - 1, -1):
            walked_path.append([start_y, walked_x])
    elif current_direction == RIGHT:
        path = "".join([lab_map[start_y][x] for x in range(start_x + 1, len(lab_map[0]))])
        obstacle_idx = path.find(OBSTACLE)
        for walked_x in range(start_x + 1, start_x + obstacle_idx + 1):
            walked_path.append([start_y, walked_x])

    end_y, end_x = walked_path[-1]
    lab_map[start_y][start_x] = NOTHING
    lab_map[end_y][end_x] = current_direction

    return walked_path, lab_map

def get_pos_and_dir(lab_map: Map) -> Tuple[Position, Direction]:
    """
    Gets the current guard's position and facing direction
    """
    direction = ""
    coords = (0, 0) 
    for y, line in enumerate(lab_map):
        for dir in [UP, DOWN, LEFT, RIGHT]:
            if dir in line:
                x = line.index(dir)
                return (y, x), dir

    return coords, direction

def is_facing_obstacle(lab_map: Map, y: int, x: int, current_direction: Direction) -> Tuple[str, bool]:
    """
    Checks if there is an obstacle in front of the guard
    When true, the guard's direction is rotated and returns true
    When false, the guard's position stays as is and returns false
    """
    direction_offsets = {
        UP: (-1, 0, ">"),
        DOWN: (1, 0, "<"),
        LEFT: (0, -1, "^"),
        RIGHT: (0, 1, "v")
    }

    dy, dx, rotate_dir = direction_offsets[current_direction]
    neighbor_y, neighbor_x = y + dy, x + dx

    if (0 <= neighbor_y < len(lab_map) and 0 <= neighbor_x < len(lab_map[0])):
        if lab_map[neighbor_y][neighbor_x] == OBSTACLE:
            return rotate_dir, True

    return current_direction, False

def walk_towards_void(lab_map: Map, y: int, x: int, current_direction: Direction) -> WalkedPath:
    """Get walked path towards void"""
    walked_to_void = []

    while 0 <= y < len(lab_map) and 0 <= x < len(lab_map[0]):
        walked_to_void.append([y, x])
        if current_direction == UP:
            y -= 1
        elif current_direction == DOWN:
            y += 1
        elif current_direction == LEFT:
            x -= 1
        elif current_direction == RIGHT:
            x += 1
        if not (0 <= y < len(lab_map) and 0 <= x < len(lab_map[0])):
            break

    return walked_to_void

def brute_force_obstacle(start: int, end: int, lab_map: Map, thread_id: int) -> int:
    """
    Brute forces by placing obstacles from `i` up to `j`
    returns `count` of times guard was stuck in an infinite loop
    """
    infinite = 0
    max_iters = 10_000
    for i in range(start, end):
        for j in range(len(lab_map)):
            wrk_map = deepcopy(lab_map)
            if wrk_map[i][j] not in [UP, DOWN, LEFT, RIGHT]:
                wrk_map[i][j] = OBSTACLE

            (y, x), current_direction = get_pos_and_dir(wrk_map)

            crr_iters = 0
            found_void = True
            while found_void:
                crr_iters += 1

                if crr_iters == max_iters:
                    infinite += 1
                    break

                _, wrk_map = move_guard(wrk_map, y, x, current_direction)
                (y, x), current_direction = get_pos_and_dir(wrk_map)
                current_direction, found_void = is_facing_obstacle(wrk_map, y, x, current_direction)
    return infinite

def part_one(input_source: Literal["input", "examples"] = "input") -> int:
    lab_map = common(input_source)

    (y, x), current_direction = get_pos_and_dir(lab_map=lab_map)

    walked_paths = []
    while True:
        walked, lab_map = move_guard(lab_map, y, x, current_direction)
        walked_paths.extend(walked)
        (y, x), current_direction = get_pos_and_dir(lab_map)
        current_direction, found_obstacle = is_facing_obstacle(lab_map, y, x, current_direction)
        
        if not found_obstacle:
            break

    walked_paths.extend(walk_towards_void(lab_map, y, x, current_direction))

    for y, x in walked_paths:
        lab_map[y][x] = WALKED

    count_walked = sum(row.count(WALKED) for row in lab_map)

    return count_walked

def part_two(input_source: Literal["input", "examples"] = "input") -> int:
    lab_map = common(input_source)

    inputs = []
    thread_id = 0
    max_workers = 8
    chunk_size = len(lab_map) // max_workers
    for s in range(0, len(lab_map), chunk_size):
        inputs.append((s, min(s + chunk_size, len(lab_map)), lab_map, thread_id))
        thread_id += 1

    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(brute_force_obstacle, *args) for args in inputs]
        results = [future.result() for future in futures]

    return sum(results)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
