import time
from collections import deque, defaultdict
from typing import Literal, List, Tuple, Dict

Page = List[int]
RuleMap = Dict[int, List[int]]
ClassifiedUpdates = Tuple[List[Page], List[Page]]

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

def classify_updates(pages: List[Page], rules: RuleMap) -> ClassifiedUpdates:
    valid_updates = []
    invalid_updates = []
    for update in pages:
        if is_ordered(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates

def is_ordered(update: Page, rules: RuleMap) -> bool:
    update_valid = []
    for pidx, page in enumerate(update):
        if page in rules.keys():
            pages_after = set(update).intersection(rules[page])
            update_valid.append(all([pidx < update.index(n) for n in pages_after]))

    return all(update_valid)

def topological_sort(update: Page, rules: RuleMap) -> Page:
    """https://en.wikipedia.org/wiki/Topological_sorting"""
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for page in update:
        if page in rules:
            for after in rules[page]:
                if after in update:
                    graph[page].append(after)
                    in_degree[after] += 1
                    if after not in in_degree:
                        in_degree[after] = 0

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
    while queue:
        page = queue.popleft()
        sorted_update.append(page)

        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def part_one(input_source: Literal["input", "examples"] = "input") -> int:
    rules, pages = common(input_source)

    valid_updates, _ = classify_updates(pages=pages, rules=rules)
    middle_pages = [update[len(update) // 2] for update in valid_updates]

    return sum(middle_pages)

def part_two(input_source: Literal["input", "examples"] = "input") -> int:
    rules, pages = common(input_source)

    _, invalid_updates = classify_updates(pages=pages, rules=rules)

    ordered_updates = []
    for update in invalid_updates:
        sorted_update = topological_sort(update, rules)
        if sorted_update:
            ordered_updates.append(sorted_update)

    middle_pages = [update[len(update) // 2] for update in ordered_updates]

    return sum(middle_pages)

if __name__ == "__main__":
    start_one = time.perf_counter()
    result_one = part_one()
    end_one = time.perf_counter()
    print(f"Part one: {result_one}, took {end_one - start_one:.6f} seconds")

    start_two = time.perf_counter()
    result_two = part_two()
    end_two = time.perf_counter()
    print(f"Part two: {result_two}, took {end_two - start_two:.6f} seconds")
