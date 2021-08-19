# V노드 E간선
# DFS 구현시 stack을 이용하는 방법 recursion을 이용하는 방법존재
# G=(V,E) V->vertex,  V노드 / set E->edge set, E간선/ degree 분지수
# 경로(path) : a-> b-> a-> c 다시 되돌아가면 경로 X
# 사이클(cycle) : 두 노드를 연결하는 경로가 회전. 경로가 유일하지않음..

# 무방향 그래프를 표현하는 방법 -> 인접성을 표현
# 1. 인접 행렬 -> 노드 * 노드의 2차원 배열 (대칭구조) -> 가시적 구조
#    단점 : 메모리의 낭비
# 2. 인접 리스트 (연결리스트) -> 존재하는 엣지만 표현가능

import sys

sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]  #
    for _ in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    stack = [S]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            for v in adj[vertex]:
                if not visited[v]:
                    stack.append(v)

    result = 1 if visited[G] else 0
    print('#{} {}'.format(tc, result))
