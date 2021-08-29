import sys
sys.stdin = open("sample_input.txt")

color = ["W", "B", "R"]

for case in range(int(input())):
    N, M = map(int, input().split())

    flag = [input() for _ in range(N)]

    array = [[] for _ in range(N)]

    for row in range(N):
        for i in range(3):
            array[i].append(M - flag[row].count(color[i]))

    cost = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            total = sum(array[0][:i+1]) + sum(array[1][i+1:j+1]) + sum(array[2][j+1:])
            if total < cost:
                cost = total

    print("#{} {}".format(case + 1, cost))
