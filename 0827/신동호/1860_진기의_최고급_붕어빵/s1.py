import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    bread = []
    for i in range(1, N//K+2):
        bread += [i * M] * K
    arr.sort()

    for t in range(N):
        if bread.pop(0) > arr[t]:
            print('#{} Impossible'.format(tc))
            break
    else:
        print('#{} Possible'.format(tc))

