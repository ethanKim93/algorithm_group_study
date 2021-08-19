import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def DFS(S, V, G):  # 출발노드 S,  V개 이내의 노드 V, G 도착노드
    stack = []  # 지나온 정점을 저장
    visited = [0] * (V+1)

    # 시작 정점은 반드시 방문한다.
    i = S

    visited[i] = 1
    while i:
        for w in range(1, V+1):
            if matrix[i][w] == 1 and visited[w] == 0: # 연결이 되어있고, 방문하지 않았다면




for test_case in range(1, T+1):
    V, E = map(int, input().split())  # V개 이내의 노드 , E개의 간선
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        matrix[n1][n2] = 1
        matrix[n1][n2] = 1

    S, G = map(int, input().split())  # 출발노드 S 도착노드 G






