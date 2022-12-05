import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    items = [_ for _ in input_str.split("\n")]

    score = 0
    for item in items:
        pass

    return score


def test_compute():
    INPUT = """"""

    assert 0 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
