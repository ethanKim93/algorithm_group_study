import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = [[] for _ in range(N)]

    for j in range(N):
        num = ''
        for i in range(N-1, -1, -1):
            num += arr[i][j]
        result[j].append(num)

    for i in range(N-1, -1, -1):
        num = ''
        for j in range(N-1, -1, -1):
            num += arr[i][j]
        result[N-1-i].append(num)

    for j in range(N-1, -1, -1):
        num = ''
        for i in range(N):
            num += arr[i][j]
        result[N-1-j].append(num)

    print('#{}'.format(tc))
    for row in result:
        print(*row)


    

'''
00 02 22 00
01 12 21 10
02 22 20 20

10 01 12 21
11 11 11 11
12 21 10 01

20 00 02 22
21 10 01 12
22 20 00 02
'''