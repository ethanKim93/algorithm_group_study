import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = []
            for box in [row[j:j+M] for row in arr[i:i+M]]:
                fly += box

            if sum(fly) > maxV:
                maxV = sum(fly)
    print('#{} {}'.format(tc, maxV))