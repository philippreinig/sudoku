def to_sudoku_index(i: int) -> int:
    return i + 1


def from_sudoku_index(i: int) -> int:
    return i - 1

def get_block_indx_of_cell(row: int, col: int) -> int:
    return ((row-1) // 3) * 3 + ((col-1) // 3) + 1
