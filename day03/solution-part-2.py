import os.path
import string
from enum import Enum

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    rucksacks = [rucksack for rucksack in input_str.split("\n")]

    score = 0
    for idx in range(0, len(rucksacks), 3):

        badge = set(rucksacks[idx]).intersection(set(rucksacks[idx+1])).intersection(set(rucksacks[idx+2])).pop()

        item_index = list(string.ascii_lowercase).index(badge.lower()) + 1

        score += item_index + 26 * badge.isupper()

    return score


def test_compute():
    INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert 70 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
