import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque


def check(cal):
    if cal > 1000000 or cal < 0:
        # 1보다크고 1,000,000보다 작아야 하므로
        # 계산해서 넘기기전에 범위에 들어가있는지 체크
        return True


def bfs(N, M):
    queue = deque()
    # list 는 O(n) deque 는 O(1)
    queue.append((N, 0))
    visited = {}
    while queue:
        num, cnt = queue.popleft()
        # 왼쪽 끝 요소를 가져오는 동시에 deque 에서 삭제한다.
        calculate = [num - 1, num + 1, num * 2, num - 10]
        if visited.get(num, 0):
            # 첫번째 인자에 해당 찾고 싶은 딕셔너리 key 값 입력하고,
            # 두번째 인자에는 첫번째 인자가 없을 경우 출력하고 싶은 값 입력.
            # 해당 수를 사용했다고 체크를 하는 변수를 이용해 가지치기
            continue
        visited[num] = 1
        if num == M:
            # 숫자가 같아지면 횟수 return
            return cnt
        cnt += 1
        for cal in calculate:
            if check(cal):
                continue
            queue.append((cal, cnt))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, bfs(N, M)))
