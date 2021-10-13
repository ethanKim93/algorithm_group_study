import sys
sys.stdin = open('sample_input.txt')

# 시계방향 : 하우, 하좌, 상좌, 상우 방향
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def circuit(i, j, k, num):
    global max_eat
    if (i, j) == start:
        max_eat = max(max_eat, num)
        return
    if i < 0 or i >=N or j < 0 or j >= N: return
    if cnt[dissert[i][j]]: return

    cnt[dissert[i][j]] = 1                              # 방문 처리
    if k < 2:                                             
        circuit(i+di[k], j+dj[k], k, num+1)             # 방향 유지하는 경우
        circuit(i+di[k+1], j+dj[k+1], k+1, num + 1)     # 방향 전환하는 경우
    elif k == 2:
        if i+j == sum(start):                           # 시작점과 대각선 방향으로 나란해지면 방향 전환
            circuit(i+di[k+1], j+dj[k+1], k+1, num+1)   
        circuit(i+di[k], j+dj[k], k, num+1)   
    elif k == 3:
        circuit(i+di[k], j+dj[k], k, num+1)             # 시작점 만날 때까지 앞으로만 이동
    cnt[dissert[i][j]] = 0                              # 방문 해제

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dissert = [list(map(int, input().split())) for _ in range(N)]
    max_eat = -1
    
    for i in range(N):
        for j in range(N):
            start = (i, j)
            cnt = [0]*101                               # 방문 여부 확인을 위한 카운트 배열 정의 1~100
            cnt[dissert[i][j]] = 1
            circuit(i+1, j+1, 0, 1)                     # 하, 우 방향으로 한칸 이동 후 시작

    print('#{} {}'.format(tc, max_eat))
