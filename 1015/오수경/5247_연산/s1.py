# 첨에 dfs 재귀로 했을 때는 Runtime Error -> bfs로 deque 사용하자!
import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def make_M(N, cnt):
    global M, ans, max_ans
    visited[N] = 1
    way = deque()
    way.append([N, cnt])

    while way:
        now = way.popleft()
        N, cnt = now[0], now[1]

        if N == M:
            if ans > cnt:
                ans = cnt
            return

        else:
            for k in (N+1, N-1, 2*N, N-10):
                if 0 < k <= 2*M and k <= 1000000:
                    if visited[k] == 0 and cnt < max_ans:
                        visited[k] = cnt +1
                        way.append([k, cnt+1])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_ans = M-N   # +1 연산으로만 도달할 때 cnt
    ans = 987654321
    visited = [0]*((2*M)+1)
    make_M(N, 0)
    print('#{} {}'.format(tc, ans))
