import os.path

import numpy

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def get_viewing_distance(height, heights_in_direction):
    count = 0

    for idx, h in enumerate(heights_in_direction):
        if height > h:
            count += 1
        elif height <= h:
            count += 1
            break

    return count


def compute(input_str: str) -> int:
    items = [_ for _ in input_str.split("\n")]

    num_rows = len(items)
    num_columns = len(items[0])

    rows = {idx: [int(tree) for tree in items[idx]] for idx in range(num_rows)}
    columns = {idx: [int(row[idx]) for row in rows.values()] for idx in range(num_columns)}

    max_scenic_score = 0

    for row_idx, row in enumerate(list(rows.values())[1:-1]):

        for col_idx, tree in enumerate(row[1:-1]):

            single_view_scores = []

            # look right
            single_view_scores.append(get_viewing_distance(tree, row[col_idx + 2:]))

            # look left
            single_view_scores.append(get_viewing_distance(tree, row[:col_idx + 1][::-1]))

            # look top
            single_view_scores.append(get_viewing_distance(tree, columns[col_idx + 1][:row_idx + 1][::-1]))

            # look down
            single_view_scores.append(get_viewing_distance(tree, columns[col_idx + 1][row_idx + 2:]))

            total_scenic_score = numpy.prod(single_view_scores)

            if total_scenic_score > max_scenic_score:
                max_scenic_score = total_scenic_score

    return max_scenic_score


def test_compute():
    INPUT = """30373
25512
65332
33549
35390"""

    assert 8 == compute(input_str=INPUT)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        print(compute(input_str=f.read()))
