# 이진석
import sys
sys.stdin = open('sample_input.txt')
delta = [(0,1), (1, 0)]   # 우, 하

def search(x,y):
    global total,min_total
    if min_total <= total:  # 현재까지의 합이 최소값보다 크면 종료
        return

    if x == N-1 and y == N-1:   # 도착지점에 도달하면 종료
        if total < min_total:   # 최소값 갱신
            min_total = total
        return

    for d in delta:
        nx = x + d[0]
        ny = y + d[1]
        if nx < N and ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            total += table[nx][ny]
            search(nx,ny)
            visited[nx][ny] = 0
            total -= table[nx][ny]


for tc in range(1, int(input())+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    total = table[0][0]     # 한 경로의 합을 담을 변수, 이동할때마다 더하기때문에 시작지점을 더해주고 시작
    min_total = (N**2)*10   # 최소합을 담을변수, 모든 경로를 더했을 때의 최댓값으로 초기화
    search(0,0) # 탐색시작
    print('#{} {}'.format(tc, min_total))