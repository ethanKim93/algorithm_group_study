import sys
sys.stdin = open('sample_input.txt')
'''
0은 통로
1은 벽
3은 도착
'''

def dfs():

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while stack:
        now = stack.pop()   # [4,3]
        r, c = now[0], now[1] # r = 4, c = 3
        maze[r][c] ='1'  # 내가 이미 지나간 곳은 벽으로 놓을거야 다시 안가
        for i in range(4):
            next_r, next_c = r+dr[i], c+dc[i]
            if 0 <= next_r < N and 0 <= next_c < N:  # 범위를 설정해 놓기!!!! 범위 안정해주면 인덱스 에러 나기 딱 좋음!
                if maze[next_r][next_c] == '0':
                    stack.append([next_r, next_c])
                elif maze[next_r][next_c] == '3':
                    return 1

    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    stack = []      # stack = [[4,3]]

    # 도착지에서 출발 (거꾸로 생각)

    for i in range(N):      # maze위치에서 순회하면서 2를 찾아주기
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i, j])    # [i,j] 좌표를 stack에 쌓아두기

    print('#{} {}'.format(tc,dfs()))


