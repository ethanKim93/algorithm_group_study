# 처음에 DFS로 풀다가 1만 계속더하다보니까 재귀깊이error 떠서 BFS로 변경
import sys
from collections import deque

sys.stdin = open('sample_input.txt')


def BFS(number, target):  # BFS
    global min_cnt
    q = deque()
    q.append((number, 0))  # 최초 enQ
    while q:
        # deQ
        now = q.popleft()
        num, cnt = now[0], now[1]

        if num == target:  # 타겟숫자인지 확인
            if min_cnt > cnt:  # BFS이기 때문에 처음 등장하는 타겟숫자라면 항상 최소 카운트를 가지고있으므로
                min_cnt = cnt  # 최소카운트 갱신후 종료
                return

        if counts[num]:  # 이미 사용한 숫자라면 다른 연산을 하더라도 최소 연산횟수보다 많으므로 continue (가지치기)
            continue
        else:
            counts[num] = 1  # 사용 체크
            # 모든 연산결과는 자연수, 100만이하. 유효성 검증 후 enQ
            if 0 < num + 1 <= 1000000:
                q.append((num + 1, cnt + 1))
            if 0 < num - 1 <= 1000000:
                q.append((num - 1, cnt + 1))
            if 0 < num * 2 <= 1000000:
                q.append((num * 2, cnt + 1))
            if 0 < num - 10 <= 1000000:
                q.append((num - 10, cnt + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    min_cnt = 1000000       # 1씩 더하더라도 100만번은 넘지 않는다
    counts = [0] * 1000001  # 한 숫자를 중복검증 하지 않기 위한 배열(1~1000000)
    BFS(N, M)
    print('#{} {}'.format(tc, min_cnt))
