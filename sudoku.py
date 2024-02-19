'''
Note: Sudoku has number 1-9 w/ each row, column and 3x3
box not having duplicate numbers.
'''
from random import choice

sudoku = [[4, 0, 0, 0, 0, 0, 0, 3, 0],
          [0, 0, 0, 0, 3, 0, 0, 0, 0],
          [0, 3, 0, 0, 5, 1, 9, 0, 4],
          [0, 8, 0, 0, 0, 5, 3, 2, 0],
          [0, 0, 1, 0, 0, 0, 7, 0, 0],
          [0, 4, 2, 3, 0, 0, 0, 8, 0],
          [6, 0, 7, 2, 4, 0, 0, 5, 0],
          [0, 0, 0, 0, 8, 0, 0, 0, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 6]]

sudoku_og = [[4, 0, 0, 0, 0, 0, 0, 3, 0],
             [0, 0, 0, 0, 3, 0, 0, 0, 0],
             [0, 3, 0, 0, 5, 1, 9, 0, 4],
             [0, 8, 0, 0, 0, 5, 3, 2, 0],
             [0, 0, 1, 0, 0, 0, 7, 0, 0],
             [0, 4, 2, 3, 0, 0, 0, 8, 0],
             [6, 0, 7, 2, 4, 0, 0, 5, 0],
             [0, 0, 0, 0, 8, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0, 6]]


def print_sudoku(sudoku):
    for r in range(len(sudoku)):
        if r % 3 == 0 and r != 0:
            print("-------------------------")
        for c in range(len(sudoku[r])):
            if c % 3 == 0 and c != 0:
                print(" | ", end = " ")
            if c == 8:
                print(str(sudoku[r][c]))
            else:
                print(str(sudoku[r][c]), end = " ")

def print_sudoku_hint(sudoku, sudoku_og, type):
    # type 1 = 3 hints
    # type 2 = 6 hints
    # type 3 = 9 hints
    type = type * 3

    poss = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for i in range(type):
        while True:
            row = choice(poss)
            col = choice(poss)
            # If zero empty is found, replace with hint from solution
            if sudoku_og[row][col] == 0:
                sudoku_og[row][col] = sudoku[row][col]
                break
            else:
                continue

    print_sudoku(sudoku_og)


# Return position (row, column) of empty spot
def find_empty(sudoku):
    for r in range(len(sudoku)):
        for c in range(len(sudoku[r])):
            if sudoku[r][c] == 0:
                return r, c
    return None

# returns bool if correct or not
def correct(sudoku, num, pos):
    # Check that there aren't any duplicates in row
    for i in range(len(sudoku[0])):
        # If there are duplicates (excluding last position), return false
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    # Check that there aren't any duplicates in column
    for i in range(len(sudoku[0])):
        # If there are duplicates (excluding last position), return false
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Check that there aren't any duplicates in 3x3 square
    current_box = pos[1] // 3
    current_box_height = pos[0] // 3

    for i in range(current_box_height * 3, current_box_height * 3 + 3):
        for j in range(current_box * 3, current_box * 3 + 3):
            # If there are duplicates (excluding last position), return false
            if sudoku[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(sudoku):
    empty = find_empty(sudoku)
    # If no empty spots left, the sudoku is solved
    if not empty:
        return True
    else:
        row, col = empty
    for i in range(1, 10):
        if correct(sudoku, i,(row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True
            sudoku[row][col] = 0

    return False

def main():
    while True:
        if solve(sudoku):
            break

    while True:
        user = input("Would you like a hint or solution: ").casefold().strip()
        if user == "solution":
            print_sudoku(sudoku)
            break
        elif user == "hint":
            while True:
                try:
                    hint_type = int(input("Would you like a \n "
                                          "1: little hint \n "
                                          "2: medium hint \n "
                                          "3: big hint\n"))
                except ValueError:
                    print("Please enter a integer")

                else:
                    if hint_type in [1, 2, 3]:
                        print_sudoku_hint(sudoku, sudoku_og, hint_type)
                        exit()
                    else:
                        print("Please enter a integer from [1, 3]")


main()