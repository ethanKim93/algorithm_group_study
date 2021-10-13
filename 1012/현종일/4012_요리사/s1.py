import sys
sys.stdin = open("sample_input.txt")

def comb(n, r, idx):
    if r <= 0:
        global answer
        f1 = 0
        f2 = 0
        for j in range(N):
            for k in range(N):
                if food[j] == food[k] and food[j] == 1:
                    f1 += ingredients[j][k]
                elif food[j] == food[k] and food[j] == 0:
                    f2 += ingredients[j][k]

        tmp = abs(f1 - f2)
        if answer > tmp:
            answer = tmp
        return

    for i in range(idx + 1, n):
        if food[i] == 0:
            food[i] = 1
            comb(n, r-1, i)
            food[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    food = [0] * N
    answer = 987654321
    comb(N, N//2, 0)

    print('#{} {}'.format(tc, answer))