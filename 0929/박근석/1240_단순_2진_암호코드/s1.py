import sys
sys.stdin = open('input.txt')

T = int(input())

num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for i in range(N)]

    for i in range(N):
        for j in range(M-1,-1,-1):
            if matrix[i][j] == '1':
                break
        if matrix[i][j] == '1':
            break

    key = matrix[i][j-55:j+1]
    arr = []
    for i in range(8):
        arr.append(num.index(key[i*7:i*7+7]))
    total = 0
    for i in range(len(arr)):
        if i%2:
            total += arr[i]
        else:
            total += arr[i]*3

    if total%10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(arr)))




