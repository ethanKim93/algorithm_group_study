import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    q = [[] for i in range(N)]
    for i in range(N):
        q[i] = [i+1, pizza[i]]

    a = 0
    while len(q) > 1:
        idx, cheese = q.pop(0)
        cheese //= 2
        if cheese:
            q.append([idx, cheese])
        else:
            if a < M-N:
                q.append([N+a+1, pizza[N+a]])
                a += 1
    print('#{} {}'.format(tc, q[0][0]))