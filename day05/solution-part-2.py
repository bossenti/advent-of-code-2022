import os.path
import re
from collections import namedtuple
from typing import List

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

Instruction = namedtuple("Instruction", ["amount", "start", "target"])


def retrieve_start_constellation(starting_stacks_raw: List[str]):

    num_stacks = max([int(g) for g in re.findall("([1-9])", starting_stacks_raw[0])])

    ship = {}
    for idx, stack_row in enumerate(starting_stacks_raw[1:]):

        expected_length = (num_stacks - 1) * 4 + 3
        if len(stack_row) != expected_length:
            stack_row += " " * (expected_length - len(stack_row))
        for n in range(1, num_stacks + 1, 1):
            if n == 1:
                crate = stack_row[1]
            elif n == num_stacks:
                crate = stack_row[-2]
            else:
                crate = stack_row[(n - 1) * 4 + 1]

            if crate != " ":
                if n in ship.keys():
                    ship[n].append(crate)
                else:
                    ship.update({n: [crate]})

    return ship


def apply_instructions(instructions: List[Instruction], starting_constellation: dict):
    for instruction in instructions:
        amount, start, target = instruction

        crates_to_move = starting_constellation[start][-amount:]
        starting_constellation[start] = starting_constellation[start][:-amount]
        starting_constellation[target].extend(crates_to_move)

    return starting_constellation


def compute(input_str: str) -> str:
    starting_stacks, instructions_raw = input_str.split("\n\n")

    instructions = []
    for instr_raw in instructions_raw.split("\n"):
        m = re.search("move ([0-9][0-9]?) from ([0-9]) to ([0-9])", instr_raw)
        instructions.append(Instruction(*[int(g) for g in m.groups()]))

    starting_stacks_raw = starting_stacks.split("\n")[::-1]

    starting_constellation = retrieve_start_constellation(starting_stacks_raw=starting_stacks_raw)

    final_constellation = apply_instructions(instructions, starting_constellation)

    return "".join(stack[-1] for k, stack in final_constellation.items())


def test_compute():
    INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    assert "MCD" == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
