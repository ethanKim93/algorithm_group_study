import sys
sys.stdin = open('input.txt')

T = int(input())


'''

2
1 0
3 2
1 2
3 2

'''


def DFS(num, value):
    global total
    visited[num] = 1
    if value > total:
        total = value
    for i in link[num]:
        if not visited[i]:
            DFS(i, value+1)
            visited[i] = 0


# 최장 경로상의 모든 정점 갯수를 출력하라고 하는것
for tc in range(1, T + 1):  # 경로의 길이가 정점의 갯수
    N, M = map(int, input().split())  # N개의 정점 M개의 간선
    link = [[] for _ in range(N + 1)]


    for _ in range(M):
        n1, n2 = map(int, input().split())
        link[n1].append(n2)
        link[n2].append(n1)
    total = 0

    for i in range(1,N+1):
        visited = [0] * (N + 1)
        DFS(i, 1)
    print('#{} {} '.format(tc, total))
