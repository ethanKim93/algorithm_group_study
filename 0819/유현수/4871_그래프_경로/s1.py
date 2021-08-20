import sys
sys.stdin = open('input.txt')


def dfs(s, g, V):       # 시작 정점, 목표 정점, 정점 개수
    stack = []
    visited = [0]*(V+1)
    i = s
    visited[i] = 1
    while i:
        for w in range(1, V+1):
            if ad[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                if i == g:
                    return 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    ad = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        ad[n1][n2] = 1                      # 방향 그래프이므로 n1 -> n2만 입력
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G, V)))
