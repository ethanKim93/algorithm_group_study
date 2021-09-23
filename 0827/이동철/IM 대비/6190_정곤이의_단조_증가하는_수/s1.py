import sys
sys.stdin = open('s_input.txt')


def check(n):
    n = str(n)
    for k in range(len(n)-1):
        if n[k] > n[k+1]:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_arr = list(map(int, input().split()))

    max_num = -1
    for i in range(len(N_arr) - 1):
        for j in range(i + 1, len(N_arr)):
            num = N_arr[i] * N_arr[j]
            if max_num < num and check(num):
                max_num = num
    print('#{} {}'.format(tc, max_num))
