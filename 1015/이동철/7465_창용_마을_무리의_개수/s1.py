import sys
sys.stdin = open('s_input.txt', 'r')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)
    # print(relation)

    visited = [0] * (N + 1)
    visited[0] = 1
    queue = deque()
    cnt = 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            cnt += 1
            queue.append(i)
            visited[i] = 1
        while queue:
            idx = queue.popleft()
            for j in relation[idx]:
                if visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1

    print('#{} {}'.format(tc, cnt))


def findset(x):                 # findset 연산, x가 속한 무리의 대표를 반환
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):                # union 연산, y를 x의 무리에 묶기
    p[findset(y)] = findset(x)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N : 사람수(1~N) M : pair 수
    p = [i for i in range(N + 1)]  # MakeSet, 마을사람 각각을 무리로 만들기

    for _ in range(M):
        x, y = map(int, input().split())    # 관계정보 입력 받고
        union(x, y)                         # 두 사람 무리짓기

    for i in range(1, N + 1):
        if i != p[i]:                       # 본인이 무리의 대표가 아니라면
            p[i] = findset(p[i])            # 같은 무리의 사람들은 대표번호로 통일

    answer = len(set(p[1:]))                # 1번사람부터 시작하므로 1~N번 무리를 중복 제거 후 무리의 개수 세기
    print('#{} {}'.format(tc, answer))