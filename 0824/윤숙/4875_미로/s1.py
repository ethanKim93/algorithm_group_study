import sys

sys.stdin = open('input.txt','r')
T = int(input())


def DFS(sx, sy):
    # 상하좌우
    global flag
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
    #상하좌우 방향으로 0이 있는지 판단하며 벽이거나 3를 발견하지 못하면 다른방향으로 방향이 전환됨.
        if sx + dx[i] >= 0 and sy + dy[i] >= 0 and sx + dx[i] < N and sy + dy[i] < N: #범위를 넘어가지 않게 가이드 라인설정
            if miromap[sx + dx[i]][sy + dy[i]] == 0: #해당방향이 0이면
                miromap[sx+dx[i]][sy+dy[i]]=1 #지나온길을 miromap에 직접 찍음
                DFS(sx + dx[i], sy + dy[i]) # 자기자신을 호출하며 반복한다.
            if miromap[sx + dx[i]][sy + dy[i]] == 3: #해당방향이 3이면
                flag = 1 #3을 발견했다는 표시를 남기고 리턴!
                return




for tc in range(1, T + 1):
    N = int(input())
    miromap = [list(map(int, input())) for _ in range(N)]
    flag = 0
    sx = 0  # 시작의 좌표 행
    sy = 0  # 시작의 좌표 열
    for i in range(N):
        for j in range(N):
            if miromap[i][j] == 2: #시작좌표 찾기
                sx = i
                sy = j
                break
        if sx and sy: #좌표 찾았으면 나가기
            break

    DFS(sx, sy) #DFS함수  실행

    print('#{} {}'.format(tc, flag))
