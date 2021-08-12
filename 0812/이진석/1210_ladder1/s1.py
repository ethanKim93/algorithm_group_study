# 2(도착점) 에 도착하는 출발점의 좌표.
import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladder = []
    flag = 0  # 0일때 상(탐색) 1일때 좌 2일때 우
    now_i = 0
    now_j = 0
    di = [-1, 0, 0]  # 상 좌 우
    dj = [0, -1, 1]
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    for j in range(100):
        if ladder[99][j] == 2:
            now_i = 99
            now_j = j
            break
    i = 99
    j = now_j
    while i > 0:
        if flag == 0:  # 탐색
            for k in [1, 2, 0]:  # 좌, 우, 상 순서
                now_i = i + di[k]
                now_j = j + dj[k]
                if 0 <= now_i <= 99 and 0 <= now_j <= 99 and ladder[now_i][now_j]:
                    j = now_j
                    i = now_i
                    flag = k
                    break
                else:
                    continue

        elif flag == 1:  # 왼쪽가는중
            for k in [0, 1]:
                now_i = i + di[k]
                now_j = j + dj[k]
                if 0 <= now_i <= 99 and 0 <= now_j <= 99 and ladder[now_i][now_j]:
                    j = now_j
                    i = now_i
                    flag = k
                    break
                else:
                    continue
        else:  # 오른쪽 가는중
            for k in [0, 2]:
                now_i = i + di[k]
                now_j = j + dj[k]
                if 0 <= now_i <= 99 and 0 <= now_j <= 99 and ladder[now_i][now_j]:
                    j = now_j
                    i = now_i
                    flag = k
                    break
                else:
                    continue
        answer = j
    print('#{} {}'.format(N, answer))
