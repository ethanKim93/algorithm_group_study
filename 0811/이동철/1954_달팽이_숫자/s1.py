import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    # row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 초기 위치 & 회전방향 설정
    row, col = 0, 0
    # 0:우, 1:하, 2:좌, 3:상
    rc_plus = 0

    for i in range(1, N*N + 1):
        snail[row][col] = i
        row += dr[rc_plus]
        col += dc[rc_plus]

        if row < 0 or col < 0 or row >= N or col >= N or snail[row][col] != 0:
            # 인덱스를 다시 원위치
            row -= dr[rc_plus]
            col -= dc[rc_plus]
            # 0, 1, 2, 3 접근을 위해 나머지로 수행
            rc_plus = (rc_plus + 1) % 4
            # 방향 바뀌고 다시 증가
            row += dr[rc_plus]
            col += dc[rc_plus]

    print('#{}'.format(tc))
    for j in snail:
        print(*j)
    print()
