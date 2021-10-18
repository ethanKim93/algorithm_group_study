import sys
sys.stdin = open('s_input.txt')

T = int(input())

def dfs(x):
    for i in range(1,M+1):


for tc in range(1,T+1):
    N,M,X = map(int,input().split())

    adj1 = [[987654321] * (N + 1) for _ in range(N + 1)]  # 원래입력 (진출)
    adj2 = [[987654321] * (N + 1) for _ in range(N + 1)]  # 뒤집은입력 (진입)

    for i in range(M):
        x, y, c = map(int, input().split())  # c가중치
        adj1[x][y] = c
        adj2[y][x] = c


    dist1 = [987654321] * (N + 1)
    dist2 = [987654321] * (N + 1)

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print("#{} {}".format(tc, max_value))

