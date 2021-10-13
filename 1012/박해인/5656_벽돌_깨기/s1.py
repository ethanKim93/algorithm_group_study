import sys
sys.stdin = open('sample_input.txt')

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]  # 상 하 좌 우

def shoot(N, W, H):
    global data2

    for i in range(H):


def npr(n, k, W, H):
    global result
    if n == k:
        r = shoot(k, W, H)
        if result > r:
            result = r

    else:
        for i in range(W):
            p[n] = i
            npr(n+1, k, W, H)
            if result == 0:
                return

T = int(input())
T = 1
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    data2 = [[0]*W for _ in range(H)]
    p = [0] * N
    result = W * H

    npr(0, N, W, H)

    print('#{} {}'.format(test_case, result))