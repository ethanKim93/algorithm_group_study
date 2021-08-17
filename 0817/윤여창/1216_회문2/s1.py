import sys
sys.stdin = open('input.txt')

def row_max(board, max_count):
    for m in range(100):
        row = board[m]

        for i in range(100, max_count, -1):
            t = 100 - max_count + 1
            for j in range(t):
                if j + i <= 100:
                    word = row[j:j + i]
                    if word == word[::-1]:
                        if i > max_count:
                            max_count = i
    return max_count


def get_column_max(board, max_count):
    for m in range(100):
        column = ''
        for j in range(100):
            column += board[j][m]

        for i in range(100, max_count, -1):
            t = 100 - max_count + 1
            for j in range(100 - max_count + 1):
                if j + i <= 100:
                    word = column[j:j + i]
                    if word == word[::-1]:
                        if i > max_count:
                            max_count = i
    return max_count


def get_max(board):
    max_count = 0
    max_count = row_max(board, max_count)
    max_column = get_column_max(board, max_count)
    if max_column > max_count:
        max_count = max_column
    return max_count


for _ in range(10):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(input())
    answer = get_max(board)
    print('#{} {}'.format(tc, answer))
