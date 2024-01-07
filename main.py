from sudoku_generator import generate_sudoku

def main():
    sudoku, solution = generate_sudoku(3)
    print(sudoku)

    sudoku.visualize()

    print(solution)

    solution.visualize()

if __name__ == "__main__":
    main()