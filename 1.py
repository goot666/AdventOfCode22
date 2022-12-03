"""Advent of code day 1."""


def elf_with_most_calories(input):
    """Find the elf with the most calories."""
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    elfs_calories = []
    calorie_count = 0

    for line in lines:
        if line != '':
            calorie_count += int(line)
        else:
            elfs_calories.append(calorie_count)
            calorie_count = 0

    # sorted_elfs = sorted(elfs_calories, reverse=True)
    max_elf = max(elfs_calories)

    return max_elf


print(elf_with_most_calories('input.txt'))