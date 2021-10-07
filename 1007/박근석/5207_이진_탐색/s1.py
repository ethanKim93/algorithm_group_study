import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def search(arr, x):
    global cnt
    l = 0
    r = len(arr) - 1
    check = 0
    while l <= r:
        m = (l + r) // 2

        if arr[m] == x:
            cnt += 1
            return
        elif arr[m] < x and (check == 0 or check == 1):
            l = m + 1
            check = 2

        elif arr[m] > x and (check == 0 or check == 2):
            r = m - 1
            check = 1
        else:
            break

    return

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = sorted(list(map(int, input().split())))
    M_arr = list(map(int, input().split()))
    cnt = 0
    for i in range(len(M_arr)):
        search(N_arr, M_arr[i])
    print('#{} {}'.format(tc, cnt))