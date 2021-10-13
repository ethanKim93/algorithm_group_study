import sys
sys.studin = open('input.txt','r')

def combi(n, r, idx):
    if r <= 0:
        global ans
        food1 = 0
        food2 = 0
        for j in range(N):
            for k in range(N):
                if food[j] == food[k] and food[j] == 1:
                    food1 += synergy_info[j][k]
                elif food[j] == food[k] and food[j] == 0:
                    food2 += synergy_info[j][k]

        diff = abs(food1 - food2)
        if ans > diff:
            ans = diff
        return

    for i in range(idx + 1, n):
        if food[i] == 0:
            food[i] = 1
            combi(n, r-1, i)
            food[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy_info = [list(map(int, input().split())) for _ in range(N)]
    food = [0] * N
    ans = 999999999999
    combi(N, N//2, 0)
    print('#{} {}'.format(tc, ans))