import time
from typing import Literal, List

def common(input_source: Literal["input", "examples"] = "input"):
    with open(f"{input_source}/day04.txt", "r") as file:
        data = file.read().strip().splitlines()

    return data

def xmas_count(word_sample: List[str]) -> int:
    """
    Counts occurrences of `target_words` in rows, cols and diagonals.
    """
    total_count = 0
    target_words = ["XMAS", "SAMX"]
    SIZE_X, SIZE_Y = len(word_sample[0]), len(word_sample)
    # Vertical check
    for k in zip(*word_sample):
        joined_k = "".join(k)
        for word in target_words:
            total_count += joined_k.count(word)

    # Horizontal check
    for k in word_sample:
        joined_k = "".join(k)
        for word in target_words:
            total_count += joined_k.count(word)

    # Diagonal check
    # Upper left -> Bottom right
    # Up until mid diagonal
    for n in range(SIZE_X):
        i, j = 0, n
        joined_ij = ""
        joined_ij_r = ""
        while i < SIZE_X and j >= 0:
            joined_ij += word_sample[i][j]
            joined_ij_r += word_sample[::-1][i][j]
            i += 1
            j -= 1
        for word in target_words:
            total_count += joined_ij.count(word)
            total_count += joined_ij_r.count(word)

    # Mid diagonal to bottom right
    for n in range(1, SIZE_Y):
        i, j = n, SIZE_X - 1
        joined_ij = ""
        joined_ij_r = ""
        while i < SIZE_Y and j >= 0:
            joined_ij += word_sample[i][j]
            joined_ij_r += word_sample[::-1][i][j]
            i += 1
            j -= 1
        for word in target_words:
            total_count += joined_ij.count(word)
            total_count += joined_ij_r.count(word)

    return total_count

def part_one(input_source: Literal["input", "examples"] = "input"):
    word_sample = common(input_source)
    return xmas_count(word_sample)

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
