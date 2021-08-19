import sys
sys.stdin = open('input.txt')

T = int(input())

arr = [[1], [1, 1]]

for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        print('#{}'.format(tc))
        print(1)
    elif N == 2:
        print('#{}'.format(tc))
        print(1)
        print(*arr[1])
    else:
        elem = [1]
        for i in range(0, N-2):
            elem.append(arr[N-2][i] + arr[N-2][i+1])
        elem.append(1)
        arr.append(elem)
        print('#{}'.format(tc))
        for k in range(0, N):
            print(*arr[k])