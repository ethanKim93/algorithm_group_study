import sys
sys.stdin = open('sample_input.txt')


def start_point(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
                return si, sj


def move(si ,sj, visited):
    global ans
    while not ans:
        vi = si
        vj = sj
        visited.append((si, sj))
        for idx in range(4):
            wi = vi + di[idx]
            wj = vj + dj[idx]
            if 0 <= wi < N and 0 <= wj < N and (wi, wj) not in visited and maze[wi][wj] == 3:
                ans = True
                return
            elif 0 <= wi < N and 0 <= wj < N and (wi, wj) not in visited and maze[wi][wj] == 0:
                move(wi, wj, visited)
        return
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # 숫자들이 붙어있을 때
    # maze = [list(map(int, input().split())) for _ in range(N)]  # 숫자 사이에 공백 있을 때

    # 출발점 찾기
    si, sj = start_point(maze, N)

    di = [0, 1, 0, -1] # 우하좌상
    dj = [1, 0, -1, 0]
    visited = []
    ans = False
    move(si, sj, visited)
    if ans:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
