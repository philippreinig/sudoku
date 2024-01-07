from sudoku import Sudoku
from utils import *
import random
import copy

def solve_sudoku(s: Sudoku, max_attemps=100_000):
    if s.is_filled():
        if not s.is_valid(print_result=False):
            raise AssertionError("The Sudoku is filled, but invalid!")
        return s

    failed_attempts = 0

    while failed_attempts < max_attemps and not s.is_filled():
        for row_indx in range(1, 10):
            for col_indx in range(1, 10):
                valid_vals = [1,2,3,4,5,6,7,8,9]

                for val in s.get_row(row_indx):
                    if val in valid_vals: valid_vals.remove(val)
                for val in s.get_col(col_indx):
                    if val in valid_vals: valid_vals.remove(val)
                for val in s.get_block_1d(get_block_indx_of_cell(row_indx, col_indx)):
                    if val in valid_vals: valid_vals.remove(val)

                if len(valid_vals) == 0:
                    failed_attempts += 1
                    s.clear()
                    break
                else:
                    rand_indx = random.randint(0, len(valid_vals) - 1)
                    s.set_val(row_indx, col_indx, valid_vals[rand_indx])
            else:
                continue
            break
        else:
            continue

    if failed_attempts == max_attemps:
        print(f"Stopping because 10_000 iterations failed")
    else:
        print(f"Successfully generated a valid Sudoku (generated {failed_attempts} invalid solutions in the process)")
        return s

def generate_sudoku(difficulty = 3):
    solution = solve_sudoku(Sudoku())
    s = copy.deepcopy(solution)
    assert s.is_valid(print_result=False) , f"Sudoku is valid: {s.is_valid()}"
    assert not any(None in row for row in s.get_table())
    sudoku_table = s.get_table()

    difficulties = {1: 36, 2: 28, 3: 24, 4: 22, 5: 17}

    removed = 0

    while removed < (81 - difficulties[difficulty]):
        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        if sudoku_table[rand_row][rand_col] is not None:
            sudoku_table[rand_row][rand_col] = None
            removed += 1

    return s, solution


