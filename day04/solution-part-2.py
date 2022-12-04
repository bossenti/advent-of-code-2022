import os.path
import string
from enum import Enum

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    items = [_ for _ in input_str.split("\n")]

    score = 0
    for item in items:
        elf_a_raw, elf_b_raw = item.split(",")[0].split("-"), item.split(",")[1].split("-")
        elf_a_plan, elf_b_plan = set(range(int(elf_a_raw[0]), int(elf_a_raw[1]) + 1)), \
                                 set(range(int(elf_b_raw[0]), int(elf_b_raw[1]) + 1))

        if len(elf_a_plan.intersection(elf_b_plan)) > 0:
            score += 1

    return score


def test_compute():
    INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    assert 4 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
