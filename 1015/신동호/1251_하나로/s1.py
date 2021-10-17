import sys
sys.stdin = open('input.txt')

def prim(s):
    # 입력값이 매우 커서 987654321 보다 커야 함
    key = [999987654321] * N
    MST = [False] * N
    key[s] = 0
    for _ in range(N):
        minV = 999987654321
        for i in range(N):
            if not MST[i] and key[i] < minV:
                minV = key[i]
                minI = i
        MST[minI] = True

        for i in range(N):
            # 모든 정점과의 거리 제곱으로 비교
            if not MST[i] and key[i] > (land[0][minI] - land[0][i]) ** 2 + (land[1][minI] - land[1][i]) ** 2:
                key[i] = (land[0][minI] - land[0][i]) ** 2 + (land[1][minI] - land[1][i]) ** 2
    return sum(key)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    land = [[] for _ in range(N)]
    for i in range(2):
        land[i] = list(map(int, input().split()))
    E = float(input())
    print('#{} {:.0f}'.format(tc, E * prim(0)))