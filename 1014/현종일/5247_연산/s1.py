import sys
from collections import deque
sys.stdin = open("sample_input.txt")

def bfs(n, m):
    global min_cnt
    queue = deque()
    queue.append((n, 0))

    while queue:
        now, cnt = queue.popleft()
        if now == m:
            min_cnt = cnt
            return

        cnt += 1
        if not visited[now]:
            visited[now] = 1
            if 0 < now - 1 <= 1000000:
                queue.append((now - 1, cnt))
            if 0 < now + 1 <= 1000000:
                queue.append((now + 1, cnt))
            if 0 < now - 10 <= 1000000:
                queue.append((now - 10, cnt))
            if 0 < now * 2 <= 1000000:
                queue.append((now * 2, cnt))

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    min_cnt = 987654321
    visited = [0] * 1000000
    bfs(N, M)

    print("#{} {}".format(tc, min_cnt))

