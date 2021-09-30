import sys
sys.stdin = open('input.txt')


def on_off(n, m):
    global ans
    for _ in range(n):
        if not m % 2:  # b0부터 bn까지 확인
            ans = 'OFF'
            return
        m //= 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 'ON'
    on_off(N, M)
    print('#{} {}'.format(tc, ans))