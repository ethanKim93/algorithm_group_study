import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))
    N_arr.sort(reverse=True)
    M_arr.sort(reverse=True)

    sum = 0
    while N_arr:
        if len(N_arr) == 0 or len(M_arr) == 0:
            break

        a = N_arr[0]
        b = M_arr[0]
        if b >= a:
            sum += a
            N_arr.pop(0)
            M_arr.pop(0)
        else:
            N_arr.pop(0)

    print('#{} {}'.format(tc, sum))
