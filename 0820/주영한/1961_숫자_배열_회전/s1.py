import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print("#{}".format(tc))

    for row in range(N):
        for col in range(N):
            print(matrix[N - col - 1][row], end="")
        print(end=" ")
        for col in range(N):
            print(matrix[N - row - 1][N - col - 1], end="")
        print(end=" ")
        for col in range(N):
            print(matrix[col][N - row - 1], end="")
        print()