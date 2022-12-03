import os.path
import string
from enum import Enum

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    rucksacks = [rucksack for rucksack in input_str.split("\n")]

    score = 0
    for rucksack in rucksacks:
        comp_size = int(len(rucksack) / 2)
        comp_a, comp_b = set(rucksack[:comp_size]), set(rucksack[comp_size:])

        assert len(comp_b), len(comp_a)

        doubled_item = comp_a.intersection(comp_b).pop()

        assert len(doubled_item), 1

        item_index = list(string.ascii_lowercase).index(doubled_item.lower()) + 1

        score += item_index + 26 * doubled_item.isupper()

    return score


def test_compute():
    INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert 157 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
