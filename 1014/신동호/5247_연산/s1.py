import sys
sys.stdin = open('sample_input.txt')
# enqueue, dequeue 직접 구현시 시간 초과
# 1000000까지 범위 줄 시 시간 초과, 2*M

# def enqueue(s, v):
#     global front
#     front += 1
#     s[front] = v

# def dequeue(s):
#     global rear
#     rear += 1
#     return s[rear]

from collections import deque

def bfs(n, m):
    # global front, rear
    # q = [0] * 100000
    q = deque([n])
    # front += 1
    # enqueue(q, n)
    # q[front] = n
    while q:
        # v = dequeue(q)
        # rear += 1
        # v = q[rear]
        v = q.popleft()
        if v == m:
            return visited[v]
        for next in (v*2, v-10, v+1, v-1):
            if 0 < next <= 2 * M and not visited[next]:
                # enqueue(q, next)
                # front += 1
                # q[front] = next
                q.append(next)
                visited[next] = visited[v] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # front = rear = -1
    visited = [0] * (2 * M + 1)
    print('#{} {}'.format(tc, bfs(N, M)))
    