import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))

    c = []
    for i, chs in enumerate(ci):
        c.append([i+1, chs])

    q = []
    for _ in range(N):
        q.append(c.pop(0))

    while len(q) > 1:
        check = q.pop(0)
        check[1] //= 2
        if check[1]:
            q.append(check)
        else:
            if c:
                q.append(c.pop(0))
    print('#{} {}'.format(tc, q[0][0]))