import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(1,T+1):
    tc = input()
    data = list(map(int, input().split()))
    N = 8
    q = []
    for i in range(N):
        q.append(data[i])
    while q[-1] != 0:
        for k in range(1,6):
            t = q.pop(0) - k
            if t <= 0:
                q.append(0)
                break
            q.append(t)
    print('#{} {}'.format(tc, ' '.join(map(str, q))))
