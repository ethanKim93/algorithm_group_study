import sys
sys.stdin = open('input.txt', 'r')


# 1. D4 | DFS
# 2. 선택한 숫자와 +1, -1로 연결될 수 있는 구간을 찾는 방법을 사용
# 3. 처음 숫자를 선택하고 그 숫자보다 값이 1이 큰 숫자를 계속 찾는다
# 4. 그 숫자보다 값이 1이 작은 숫자도 계속 찾는다.
# 5. 찾은 작은 숫자 ~ 큰 숫자의 범위가 하나의 구간이 된다.
# 6. 값을 다른 숫자(ex. -10)으로 바꿔줘서 하나의 구간을 여러번 탐색하지 않게 한다.
# 7. 모든 구간들을 구하고 구간의 길이가 가장 긴 구간을 선택. 구간이 여러개라면
#    시작점이 가장 작은 숫자를 선택한다.
# (cnt_list 는 시작점을 인덱스로 하고 값을 구간의 길이로 하는 리스트이다)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    cnt_list = [0] * (N ** 2 + 1)

    for i in range(N):
        for j in range(N):
            if rooms[i][j] > 0:
                low_stack = [(i, j)]
                low_num = rooms[i][j]

                high_num = rooms[i][j]
                high_stack = [(i, j)]

                rooms[i][j] = -10
                # 큰 숫자 찾기
                while high_stack:
                    x, y = high_stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if rooms[nx][ny] == high_num + 1:
                                high_stack.append((nx, ny))
                                high_num += 1
                                rooms[nx][ny] = -10
                                break
                # 작은 숫자 찾기
                while low_stack:
                    x, y = low_stack.pop()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if rooms[nx][ny] == low_num - 1:
                                low_stack.append((nx, ny))
                                low_num -= 1
                                rooms[nx][ny] = -10
                                break

                    cnt_list[low_num] = high_num - low_num + 1

    max_cnt = max(cnt_list)
    max_cnt_idx = cnt_list.index(max_cnt)
    print('#{} {} {}'.format(tc, max_cnt_idx, max_cnt))