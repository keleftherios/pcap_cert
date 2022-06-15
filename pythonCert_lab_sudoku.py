# Scenario
# As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board.
# The player has to fill the board in a very specific way:
#
# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
# If you need more details, you can find them in https://en.wikipedia.org/wiki/Sudoku.
#
# Your task is to write a program which:
#
# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.
# Test your code using the data we've provided.
#
# Test data
# Sample input:
#
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# Sample output:
#
# Yes
#
#
# Sample input:
#
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
# Sample output:
#
# No


# row_list = []
# count = 1
# while count < 10:
#     count += 1
#     data = input()
#     if data.isdigit() and len(data) == 9:
#         row_list.append(data)
#     else:
#         print("Invalid input...")
#         break

# row_list = ['295743861', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '154938672']
row_list = ['195743862', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '254938671']


def check_sudoku_list(list_name):
    pattern = [str(i) for i in range(1, 10)]
    for row in list_name:
        if pattern != sorted(list(row)):
            return False
    return True


def create_col_list(list_name):
    newList = []
    for col in range(9):
        data = ''
        for L in list_name:
            data += L[col]
        newList.append(data)
    return newList


#TODO: Refactor beflow function, to be more efficient!!!
def create_tile_list(list_name):
    newList = []
    row_start, row_end = 0, 3
    for _ in range(3):
        col_start, col_end = 0, 3
        for _ in range(3):
            tile = []
            for row in range(row_start, row_end):
                data = ''
                for col in range(col_start, col_end):
                    data += list_name[row][col]
                tile.append(data)
            col_start += 3
            col_end += 3
            newList.append(''.join(tile))
        row_start += 3
        row_end += 3
    return newList


def display_list(list_name):
    for i in list_name:
        print(list(i))


col_list = create_col_list(row_list)
tile_list = create_tile_list(row_list)
if check_sudoku_list(row_list) and check_sudoku_list(col_list) and check_sudoku_list(tile_list):
    print("Yes")
else:
    print("No")

L = []
start_row = start_col = 0
for t in range(1, 10):
    tile = []
    for r in range(1, 10):
        data = ''
        row = (r - 1) // t
        for c in range(start_col, 10):
            col = (c - 1) % t
            data += row_list[row][col]
        tile.append(data)
    L.append(''.join(tile))
