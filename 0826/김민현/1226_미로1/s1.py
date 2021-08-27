import sys
sys.stdin = open("input.txt")

ax = [1,0,-1,0]
ay = [0,1,0,-1]

def start(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 2:return i,j

def bfs(data,x,y):
    q = []
    visit = []
    q.append([x,y])
    visit.append([x,y])
    while q:
        x,y = q.pop(0)
        for i in range(4):
           if data[x+ax[i]][y+ay[i]] != 1 and [x+ax[i],y+ay[i]] not in visit:
                q.append([x+ax[i],y+ay[i]])
                visit.append([x+ax[i],y+ay[i]])
           if data[x+ax[i]][y+ay[i]] == 3:
               return 1
           a = 1
    return 0

for _ in range(1,11):
    tc = int(input())
    matrix = [list(map(int,input())) for _ in range(16)]
    si,sj = start(matrix)
    print('#{} {}'.format(tc,bfs(matrix,si,sj)))
