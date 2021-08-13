import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    x = 99
    for i in range(100):
        # 도착지는 값이 2
        if matrix[99][i] == 2:
            # 도착지의 column 좌표를 저장
            y = i

    # delta 값
    d = [-1, 1]

    # 가장 윗부분에 도달하면 끝내자
    while x != 0:
        # 주위를 둘러보고 왼쪽이나 오른쪽으로 갈 길이 있으면 가자
        # 방향 델타로 이동
        for i in range(2):
            # 좌->우
            # 좌표 변경
            ny = y + d[i]

            # 새로운 위치로 옮겼을 때 그 위치가
            # matrix 범위 내에서 안에 포함되면서 이동가능한지 확인하고
            if 0 <= ny < 100 and matrix[x][ny]:
                # 현재 위치는 0으로 만들고(그래야 다음 탐색에서 1을 보고 가지 않음)
                matrix[x][y] = 0
                # 현재 위치 갱신 -> 움직여야 할 곳으로 이동
                y += d[i]
                break
        else:   # 양 옆에 길이 없으면 위로 이동
            x -= 1

    # 최종적으로 column값 출력
    print('#{} {}'.format(tc, y))