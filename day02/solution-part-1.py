import os.path
from enum import Enum

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class CodeOpponent(Enum):
    A = "Rock"
    B = "Paper"
    C = "Scissors"


class CodeSelf(Enum):
    X = "Rock"
    Y = "Paper"
    Z = "Scissors"


class Scores(Enum):
    X = 1
    Y = 2
    Z = 3


def compute(input_str: str) -> int:
    games = [game_raw.split(" ") for game_raw in input_str.split("\n")]

    score = 0
    for draw_opp, draw_self in games:

        if CodeOpponent[draw_opp].value == CodeSelf[draw_self].value:
            score += Scores[draw_self].value + 3
        elif (draw_opp == CodeOpponent.A.name and draw_self == CodeSelf.Y.name) or \
                (draw_opp == CodeOpponent.B.name and draw_self == CodeSelf.Z.name) or\
                (draw_opp == CodeOpponent.C.name and draw_self == CodeSelf.X.name):
            score += Scores[draw_self].value + 6
        else:
            score += Scores[draw_self].value

    return score


def test_compute():
    INPUT = """A Y
B X
C Z"""

    assert 15 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
