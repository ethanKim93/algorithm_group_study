import sys
sys.stdin = open("input.txt")

def change_dir(idx, idy, cnt):
    global status, number

    # Dir check & change
    if status == 3:
        status = 0
    else:
        status += 1

    # 바뀐 dir로 체크
    nr = idx + dirs[status][0]
    nc = idy + dirs[status][1]

    if 0 <= nr < n and 0 <= nc < n:
        if not maps[nr][nc]:
            number += 1
            maps[nr][nc] = number
            snail_go(nr, nc, cnt + 1) # 계속해서 재귀

def snail_go(idx, idy, cnt):
    global number, maps, status

    if cnt == n**2: # 없어도 되지만 명시적으로
        return

    nr = idx + dirs[status][0]
    nc = idy + dirs[status][1]

    if 0 <= nr < n and 0 <= nc < n:
        # 갈 수 있는 자리로 기존 방향으로 이동
        if maps[nr][nc] == 0:
            number += 1
            maps[nr][nc] = number
            snail_go(nr, nc, cnt+1)

        # 이미 지나온 자리면, 방향 변경
        else:
            change_dir(idx, idy, cnt)

    # Map안에 있는 좌표가 아니면, 방향 변경
    else:
        change_dir(idx, idy, cnt)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    maps = [[0]*n for _ in range(n)]
    dirs = [(0,1), (1,0), (0,-1), (-1,0)] # Dir 우하좌상 순
    status = 0
    number = 0
    snail_go(0, -1, 0) # 좌상단 -1열에서 출발

    # Print
    print("#" + str(tc))
    for i in range(n):
        for x in range(n):
            print(maps[i][x], end=" ")
        print()