import sys
sys.stdin = open('input.txt')


def backtracking(idx, totalP):
    global maxP
    if idx == N:
        if totalP > maxP:
            maxP = totalP
            return

    if totalP <= maxP:
        return
    else:
        for i in range(N):
            if not done[i]:
                done[i] = 1
                backtracking(idx+1, totalP * success[idx][i]/100)
                done[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    success = [list(map(int, input().split())) for _ in range(N)]
    done = [0] * N
    maxP = 0
    backtracking(0, 1)
    print('#{} {:.6f}'.format(tc, maxP * 100))