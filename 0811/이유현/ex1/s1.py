import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0
    for i in range(N):
        for j in range(len(arr[i])):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if ni in range(N) and nj in range(N):
                    result += abs(arr[i][j] - arr[ni][nj])
    print(result)