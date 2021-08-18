import sys
sys.stdin = open('input.txt')


def pascal(n):
    arr[0] = [1]
    if n > 1:
        for i in range(1, n):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(arr[i-1][j-1] + arr[i-1][j])
            arr[i] = temp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    pascal(N)
    print('#{}'.format(tc))
    for i in range(N):
        print(*arr[i], sep=' ')