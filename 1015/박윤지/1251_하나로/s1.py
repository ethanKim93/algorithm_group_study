# MST(minimum spanning tree) -> Prim, Kruskal

import sys
sys.stdin = open('input1.txt')

def prim():
    # 1. 임의의 정점 선택 -> 1번
    selected 


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N: 섬 개수, X,Y: x,y 좌표
    xli = list(map(int, input().split()))
    yli = list(map(int, input().split()))
    island = [0] * (N+1)  # 1번부터 섬 좌표
    for i in range(1, N+1):
        island[i] = (xli[i-1], yli[i-1])
    E = float(input())  # 환경부담세율

    # 모든 섬들 사이 거리의 제곱을 저장하는 배열 (E는 맨 나중에 곱하면 돼서 포함x)
    adj = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            temp = (island[i][0] - island[j][0]) ** 2 + (island[i][1] - island[j][1]) ** 2
            adj[i][j] = temp
            adj[j][i] = temp

    # Prim으로 풀어본다...


