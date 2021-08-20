import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [0] * 200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2:
            s = s//2
        else:
            s = s//2 - 1
        if e % 2:
            e = e//2
        else:
            e = e//2 -1
        for i in range(s, e+1):
            rooms[i] += 1

    print('#{} {}'.format(tc, max(rooms)))
