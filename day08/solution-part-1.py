import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    items = [_ for _ in input_str.split("\n")]

    num_rows = len(items)
    num_columns = len(items[0])

    visible_trees = 4 * (num_rows - 1)

    rows = {idx: [int(tree) for tree in items[idx]] for idx in range(num_rows)}
    columns = {idx: [int(row[idx]) for row in rows.values()] for idx in range(num_columns)}

    for row_idx, row in enumerate(list(rows.values())[1:-1]):

        for col_idx, tree in enumerate(row[1:-1]):

            is_visible = False

            # look right
            if tree > max(row[col_idx+2:]):
                is_visible = True
            elif tree > max(row[:col_idx+1]):  # look left
                is_visible = True
            elif tree > max(columns[col_idx+1][:row_idx+1]):  # look top
                is_visible = True
            elif tree > max(columns[col_idx+1][row_idx+2:]):  # look down
                is_visible = True

            if is_visible:
                visible_trees += 1

    return visible_trees


def test_compute():
    INPUT = """30373
25512
65332
33549
35390"""

    assert 21 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
