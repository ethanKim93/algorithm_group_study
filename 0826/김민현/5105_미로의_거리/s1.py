import sys
sys.stdin = open("sample_input.txt")

T = int(input())

ax = [0,1,0,-1]
ay = [1,0,-1,0]

def escape(matrix):
    q = []
    #시작점, 끝점 찾기
    for i in range(N+2):
        for j in range(N+2):
            if matrix[i][j] == '2':start = [i,j]
    visit[start[0]][start[1]] = 0


    while 1:
        x,y = int(start[0]),int(start[1])
        for k in range(4):
            if int(matrix[x+ax[k]][y+ay[k]]) != 1 and visit[x+ax[k]][y+ay[k]] == 0: #벽이 아니면서,
                visit[x+ax[k]][y+ay[k]] += visit[x][y] + 1
                q.append([x+ax[k],y+ay[k]])
                if matrix[x+ax[k]][y+ay[k]] == '3':
                    return visit[x+ax[k]][y+ay[k]]-1
        if not q: #q가 없을때
            return 0
        else:
            start = q.pop(0)



for tc in range(1,T+1):
    N = int(input())
    matrix = [[1]+ list(input()) + [1] for _ in range(N)] #미로 전체를 좌우를 1로 막음
    #미로 상하를 1로 막음
    block = [1]*(N+2)
    matrix.append(block)
    matrix.insert(0,block)
    visit = [[0]*(N+2) for _ in range(N+2)]
    candidate = [] #경로값 후보

    print('#{} {}'.format(tc,escape(matrix)))



    #print('#{} {}'.format(tc,visit[G]))
