import time
from typing import Literal

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day05.txt", "r") as file:
        data = file.read().strip().splitlines()
        rules = {}
        pages = []
        for line in data:
            if "|" in line:
                before, after = list(map(int, line.split("|")))
                if before not in rules.keys():
                    rules[before] = [after]
                else:
                    rules[before].append(after)
            elif "," in line:
                page_nums = list(map(int, line.split(",")))
                pages.append(page_nums)

    return rules, pages

def part_one(input_source: Literal["input", "examples"] = "input"):
    rules, pages = common(input_source)

    valid_updates = []
    for update in pages:
        update_valid = []
        for pidx, page in enumerate(update):
            if page in rules.keys():
                pages_after = set(update).intersection(rules[page])
                update_valid.append(all([pidx < update.index(n) for n in pages_after]))
        if all(update_valid):
            valid_updates.append(update)

    middle_pages = []
    for update in valid_updates:
        middle_pages.append(update[len(update) // 2])

    return sum(middle_pages)

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
