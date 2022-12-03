import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(inpt: str) -> int:

    elf_raw_cal_list = inpt.split("\n\n")
    elf_cal_list = [[int(cal_val) for cal_val in elf.split("\n")] for elf in elf_raw_cal_list]
    elf_agg_cal_list = sorted([sum(cal_list) for cal_list in elf_cal_list])[::-1]

    return sum(elf_agg_cal_list[:3])


def test_compute():
    INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    assert 45000 == compute(inpt=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(inpt=f.read()))
