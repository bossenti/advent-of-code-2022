import os.path

import pytest as pytest

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    for i in range(len(input_str)):

        if i < len(input_str) - 14:
            sequence = input_str[i:i + 14]
        else:
            sequence = input_str[i:]

        if len(set(sequence)) == 14:
            return i + 14


@pytest.mark.parametrize("test_data, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
])
def test_compute(test_data, expected):
    INPUT = test_data

    assert expected == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
