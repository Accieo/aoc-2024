import time
from math import prod
from typing import Literal, List, Tuple

Vec2 = Tuple[int, int]

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day14.txt", "r") as file:
        data = file.read().strip().splitlines()
        positions = []
        speeds = []
        for line in data:
            p, v = line.split(" ")
            px, py = p.split("=")[1].split(",")
            vx, vy = v.split("=")[1].split(",")
            positions.append((int(px), int(py)))
            speeds.append((int(vx), int(vy)))

    return positions, speeds

def simulate_movement(positions: List[Vec2], speeds: List[Vec2], seconds: int, max_lengths: Vec2) -> List[Vec2]:
    new_positions = []
    max_x, max_y = max_lengths
    for (px, py), (vx, vy) in zip(positions, speeds):
        px += vx * seconds
        py += vy * seconds
        px = px % max_x
        py = py % max_y
        new_positions.append((px, py))

    return new_positions

def filter_middle(positions: List[Vec2], max_lengths: Vec2) -> List[Vec2]:
    filtered = []
    max_x, max_y = max_lengths
    for x, y in positions:
        if x != max_x // 2 and y != max_y // 2:
            filtered.append((x, y))

    return filtered

def count_quadrants(positions: List[Vec2], max_lengths: Vec2) -> List[int]:
    max_x, max_y = max_lengths
    mid_x, mid_y = max_x // 2, max_y // 2
    
    diffs = [
        (lambda x, y: 0 <= x < mid_x and 0 <= y < mid_y),        # Q0
        (lambda x, y: mid_x <= x < max_x and 0 <= y < mid_y),    # Q1
        (lambda x, y: 0 <= x < mid_x and mid_y <= y < max_y),    # Q2
        (lambda x, y: mid_x <= x < max_x and mid_y <= y < max_y) # Q3
    ]
    
    counts = [0, 0, 0, 0]

    for x, y in positions:
        for i, quad in enumerate(diffs):
            if quad(x, y):
                counts[i] += 1
                break

    return counts

def part_one(input_source: Literal["input", "examples"] = "input"):
    positions, speeds = common(input_source)

    max_lengths = (101, 103)

    new_positions = simulate_movement(positions, speeds, 100, max_lengths)
    new_positions = filter_middle(new_positions, max_lengths)
    counts = count_quadrants(new_positions, max_lengths)

    return prod(counts)

def part_two(input_source: Literal["input", "examples"] = "input"):
    positions, speeds = common(input_source)

    max_lengths = (101, 103)

    # For this part I just dumped the row string into a .txt file
    # with the name of the seconds, looped from (0, 10_000)
    # then, using the MacOS finder, saw the christmas tree on the file icon
    # If it's stupid but it works, it ain't stupid (￣^￣ )ゞ

    # Ideally, you'd use an algorithm to find if there's a cluster based on the coords
    # we could use pairwise distances, and calculate average distance of all points
    # if they are less than the T threshold, then we have a cluster. T could be
    # estimated by simply looping through the different set of coordinates and see how
    # the average distances behave.
    
    new_positions = simulate_movement(positions, speeds, 7520, max_lengths)
    for y in range(0, max_lengths[1]):
        row = ""
        for x in range(0, max_lengths[0]):
            if (x, y) in new_positions:
                row += "*"
            else:
                row += "."
        print(row)

    return 7520

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
