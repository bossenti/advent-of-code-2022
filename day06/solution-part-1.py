import os.path

import pytest as pytest

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    for i in range(len(input_str)):

        if i < len(input_str) - 4:
            sequence = input_str[i:i + 4]
        else:
            sequence = input_str[i:]

        if len(set(sequence)) == 4:
            return i + 4


@pytest.mark.parametrize("test_data, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
])
def test_compute(test_data, expected):
    INPUT = test_data

    assert expected == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
