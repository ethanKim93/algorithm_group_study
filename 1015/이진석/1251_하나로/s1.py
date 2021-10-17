import sys

sys.stdin = open('input.txt')

def prim(start):                # 모든 섬들을 최소비용으로 연결시키기만 하면되기 때문에 prim 알고리즘 사용
    cost = [INF] * N            # 시작점부터 각 섬까지의 최소 환경부담금
    cost[start] = 0
    visited = [0] * N           # 최소신장트리 포함여부

    for _ in range(N-1):
        min_idx = -1            # 최소값인덱스
        min_val = INF           # 최소값
        for i in range(N):
            if not visited[i] and min_val > cost[i]:    # 최소신장트리에 포함안되는 최소값을 찾았을때 최소값 갱신
                min_idx = i
                min_val = cost[i]
        visited[min_idx] = 1    # 최소값인덱스 포함표시

        for i in range(N):
            # 최소신장트리에 포함 안된 섬일때 최소비용을 찾았다면 최소비용 갱신
            if not visited[i] and cost[i] > adj[min_idx][i]:
                cost[i] = adj[min_idx][i]
    return sum(cost)            # 각 섬까지의 최소비용 합 리턴

for tc in range(1, int(input()) + 1):
    N = int(input())
    islandx = list(map(int, input().split()))   # 각 섬의 x좌표
    islandy = list(map(int, input().split()))   # 각 섬의 y좌표
    E = float(input())                          # 환경부담세율
    INF = E*((10 ** 6)**2)                      # 이론상 최대값
    adj = [[INF] * N for _ in range(N)]         # 인접 섬까지의 환경부담금

    for i in range(N):                          # 각 섬에서부터 다른 섬 까지의 환경부담금 계산
        for j in range(N):
            if i != j:
                adj[i][j] = ((islandx[i] - islandx[j])**2 + (islandy[i] - islandy[j]) ** 2) * E
    print('#{} {}'.format(tc, round(prim(0))))  # 첫째자리 반올림해서 출력
