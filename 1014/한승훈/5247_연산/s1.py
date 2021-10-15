import sys
sys.stdin = open('sample_input.txt')

from collections import deque
import time

start = time.time()
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque()  # 계산할 숫자, 카운트
    queue.append((N, 0))
    visited = set()
    while queue:
        n, cnt = queue.popleft()
        if n == M:
            print('#{} {}'.format(tc, cnt))
            break
        for j in [n+1, n-1, n*2, n-10]:  # 4가지 연산
            if 1 <= j <= 1000000 and j not in visited:  # 조건
                queue.append((j, cnt+1))
                visited.add(j)

print("time :", time.time() - start)  # 0.0009999275207519531



