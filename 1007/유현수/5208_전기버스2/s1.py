import sys
sys.stdin = open('sample_input.txt')


def backtrack(idx):
    global ans, cnt
    if idx >= len(bus_stop):
        if ans > cnt:
            ans = cnt
        return

    if ans <= cnt:
        return

    for i in range(idx+bus_stop[idx], idx, -1):
        cnt += 1
        backtrack(i)
        cnt -= 1


T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    ans = 987654321
    cnt = 0
    backtrack(1)
    print('#{} {}'.format(tc, ans-1))

