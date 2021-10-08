import sys
sys.stdin = open('sample_input.txt')


def find_min_price(col, total):
    global min_price

    if min_price < total:
        return
    if col == N:
        if min_price > total:
            min_price = total
        return
    else:
        for i in range(N):
            if not row_list[i]:
                row_list[i] = 1
                find_min_price(col+1, total+price_table[i][col])
                row_list[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_table = [list(map(int, input().split())) for _ in range(N)]
    row_list = [0] * N

    min_price = 99 * N
    find_min_price(0, 0)
    print(min_price)
