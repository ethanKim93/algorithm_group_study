import sys
sys.stdin = open('sample_input.txt')

def dijkstra(s):
    global dist
    visited = [0] * (N+1)       # 도로번호만큼 방문 배열 생성
    visited[s] = 1      # 시작지점 방문 표시
    dist = [0] * (N+1)      # 거리 표시할 배열 생성
    for i in range(N+1):
        dist[i] = arr[s][i]     # 시작지점부터 i까지의 거리로 dist배열 초기화
    for _ in range(N+1):
        minV = INF
        v = 0
        for k in range(N+1):        # 방문하지 않았으면서, 구간거리가 최소인 값 찾기
            if visited[k] == 0 and minV > arr[s][k] :
                minV = arr[s][k]
                v = k
        visited[v] = 1      # 선택한 해당 도로번호 방문 표시
        # 시작점부터 v까지 이동하는 최소 거리는 찾았으므로, v부터 각 도로 번호까지의 최소거리를 찾아야함
        for m in range(N+1):
            dist[m] = min(dist[m], dist[v]+arr[v][m])   # 시작부터 m까지 가는게 더 짧은지, 시작점에서 v에서 m으로 거쳐가는게 더 짧은지 갱신

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    INF = 20        # 구간거리 최대값은 10이므로 적당히 20으로 설정
    arr = [[INF] * (N+1) for _ in range(N+1)]   # 가중치 배열 arr 초기화
    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s][e] = w
    # 이렇게 되면 인접한 구간에만 구간거리가 갱신됨
    dijkstra(0)
    print('#{} {}'.format(tc,dist[N]))


