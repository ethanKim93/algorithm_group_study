import sys
sys.stdin = open('input.txt')

def dijkstra(arr):
    INF = 987654321
    dist = [0]+[INF]*N
    visit = [0]*(N+1)
    dist[X] = 0
    for i in range(N+1):
        minV = INF
        min_Vertex = -1
        for j in range(N+1):
            if not visit[j] and minV>dist[j]:
                minV = dist[j]
                min_Vertex = j
        visit[min_Vertex] = 1

        for j in range(N+1):
            if not visit[j] and arr[min_Vertex][j] != 0 and arr[min_Vertex][j]+dist[min_Vertex]<dist[j]:
                dist[j] = arr[min_Vertex][j]+dist[min_Vertex]
    return dist

T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    arr1 = [[0] * (N + 1) for _ in range(N + 1)]
    arr2 = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr1[x][y] = c
        arr2[y][x] = c
    dist1 = dijkstra(arr1)
    dist2 = dijkstra(arr2)
    answer = 0
    for i in range(N+1):
        if answer<dist1[i]+dist2[i]:
            answer = dist1[i]+dist2[i]
    print('#{} {}'.format(tc,answer))

