import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for i in range(10)]

    for i in range(N):
        square = list(map(int, input().split()))
        for j in range(square[0], square[2]+1):
            for k in range(square[1], square[3]+1):
                arr[j][k] += square[4]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))