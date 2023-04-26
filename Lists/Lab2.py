# import sys

# from termcolor import colored, cprint

# board = []

# for i in range(8):
#     row = [' ' for i in range(8)]
#     board.append(row)

# for j in range(8):
#     board[0][j] = f"[0][{j}]"
#     board[1][j] = 'b'
#     board[2][j] = f"[2][{j}]"
#     board[3][j] = f"[3][{j}]"
#     board[4][j] = f"[4][{j}]"
#     board[5][j] = f"[5][{j}]"
#     board[6][j] = 'b'
#     board[7][j] = f"[7][{j}]"
    
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if (i+j) % 2 != 0:
#             cprint(board[i][j], "black", end=" ")
#         else:
#             cprint(board[i][j], "white", end=" ")
#     print("")

# for row in board:
#     for cell in row:
#         print(cell, end=' ')
#     print()

#TODO

from termcolor import colored, cprint

board = [[' ' for i in range(8)] for j in range(8)]

for j in range(8):
    board[0][j] = f"[0][{j}]"
    board[1][j] = '  b   '
    board[2][j] = f"[2][{j}]"
    board[3][j] = f"[3][{j}]"
    board[4][j] = f"[4][{j}]"
    board[5][j] = f"[5][{j}]"
    board[6][j] = '  b   '
    board[7][j] = f"[7][{j}]"
    
for i in range(len(board)):
    for j in range(len(board[0])):
        color = "black" if (i+j) % 2 != 0 else "white"
        cprint(board[i][j], color, end=" ")
    print()


# for row in board:
#     print(' '.join(row))
