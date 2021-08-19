import sys
sys.stdin = open("input.txt")

#dfs 정의
def dfs():
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:         # 방문을 안한 노드면
            visited[vertex] = 1         # 방문 도장 찍음
            for v in cnt[vertex]:       # 현재 정점에서 갈 수 있는 곳 반복
                if v == 99:             # 갈 수 있는 곳중 99 있으면 리턴 1하고 나감
                    return 1
                if not visited[v]:      # 갈 수 있는 곳 중 방문 안했으면
                    stack.append(v)     # 방문 경로 누적
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    N = list(map(int, input().split()))
    cnt = [[] for _ in range(100)]
    for i in range(0, len(N), 2):
        cnt[N[i]].append(N[i+1])

    #0 에서 99 갈 수 있는지 찾기
    stack = [0]                         # 방문 경로 스택
    visited = [0]*100                   # 방문여부

    print('#{} {}'.format(tc, dfs()))