# -*- coding: utf-8 -*-

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(row, col):
    global start_pos, max_value, visited

    # bfs를 위한 선형 큐 작성
    front = -1
    rear = 0
    queue = [0] * (N * N)
    queue[rear] = [row, col]
    visited[row][col] = 1

    # 현재 케이스에서 경우에서 열 수 있는 방문의 시작점과 최대로 열 수 있는
    # temp_pos와 temp_value를 정의
    temp_pos = maps[row][col]
    temp_value = 1

    while front < rear:
        
        # 선형 큐에 대한 pop 연산
        front += 1
        temp_row, temp_col = queue[front]
        
        # 이동할 수 있는 경우에 대해 탐색
        for direction in directions:
            new_row = temp_row + direction[0]
            new_col = temp_col + direction[1]
            
            # 이동할 수 있는지 조건 판단
            if 0 <= new_row < N and 0 <= new_col < N:
                # 원소의 차의 절댓값과 방문 여부에 대한 조건 판단
                if abs(maps[new_row][new_col] - maps[temp_row][temp_col]) == 1 and not visited[new_row][new_col]:
                    # 방문 하는 경우, 방문 할 경우의 방 번호가 기존에 정의된 번호보다 작으면 업데이트를 한다
                    if temp_pos > maps[new_row][new_col]:
                        temp_pos = maps[new_row][new_col]

                    # 열 수 있는 방 갯수를 업데이트하고, 방문 여부를 업데이트 한다.
                    temp_value += 1
                    visited[new_row][new_col] = 1

                    # 큐에 대한 삽입 연산을 진행한다.
                    rear += 1
                    queue[rear] = [new_row, new_col]

    # 이번 탐색에서 정해진 방문을 열 수 있는 최대의 값과 열 수 있는 방의 번호를 업데이트 한다
    if max_value == temp_value:
        if temp_pos < start_pos:
            start_pos = temp_pos
    if max_value < temp_value:
        start_pos = temp_pos
        max_value = temp_value
    return


T = int(input())
for tc in range(1, T + 1):

    N = int(input())

    # 행렬에 대한 정보를 담는 maps 변수 선언
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 행렬의 방문과 관련된 정보를 담는 visited 변수 선언
    visited = [[0 for _ in range(N)] for __ in range(N)]

    # 최대로 방을 이동할 수 있는 방의 번호 start_pos 선언
    start_pos = 0
    
    # 최대 몇 개의 방을 이동할 수 있는지를 나타내는 max_value 선언
    max_value = 0

    # 모든 방문 안한 상태의 행렬 데이터에 대해 탐색 실시
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                bfs(row, col)
    
    print("#{} {} {}".format(tc, start_pos, max_value))
    