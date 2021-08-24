import sys
sys.stdin = open('sample_input.txt')


#1. 2차원 배열(visited) 생성 후 방문 체크하면서 이동
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def DFS(r, c):
    global result

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]                           # 다음 이동할 위치
        if 0 <= nr < N and 0 <= nc < N:                         # 이동할 위치가 미로 범위 안에 있는지 파악
            if data[nr][nc] == 3:                               # 만약 이동한 곳에서 도착지를 바로 만나면 result에 1 할당 후 함수 종료
                result = 1
                return
            if (not data[nr][nc]) and (not visited[nr][nc]):    # 이동한 위치가 통로(0) & 방문하지 않은 곳이라면
                visited[nr][nc] = 1                             # 방문 처리하고
                DFS(nr, nc)                                     # 이동한 위치에서 다시 탐색


T = int(input())
for tc in range(1, T+1):
    N = int(input())                                            # 미로 크기
    data = [list(map(int, list(input()))) for _ in range(N)]    # 미로(정수형으로 형변환)
    visited = [[0] * N for _ in range(N)]                       # 방문처리
    result = 0                                                  # 결과

    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                DFS(r, c)                                       # 출발지를 찾으면 그때의 좌표에서 DFS 탐색 시작
                break

    print('#{} {}'.format(tc, result))



#2. 미로 자체에 흔적남기며 이동

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def DFS():
    while stack:                                    # stack이 비워질때까지 반복
        r,c = stack.pop()                           # stack에 마지막으로 들어간 현재 위치의 행과 열 
        maze[r][c] = '1'                            # 미로에 '1'로 처리 후 이동
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]           # 이동할 위치의 좌표
            if 0 <= nr < N and 0 <= nc < N:         # 미로 범위 안에 있다면
                if maze[nr][nc] == '0':             # 미로에서 통로('0')인 경우 stack에 추가
                    stack.append([nr,nc])
                elif maze[nr][nc] == '3':           # 도착점('3')인 경우 return 1
                    return 1
    return 0                                        # stack이 비워졌음에도 함수가 종료되지 않았다면 return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    stack = []                                      # 현재 위치를 담을 stack 생성
    for i in range(N):                              # 미로 전체를 순회하며 출발점 찾아서 stack에 추가
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i,j])
    print('#{} {}'.format(tc, DFS()))               # DFS 함수 결과값을 formating해서 출력