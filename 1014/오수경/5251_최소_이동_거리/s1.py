import sys
sys.stdin = open('sample_input.txt')

def dijkstra():
    for _ in range(V):  # 초기 정점(0번) 제외 모든 정점 -> V-1 번 반복

        # s -> through_idx(최솟값) -> e
        # 최소 정점 찾기
        min_idx = -1
        min_value = 99999

        for i in range(V+1):
            if U[i] == 0 and D[i] < min_value:
                min_idx = i
                min_value = D[i]            # for 돌면서 최솟값 찾아냄
            U[min_idx] = 1                  # 맨 초기값 -> 0 부터 시작

            for j in range(V+1):             # 방문하기로 결정한 정점과 인접노드의 최솟값 갱신!
                if A[min_idx][j] != 999999:  # 인접 노드 중에서
                    if D[j] > D[min_idx] + A[min_idx][j]:
                        D[j] = D[min_idx] + A[min_idx][j]   # 최솟값 갱신

    return D[V]     # 최종 방문해서 최소로 갱신한 값



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    U = [0]*(V+1)   # 사용된 정점
    A = [[999999]*(V+1) for _ in range(V+1)]  # 가중치 초기화

    D = [999999] * (V + 1)       # 비용(거리) 초기화
    D[0] = 0                     # 시작 정점 지점 (0번 -> 0번의 거리는 0)

    for _ in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w

    print('#{} {}'.format(tc, dijkstra()))
