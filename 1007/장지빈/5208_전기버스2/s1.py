import sys
sys.stdin = open('input.txt')


def check(n, cnt):
    global ans
    if cnt >= ans:
        return
    if n >= N - 1:
        if ans > cnt:
            ans = cnt
        return
    for i in range(bat[n]):
        check(n + i + 1, cnt+1)

for tc in range(1, int(input())+1):
    ans = (100**2)+1
    li = list(map(int, input().split()))
    N = li[0]
    bat = li[1:]
    check(0, -1)

    print('#{} {}'.format(tc, ans))