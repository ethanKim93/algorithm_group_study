import sys
sys.stdin = open("input.txt")

def DFS(i, x, cnt, k):
    global ans

    if cnt > ans: # 현재까지의 높이가 지금까지의 최고 높이보다 크다면 변경
        ans = cnt

    for y in range(4): # 들어온 좌표로부터 상하좌우 탐색
        nr = i + dirs[y][0]
        nc = x + dirs[y][1]
        if 0 <= nr < n and 0 <= nc < n: # 좌표 안에 있다면
            if maps[nr][nc] < maps[i][x] and temps[nr][nc] == "NO": # 현재 높이보다 낮고, 방문하지 않았다면
                temps[nr][nc] = "YES" # 방문 체크
                DFS(nr, nc, cnt + 1, k) # 다음 높이로 이동
                temps[nr][nc] = "NO" # 방문 해제

            elif maps[nr][nc] - k < maps[i][x] and temps[nr][nc] == "NO": # 최대값 k만큼 공사를 했을 때 현재점보다 낮아지고, 방문하지 않았다면
                temps[nr][nc] = "YES" # 방문 체크
                temp = maps[nr][nc] # 재귀를 빠져나왔을 때 되돌려줄 원래 높이의 값을 temp에 저장
                maps[nr][nc] = maps[i][x]-1 # 현재점보다 -1 만큼만 공사
                DFS(nr, nc, cnt + 1, k - k) # k를 사용할 수 없도록 0으로 만들기
                maps[nr][nc] = temp # 탐색이 끝나고 되돌아올때, 원래 높이로 되돌려주기
                temps[nr][nc] = "NO" # 방문 해제

t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    temps = [["NO"] * (n+1) for _ in range(n+1)] # 방문 체크 리스트 {"NO":미방문}
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 0 # 최종 답
    top = [] # 가장 높은 산의 위치 리스트
    now_top = 0 # 가장 높은 산의 높이

    # 가장 높은 산의 높이 찾기
    for i in range(n):
        now_top = max(now_top, max(maps[i]))

    # 가장 높은 산을 top 리스트에 담아주기
    for i in range(n):
        for x in range(n):
            if maps[i][x] == now_top:
                top.append([i,x])

    # 가장 높은 산들로부터 출발
    for i, x in top:
        temps[i][x] = "YES" # 출발점 방문 체크
        DFS(i, x, 0, k)
        temps[i][x] = "NO" # 출발점 방문 해제

    print("#{} {}".format(tc, ans+1))