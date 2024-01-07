from sudoku_generator import generate_sudoku

def main():
    sudoku, solution = generate_sudoku(3)
    print(sudoku)

    input("Please press any key to show the solution")

    print(solution)

if __name__ == "__main__":
    main()