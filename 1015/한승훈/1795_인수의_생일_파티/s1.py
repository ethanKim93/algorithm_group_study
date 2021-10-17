import sys
sys.stdin = open('input.txt')
from collections import deque

def diikstra(start, lst):
    key = [inf] * (N+1)
    key[start] = 0
    queue = deque(([start]))
    while queue:
        t = queue.popleft()
        for h, c in lst[t]:
            if key[t] + c < key[h]:
                key[h] = key[t] + c
                queue.append(h)
    return key


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    go = [[] for _ in range(N+1)]
    back = [[] for _ in range(N+1)]
    inf = 987654321
    for _ in range(M):
        x, y, c = map(int, input().split())
        back[x].append((y, c))
        go[y].append((x, c))
    max_cnt = 0
    for i in range(1, N+1):
        if max_cnt < diikstra(X, go)[i] + diikstra(X, back)[i]:
            max_cnt = diikstra(X, go)[i] + diikstra(X, back)[i]
    print('#{} {}'.format(tc, max_cnt))