import sys
sys.stdin = open('sample_input.txt')
def check():

    di = [0, 1, 0, -1]  # 우 하 좌 상
    dj = [1, 0, -1, 0]

    while stack:            # 더이상 갈곳이 없다면 종료 (스택이 비어있으면)
        now = stack.pop()   # 스택에서 pop 해서 현재위치를 설정 (갈 수 있는길 확인 후 돌아온경우)
        i = now[0]
        j = now[1]
        for k in range(4):  # 델타를 이용해서 이동할수 있는 길이 있는지 확인
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                if maze[ni][nj] == 3:   # 도착지점에 도착하면 1(True)을 Return
                    return 1
                maze[ni][nj] = 1    # 이미 점검한 길을 다시 점검하지 않도록 1로 변경
                stack.append([ni,nj])   # 스택에 지나온 길을 저장
    return 0
for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int,list(input()))) for _ in range(N)] # 미로 배열
    start = []      # 시작지점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]

    stack= [start] # 방문 경로를 스택에 저장하기 때문에 시작지점을 저장후 함수 실행행
    print('#{} {}'.format(tc, check()))