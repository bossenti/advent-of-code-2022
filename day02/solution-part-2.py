import os.path
from enum import Enum

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class CodeOpponent(Enum):
    A = "Rock"
    B = "Paper"
    C = "Scissors"


class CodeSelf(Enum):
    X = "LOOSE"
    Y = "DRAW"
    Z = "WIN"


class Scores(Enum):
    A = 1
    B = 2
    C = 3


response_strategies = {
    ("A", "X"): "C",
}


def compute(input_str: str) -> int:
    games = [game_raw.split(" ") for game_raw in input_str.split("\n")]

    score = 0
    for draw_opp, draw_self in games:

        if draw_self == CodeSelf.Y.name:
            score += Scores[draw_opp].value + 3
        elif draw_self == CodeSelf.X.name:

            if draw_opp == "A":
                score += Scores["C"].value
            elif draw_opp == "B":
                score += Scores["A"].value
            else:
                score += Scores["B"].value

        else:

            if draw_opp == "A":
                score += Scores["B"].value + 6
            elif draw_opp == "B":
                score += Scores["C"].value + 6
            else:
                score += Scores["A"].value + 6

    return score


def test_compute():
    INPUT = """A Y
B X
C Z"""

    assert 12 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
