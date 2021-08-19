import sys

sys.stdin = open('sample_input.txt')


def dfs(start, goal, v):
    visited[start] = 1                              # 시작지점 방문 기록
    now = start
    stack.append(now)                               # 시작지점 push
    while now:                                      # stack에 남아있는게 없을때 종료
        for i in range(1, v+1):                     # 각 노드를 순회하면서
            if graph[now][i] and not visited[i]:    # 방문하지 않은 연결된 노드 찾기
                now = i
                visited[now] = 1                    # 현재 노드 방문 기록
                stack.append(now)                   # 현재 노드 push
                if now == goal:                     # 목표 노드 도착시 종료 및 리턴
                    return 1
                break
        else:                                       # 인접 노드에서 방문 안한 노드가 없을 때
            if stack:                               # 스택내에 값이 존재하면 이전 노드로 이동
                now = stack.pop()
            else:                                   # 최초 노드까지 돌아가서 목표 노드 도착 실패시 종료
                now = 0
    return 0



for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        v, w = map(int, input().split())
        graph[v][w] = 1
    s, g = map(int, input().split())

    visited = [0] * (V + 1)
    stack = []
    print('#{} {}'.format(tc, dfs(s, g, V)))
