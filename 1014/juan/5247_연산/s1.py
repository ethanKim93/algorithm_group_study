import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def BFS():
    q = deque([N])
    while q:
        now = q.popleft()
        if now == M:                                    # now가 M과 같으면 현재까지의 연산횟수 반환
            return visited[now]
        for num in (now+1, now-1, now*2, now-10):       # now에 4가지 연산을 한 결과들을 순회
            if 0 < num <= 2*M and not visited[num]:     # 연산 결과값이 M의 2배를 넘지 않고(M보다 큰 수를 2배 연산할 필요가 없기 때문에), 확인한 적이 없는 숫자라면
                q.append(num)                           # 큐에 추가
                visited[num] = visited[now] + 1         # 연산 횟수 1증가 후 할당


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (2*M+1)
    print('#{} {}'.format(tc, BFS()))