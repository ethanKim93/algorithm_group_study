import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            arsum = 0
            for k in range(M):
                for l in range(M):
                    arsum += arr[i+k][j+l]
            if arsum > max_sum:
                max_sum = arsum
    print('#{} {}'.format(test_case, max_sum))


