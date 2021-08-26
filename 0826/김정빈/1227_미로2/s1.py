import sys
sys.stdin = open("input.txt")

def dfs(s):
    stack = []
    stack.append(s) #미리 붙여놓고
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while stack:
        r, c = stack.pop() #팝하여 사용
        maze[r][c] = 1 #미로 자체에 방문기록(맞나요...?)

        #상하좌우 순회할 반복문
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]

            if 0 <= nr < N and 0 <= nc < N: #범위제한
                if maze[nr][nc] == 0: #0이면 이동
                    stack.append([nr,nc]) #다음에 쓸 값 붙이기
                elif maze[nr][nc] == 3:
                    return 1
    return 0
N = 100
for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    stack = []

    #출발지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s = ([i,j])

    print('#{} {}'.format(tc, dfs(s)))

"""
#1 1
#2 1
#3 1
#4 0
#5 0
#6 1
#7 1
#8 0
#9 1
#10 0
"""