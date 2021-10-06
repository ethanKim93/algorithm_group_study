import sys
sys.stdin = open('sample_input.txt')

dx = [0 , 1]
dy = [1 , 0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    visit = [[0]*N for _ in range(N)] #방문리스트
    queue = []
    ans_list= [] #후보값 리스트(이중 가장 최소값이 정답)
    x,y = 0,0 #최초 탐색 시작위치
    queue.append((x,y))
    visit[0][0] = board[0][0] #시작값 입력

    while queue:
       x,y = queue.pop(0)
       for k in range(2):
           i = x + dx[k]
           j = y + dy[k]
           if i < N and j < N: #board의 범위를 넘지 않으면서
               if not visit[i][j]: #방문한적이 없다면
                   visit[i][j] = visit[x][y] + board[i][j] #visit에 누적합 저장
                   queue.append((i,j))
               elif visit[i][j] > visit[x][y] + board[i][j]: #방문 했어도 visit에 저장된값보다 작다면
                   visit[i][j] = visit[x][y] + board[i][j] #최소값으로 다시저장

               if i == N -1 and j == N-1:
                   ans_list.append(visit[i][j]) #마지막 위치에서의 값 리스트로 저장

    print('#{} {}'.format(tc,min(ans_list)))#최소값 출력