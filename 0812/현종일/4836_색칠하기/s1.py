import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    result = 0
    for i in range(N):
        area = list(map(int, input().split()))
        x = [area[0], area[2]]
        y = [area[1], area[3]]
        for j in range(x[0], x[1]+1):
            for k in range(y[0], y[1]+1):
                if not arr[j][k]:
                    arr[j][k] = area[4]
                else:
                    arr[j][k] = 3

    for l in range(10):
        for m in range(10):
            if arr[l][m] == 3:
                result += 1
    print('#{} {}'.format(tc, result))