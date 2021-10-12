import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N = (N//10)*10
    print('#{}'.format(tc))
    print(N//50000, end=' ')
    if N//50000:
        N = N%50000
    print(N // 10000, end=' ')
    if N // 10000:
        N = N % 10000
    print(N // 5000, end=' ')
    if N // 5000:
        N = N % 5000
    print(N // 1000, end=' ')
    if N // 1000:
        N = N % 1000
    print(N // 500, end=' ')
    if N // 500:
        N = N % 500
    print(N // 100, end=' ')
    if N // 100:
        N = N % 100
    print(N // 50, end=' ')
    if N // 50:
        N = N % 50
    print(N // 10, end=' ')
    if N // 10:
        N = N % 10
    print()





