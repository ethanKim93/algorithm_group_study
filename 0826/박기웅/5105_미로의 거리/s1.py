import sys
sys.stdin = open("sample_input.txt")

#dfs 재귀 호출을 통해 가능한 경로 중 최소 경로 비교
def dfs(S, cnt):                                # S: 출발점, cnt: 이동 거리
    global min_dist
    stack.append(S)                             # 출발점 push
    while stack:
        i, j = stack.pop()                      # 하나 빼고 방문 기록
        visited[i][j] = 1

        if miro[i][j] == '3':                   # 도착지인 경우 최소값과 비교 후 갱신
            if min_dist > cnt:
                min_dist = cnt
            return                              # 도착한 경우 재귀 탈출

        for k in range(4):                      # 4방향 검사
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:     # 방문하지 않은 곳 중 갈 곳이 있으면
                if miro[ni][nj] == '0' or miro[ni][nj] == '3':          # 0 아니면 3 중에서
                    dfs([ni, nj], cnt+1)                                # 그곳으로 출발점 초기화
    return                                                              # 아예 길이 없다면 재귀 탈출

for tc in range(1, int(input())+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):                                                  # 출발점 찾기
        for j in range(N):
            if miro[i][j] == '2':
                S = [i, j]
                break
    stack = []
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]
    visited = [[0]*(N+1) for _ in range(N+1)]  # 방문기록 초기화
    min_dist = N**3                            # 경로 초기화 될 수 없는 큰 값으로
    dfs(S, 0)                                  # 이동거리 0으로 dfs 호출
    print('#{} {}'.format(tc, min_dist-1 if min_dist != N**3 else 0))



