import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1 # 처음 방문
    for w in range(1, V):
        if matrix[v][w] == 1 and not visited[w]: # 길이 있으며 방문기록 없는 경우
            dfs(w)


for _ in range(1,11):
    V, G = 100, 99
    tc, E = map(int, input().split())
    E_lst = list(map(int, input().split()))
    matrix = [[0] * V for _ in range(V)]
    visited = [0] * V
    for i in range(0, len(E_lst)-1, 2):
        matrix[E_lst[i]][E_lst[i+1]] = 1  # matrix 내부에 경로 체크 & 일방통행 이므로 반대는 없다.
    dfs(0)
    print('#{} {}'.format(tc, visited[G]))


