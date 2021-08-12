import sys

sys.stdin = open('sample_input.txt')


def search_cnt(num):
    global P
    start = 1
    cnt = 0

    while True:
        c = int((start + P) / 2)
        if num > c:
            cnt += 1
            start = c + 1

        elif num < c:
            cnt += 1
            P = c - 1

        else:
            return cnt


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    acnt = search_cnt(A)
    bcnt = search_cnt(B)
    print(acnt, bcnt)
    result = '0'
    if acnt > bcnt:
        result = 'B'

    elif acnt < bcnt:
        result = 'A'
    else:
        result = '0'

    print('#{} {}'.format(tc, result))
