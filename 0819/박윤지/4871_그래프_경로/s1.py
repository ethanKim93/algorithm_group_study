import sys
sys.stdin = open('sample_input.txt')

def dfs(S, G, V):
    visited = [0] * (V+1)
    stack = []
    i = S
    visited[i] = 1
    while i != 0:
        for w in range(1, V+1):
            if board[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
    if visited[G] == 1:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 노드 배열(행-출발, 열-도착) 만들기
    board = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        board[a][b] = 1

    S, G = map(int, input().split())
    print('#{} {}'.format(tc, dfs(S, G, V)))