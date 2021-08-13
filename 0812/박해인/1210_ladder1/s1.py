# x : 95에서부터 오류나는데 왜인지 모르겠습니다 :)..............

import sys
sys.stdin = open('input.txt')

# 델타
dx = [-1, 0, 0]  # 상, 우, 좌
dy = [0, 1, -1]

# end -> start로 올라가기
T = int(input())
for test_case in range(1, T+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = ladder[99].index(2)  # 종착점
    x = 99  # 바닥부터 시작하기 위해 x = 99로 설정
    dir = 0  # direction 방향 표시, 초기화

    while x != 0:  # 맨 위에 도달할 때까지 반복
        if dir == 0:  # 위를 향할 때
            if y < 99 and ladder[x+dx[1]][y+dy[1]]: # 오른쪽 확인
                dir = 1  # 방향 전환
            elif y > 0 and ladder[x+dx[2]][y+dy[2]]: # 왼쪽 확인
                dir = 2  # 방향 전환
            else:  # 오른쪽 왼쪽 둘 다 갈 곳이 없다면, 직진
                x += dx[dir]
                y += dy[dir]

        elif dir == 1:  # 오른쪽을 향할 때
            if y < 99 and ladder[x+dx[dir]][y+dy[dir]]: # 오른쪽으로 갈 수 있으면,
                x += dx[dir]
                y += dx[dir]
            else:  # 못간다면 위로 이동
                dir = 0
                x += dx[dir]
                y += dx[dir]
        else:  # 왼쪽을 향할 때
            if y > 0 and ladder[x+dx[dir]][y+dy[dir]]: # 왼쪽으로 갈 수 있으면,
                x += dx[dir]
                y += dx[dir]
            else:
                dir = 0
                x += dx[dir]
                y += dx[dir]

        if x == 0:  # 위에 다 도달했다면
            break

    print('#{} {}'.format(test_case, y))
