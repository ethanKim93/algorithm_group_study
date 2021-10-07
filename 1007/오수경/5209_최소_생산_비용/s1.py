import sys
sys.stdin = open('sample_input.txt')

def how_much(j, tmp):
    global N, pay

    if tmp >= pay:
        return

    if product == [1]*N:
        if tmp < pay:
            pay = tmp
            return

    for i in range(N):
        if product[i] == 0:
            product[i] = 1
            how_much(j + 1, tmp+cost[i][j])
            product[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    product = [0]*N     # i
    pay = 99*N
    how_much(0, 0)


    print('#{} {}'.format(tc, pay))