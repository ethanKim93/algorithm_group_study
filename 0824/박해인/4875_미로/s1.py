import sys
sys.stdin = open('sample_input.txt')


# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def where_to_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발 점 찾기
                ni = i
                nj = j
            return ni, nj


def DFS(maze):
    # 출발 지점 stack
    stack = [where_to_start(N, maze)]

    print(stack)
    # while stack:
    #     i = stack[][]
    #     j = stack[][]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 미로의 크기 N
    maze = [list(map(int, input().split())) for _ in range(N)]
    # 0 통로 # 1 벽 # 2 출발 # 3 도착

    DFS(maze)

