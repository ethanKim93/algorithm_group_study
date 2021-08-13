import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    zero2d = [[0]*10 for _ in range(10)]
    arr2d = [list(map(int, input().split())) for _ in range(N)]
    for arr in arr2d:
        for i in range(arr[0],arr[2]+1):
            for j in range(arr[1], arr[3]+1):
                zero2d[i][j] += arr[4]

    cnt = 0
    for zero1d in zero2d:
        for zero in zero1d:
            if zero == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))




