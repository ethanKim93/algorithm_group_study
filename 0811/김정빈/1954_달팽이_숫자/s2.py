import sys
sys.stdin = open("input.txt")

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    while N > 0:
        for i in range(N):
            for j in range(N):
                print(arr[i][j], "#")
                print(arr[j][i])
                N -= 1