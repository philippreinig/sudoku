from utils import *
import random


class Sudoku:
    def __init__(self, table: list[list[int]] = None):
        self.table = table if table is not None else [[None for i in range(9)] for _ in range(9)]

    def get_table(self):
        return self.table

    def set_val(self, row: int, col: int, val: int):
        if row < 1 or row > 9:
            raise ValueError(f"Invalid row index: {row}")
        if col < 1 or col > 9:
            raise ValueError(f"Invalid col index: {col}")
        if val < 1 or val > 9:
            raise ValueError(f"Invalid value: {val}")

        self.table[from_sudoku_index(row)][from_sudoku_index(col)] = val

    def get_val(self, row: int, col: int):
        if row < 1 or row > 9:
            raise ValueError(f"Invalid row index: {row}")
        if col < 1 or col > 9:
            raise ValueError(f"Invalid col index: {col}")

        return self.table[from_sudoku_index(row)][from_sudoku_index(col)]

    def get_row(self, row: int) -> list[int]:
        if row < 1 or row > 9:
            raise ValueError(f"Invalid row index: {row}")
        return self.table[from_sudoku_index(row)]

    def get_col(self, col: int) -> list[int]:
        if col < 1 or col > 9:
            raise ValueError(f"Invalid col index: {col}")
        col_vals = []
        for i in range(9):
            col_vals.append(self.table[i][from_sudoku_index(col)])
        return col_vals

    def get_block_1d(self, block: int) -> list[int]:
        indx_x = (block-1) // 3
        indx_y = (block-1) % 3

        block_vals = []

        for i in range(1, 4):
            for j in range(1, 4):
                block_vals.append(self.get_val(3*indx_x+i, 3*indx_y+j))

        return block_vals

    def get_block_2d(self, block_indx: int) -> list[list[int]]:
        indx_x = (block_indx-1) // 3
        indx_y = (block_indx-1) % 3

        block = []

        for i in range(1, 4):
            block_row = []
            for j in range(1, 4):
                block_row.append(self.get_val(3 * indx_x + i, 3 * indx_y + j))
            block.append(block_row)

        return block

    def is_valid(self, print_result=True) -> bool:
        errors = {"rows"  : [],
                  "columns"  : [],
                  "blocks": []}

        # Check all rows
        for row in range(1, 10):
            for val in range(1, 10):
                val_found_at_indx = []
                for col in range(1, 10):
                    if self.get_val(row, col) == val:
                        val_found_at_indx.append(col)

                if len(val_found_at_indx) > 1:
                    errors["rows"].append(f"Row {row} contains {val} {len(val_found_at_indx)} times at indexes: {val_found_at_indx}")
                if len(val_found_at_indx) == 0:
                    errors["rows"].append(f"Row {row} doesn't contain {val}")

        # Check all rows
        for col in range(1, 10):
            for val in range(1, 10):
                val_found_at_indx = []
                for row in range(1, 10):
                    if self.get_val(row, col) == val:
                        val_found_at_indx.append(col)

                if len(val_found_at_indx) > 1:
                    errors["columns"].append(
                        f"Column {col} contains {val} {len(val_found_at_indx)} times at indexes: {val_found_at_indx}")
                if len(val_found_at_indx) == 0:
                    errors["columns"].append(f"Column {col} doesn't contain {val}")

        # Check all blocks
        for block_indx in range(1, 10):
            block = self.get_block_1d(block_indx)
            for val in range(1, 10):
                val_found_at_indx = []
                for i in range(1, 10):
                    if block[from_sudoku_index(i)] == val:
                        val_found_at_indx.append(i)

                if len(val_found_at_indx) > 1:
                    errors["blocks"].append(f"Block {block_indx} contains {val} {len(val_found_at_indx)} times at indexes: {val_found_at_indx}")
                if len(val_found_at_indx) == 0:
                    errors["blocks"].append(f"Block {block_indx} doesn't contain {val}")

        # Print errors

        if len(errors["rows"]) == 0 and len(errors["columns"]) == 0 and len(errors["blocks"]) == 0:
            if print_result:
                print("Sudoku is entirely correct!")
            return True
        else:
            for element, error_list in errors.items():
                if print_result:
                    print(f"Found {len(error_list)} errors in {element}")
                    for error in error_list:
                        print(f"\t{error}")
            return False

    def is_filled(self):
        if any(None in row for row in self.table):
            return False
        return True

    def clear(self) -> None:
        for row in range(0, 9):
            for col in range(0, 9):
                self.table[row][col] = None

    def __str__(self):
            s = ""
            for i in range(9):
                if i > 0 and i % 3 == 0:
                    s += "------+-------+------\n"
                for j in range(9):
                    if j > 0 and j % 3 == 0:
                        s += "| "
                    if self.table[i][j] is None:
                        s += "  "
                    else:
                        s += str(self.table[i][j]) + " "
                    if j == 8:
                        s += "\n"
            return s


        # # Create a string representation of the list
        # result = ""
        # for row in self.table:
        #     for element in row:
        #         # Add the element to the result string with padding
        #         result += str(element if element is not None else " ").rjust(2) + " "
        #     result += "\n"
        #
        # return result