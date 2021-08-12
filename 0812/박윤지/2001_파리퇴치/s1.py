import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fly_list = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for di in range(M):
                for dj in range(M):
                    fly += arr[i+di][j+dj]
            fly_list.append(fly)

    maxV = 0
    for fly in fly_list:
        if maxV < fly:
            maxV = fly

    print('#{} {}'.format(tc, maxV))
