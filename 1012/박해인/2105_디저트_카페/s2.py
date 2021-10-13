## 다시해보기
import sys
sys.stdin = open('sample_input.txt')

DI = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

def search(curY, curX, curD, k):
    global maxV

    # 만약 왔던 길을 또 가면?
    for i in range(1, k-1):
        if res[i][2] == data[curY][curX]:
            return

    # 좌상의 방향이면서 원 경로로 돌아왔으면
    if curD == 3 and curX == res[0][0] and curY == res[0][1]:
        if k > maxV:
            maxV = k
        return

    # 방향유지
    dy, dx = DI[curD]
    if 0 <= curY + dy < N and 0 <= curX+dx < N:
        res[k] = (curX, curY, data[curY][curX])
        search(curY+dy, curX+dx, curD, k+1)

    # 방향전환
    if curD < 3:
        dy, dx = DI[curD+1]
        if 0 <= curY + dy < N and 0 <= curX+dx < N:
            res[k] = (curX, curY, data[curY][curX])
            search(curY, curX, curD+1, k+1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    res = [(-1, -1, -1)] * (N*N)  # 좌표
    maxV = 0
    for i in range(N):
        for j in range(N):
            res[0] = (j, i, data[i][j])
            search(j, i, 0, 1)

    print('#{} {}'.format(test_case, maxV))