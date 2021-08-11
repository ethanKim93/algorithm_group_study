import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for i in range(100)]

    max_v1 = 0
    s1 = 0
    for i in range(100): #오른쪽 아래 대각선 합
        s1 += arr[i][i]
    max_v1 = s1


    s2 = 0
    for j in range(100):
        s2 += arr[j][99-j] #왼쪽 아래 대각선 합
    if max_v1 < s2:
        max_v1 = s2

    for i in range(100):
        s3 = 0
        for j in range(100):
            s3 += arr[i][j]
        if max_v1 < s3:
            max_v1 = s3

    for j in range(100):
        s4 = 0
        for i in range(100):
            s4 += arr[i][j]
        if max_v1 < s4:
            max_v1 = s4

    print('#{} {}'.format(tc, max_v1))

