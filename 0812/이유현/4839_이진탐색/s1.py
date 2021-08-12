import sys

sys.stdin = open('sample_input.txt')


def search_cnt(start, end, num, cnt):
    while True:
        c = int((start + end) / 2)
        if num > c:
            cnt += 1
            start = c + 1

        elif num < c:
            cnt += 1
            end = c - 1

        else:
            return cnt


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    # print(search_cnt(A), search_cnt(B))
    result = '0'
    if search_cnt(1, P, A, 0) > search_cnt(1, P, B, 0):
        result = 'B'

    elif search_cnt(1, P, A, 0) < search_cnt(1, P, B, 0):
        result = 'A'
    else:
        result = '0'

    print('#{} {}'.format(tc, result))
