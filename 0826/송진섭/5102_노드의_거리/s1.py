# 인접리스트로 해결
import sys
sys.stdin = open('sample_input.txt')


def bfs(start, goal):
    visited = [0] * (V+1)
    q = [start]
    visited[start] = 1
    while q:
        t = q.pop(0)
        for i in adj_list[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
            if goal == i:
                return visited[t]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    start, goal = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]  # 인접 리스트 생성
    for i in edge:
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    for i in range(len(adj_list)):  # 빈 리스트는 0 추가
        if not adj_list[i]:
            adj_list[i].append(0)
    # print(adj_list)
    ans = bfs(start, goal)
    print('#{} {}'.format(tc, ans))
