import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pascals = [[0] * idx for idx in range(1, N + 1)]
    for row in range(N):
        col_size = len(pascals[row])
        for col in range(col_size):
            if col == 0 or col == col_size - 1:
                pascals[row][col] = 1
            else :
                pascals[row][col] = pascals[row - 1][col - 1] + pascals[row - 1][col]
    print("#{}".format(tc))
    for pascal in pascals:
        for elem in pascal:
            print(elem, end=" ")
        print()