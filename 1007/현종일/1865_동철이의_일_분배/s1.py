import sys
sys.stdin = open("input.txt")

def select_worker(now):
    global result, percent

    if now > N:
        if percent > result:
            result = percent
        return

    if percent < result:
        return

    for i in range(1, N+1):
        if used[i] == 0:
            if success[now][i] == 0:
                continue
            else:
                percent *= (success[now][i]/100)
                used[i] = 1
                select_worker(now+1)
                percent /= (success[now][i] / 100)
                used[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    success = [[0]] + [[0]+list(map(int, input().split())) for _ in range(N)]
    used = [0] * (N+1)
    percent, result = 1, 0
    select_worker(1)

    print('#{} {:.6f}'.format(tc, round(result * 100, 6)))



