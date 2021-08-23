import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for row in range(N):
        temp = []
        for num in input():
            temp.append(int(num))
        matrix.append(temp)
    profit = 0
    for row in range(N // 2):
        for col in range(N // 2 - row, N // 2 + row + 1):
            profit += matrix[row][col]
            profit += matrix[N - 1 - row][col]
    for col in range(N):
        profit += matrix[N//2][col]
    print("#{} {}".format(tc, profit))