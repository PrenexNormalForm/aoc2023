from math import prod
from typing import Set


with open("day/03/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def is_symbol(row: int, col: int) -> bool:
    if row < 0 or row >= len(lines):
        return False
    if col < 0 or col >= len(lines[row]):
        return False
    char = lines[row][col]
    return char != "." and not char.isdigit()


def parse_num(row: int, col: int) -> int:
    if not lines[row][col].isdigit():
        raise ValueError(f"no number at {row}{col}")
    num = int(lines[row][col])
    col += 1
    while col < len(lines[row]) and lines[row][col].isdigit():
        num = num * 10 + int(lines[row][col])
        col += 1
    return num


def locate_num_start(row: int, col: int) -> int:
    if not lines[row][col].isdigit():
        raise ValueError(f"no number at {row},{col}")
    while col >= 0 and lines[row][col].isdigit():
        col -= 1
    return col + 1


def identify_adjacent_numbers(row: int, col: int) -> Set:
    if not is_symbol(row, col):
        raise ValueError(f"{row:},{col:} must be symbol")
    numbers = {}
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (
                i >= 0
                and i < len(lines)
                and j >= 0
                and j < len(lines[i])
                and lines[i][j].isdigit()
            ):
                num_start = locate_num_start(i, j)
                num = parse_num(i, num_start)
                numbers[(i, num_start)] = num
    return set(numbers.values())


if __name__ == "__main__":
    # part 1
    sum = 0
    for line_index, line in enumerate(lines):
        line = line.strip()
        index = 0
        while index < len(line):
            digit_offset = 1
            if line[index].isdigit():
                num = int(line[index])
                while (
                    index + digit_offset < len(line)
                    and line[index + digit_offset].isdigit()
                ):
                    num = num * 10 + int(line[index + digit_offset])
                    digit_offset += 1
                for row in range(line_index - 1, line_index + 2):
                    for col in range(index - 1, index + digit_offset + 1):
                        if is_symbol(row, col):
                            sum += num
            index += digit_offset
    print(f"sum of part numbers: {sum}")

    # part 2
    sum = 0
    for row, line in enumerate(lines):
        for col, _ in enumerate(line):
            if is_symbol(row, col):
                adjacent_nums = identify_adjacent_numbers(row, col)
                if len(adjacent_nums) == 2:
                    sum += prod(adjacent_nums)
    print(f"sum of gear ratios: {sum}")
