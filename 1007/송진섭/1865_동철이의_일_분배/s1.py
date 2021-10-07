import sys
sys.stdin = open('input.txt')


def find_max_rate(col, total):
    global max_success_rate

    if max_success_rate >= total:
        return
    if col == N:
        if max_success_rate < total:
            max_success_rate = total
        return
    else:
        for i in range(N):
            if not row_list[i]:
                row_list[i] = 1
                find_max_rate(col+1, total*work_table[i][col]/100)
                row_list[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_table = [list(map(int, input().split())) for _ in range(N)]
    row_list = [0] * N

    max_success_rate = 0
    find_max_rate(0, 1)
    ans = max_success_rate * 100
    print('#{} {:.6f}'.format(tc, ans))
