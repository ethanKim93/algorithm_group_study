import sys
sys.stdin = open('sample_input.txt')


def in_order(n, MaxN):
    global k
    if n <= MaxN:
        in_order(n * 2, MaxN)
        arr[n] = k
        k += 1
        in_order(n * 2 + 1, MaxN)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [0] * (N + 1)
    k = 1
    in_order(1, N)

    print('#{} {} {}'.format(tc, arr[1], arr[N//2]))


