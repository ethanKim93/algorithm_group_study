import sys
sys.stdin = open('input.txt')

def work_success(i, tmp):
    global N, percent

    if tmp <= percent:
        return

    if assigned == [1]*N:
        if tmp > percent:
            percent = tmp
            return

    for j in range(N):
        if assigned[j] == 0:
            assigned[j] = 1
            work_success(i + 1, tmp*(work[i][j]/100))
            assigned[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    percent = 0
    assigned = [0]*N
    work_success(0, 100)
    print('#{} {:6f}'.format(tc, percent))

