import sys
sys.stdin = open("sample_input.txt")

def select_order(fac, cost, product):
    global result
    cost += cost_arr[product][fac]

    if cost > result:
        return

    if product >= N:
        if cost < result:
            result = cost
        return

    for i in range(1, N+1):
        if used[i] == 0:
            used[i] = 1
            select_order(i, cost, product+1)
            used[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    cost_arr = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)]
    used = [0] * (N+1)
    result = 99 * N

    select_order(0, 0, 0)

    print('#{} {}'.format(tc, result))




