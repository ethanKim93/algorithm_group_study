import sys
sys.stdin = open('input.txt')
def find(u,v):
    global flag
    if miro[u][v-1] == '3' or miro[u][v+1] == '3' or miro[u+1][v]=='3' or miro[u-1][v]=='3':
        flag = 1
    else:
        if miro[u][v-1] == '0':
            miro[u][v-1] = '1'
            find(u,v-1)
        if miro[u][v+1] == '0':
            miro[u][v + 1] = '1'
            find(u,v+1)
        if miro[u+1][v] == '0':
            miro[u+1][v] = '1'
            find(u+1,v)
        if miro[u-1][v] == '0':
            miro[u-1][v] = '1'
            find(u-1,v)
        return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = []
    flag=0
    for _ in range(N):
        hang = list(input())
        hang = ['1']+ hang + ['1']
        miro.append(hang)
    miro.insert(0,['1']*(N+2))
    miro.append(['1']*(N+2))
    for i in range(N+2):
        for j in range(N+2):
            if miro[i][j] == '2':
                start_i = i
                start_j = j
    print('#{}'.format(tc),end=' ')
    find(start_i,start_j)
    if flag:
        print(1)
    else:
        print(0)
