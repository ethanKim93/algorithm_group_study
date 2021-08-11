dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

import sys
sys.stdin = open("input.txt")

T = int(input())

for case in range(T):
    N = int(input())
    li = []

    for n in range(N):
        li.append(list(map(int, input().split())))
    val = 0
    for row in range(N):
        for col in range(N):
            for i in range(4):
                if 0 <= row + dy[i] < N and 0 <= col + dx[i] < N:
                    val += abs(li[row + dy[i]][col + dx[i]] - li[row][col])

    print("#{} {}".format(case + 1, val))

