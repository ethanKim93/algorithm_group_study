import sys
sys.stdin = open("input.txt")

def bfs(s):
    di = [1, -1, 0, 0] #방향 탐색 위한 델타
    dj = [0, 0, -1, 1]

    q = [] #queue
    i, j = s[0], s[1] #초기 시작 값 좌표
    q.append([i,j]) #좌표를 넣어주고 시작

    while q:
        i, j = q.pop(0) #들어있는 좌표를 빼내 순회 함
        for k in range(4): #상하좌우를 탐색
            ni = i + di[k] #초기값으로부터 방향값을 더해 상하좌우를 탐색 할 새 i, j
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: #ni, nj가 범위 내에 있는지 확인(인덱스에러방지)
                if visited[ni][nj] == 0: #만약 통로이면 갈수 있음
                    if arr[ni][nj] == 3: #도착점에 도착하면
                        return "1" #끝
                    elif arr[ni][nj] == 0: #계속 통로이면
                        q.append([ni,nj]) #이동한걸 fix시켜 다시 q에 넣으면 반복문 돌며 꺼내 쓴다
                        visited[ni][nj] = 1 #방문 표시
    return "0"


N = 16
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N): #출발점을 찾을 반복문
        for j in range(N):
            if arr[i][j] == 2:
                s = (i, j)

    visited = [[0]*N for _ in range(N)] #방문을 기록할(다시 안가기 위해) 리스트
    print('#{} {}'.format(tc, bfs(s)))


# """
# #1 1
# #2 1
# #3 1
# #4 0
# #5 1
# #6 1
# #7 0
# #8 1
# #9 1
# #10 1
# """
