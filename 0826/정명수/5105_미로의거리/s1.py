import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #미로의 크기
    miro = [list(input()) for _ in range(N)]
    s_i = s_j = 0
    for i in range(N):
        for j in range(N):
            miro[i][j] = int(miro[i][j])
            if miro[i][j] == 2:
                s_i = i
                s_j = j
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = [(s_i,s_j)]
    visited = [[0]*N for _ in range(N)]
    visited[q[0][0]][q[0][1]] = 1
    flag = 0
    while q:
        t = q.pop(0)
        for i in range(4):
            if t[0]+dx[i] >= 0 and t[1]+dy[i] >=0 and t[0]+dx[i] < N and t[1]+dy[i] <N:
                if miro[t[0]+dx[i]][t[1]+dy[i]] == 0 and not visited[t[0]+dx[i]][t[1]+dy[i]]:
                    q.append((t[0]+dx[i], t[1]+dy[i]))
                    visited[t[0]+dx[i]][t[1]+dy[i]] = visited[t[0]][t[1]]+1
                if miro[t[0]+dx[i]][t[1]+dy[i]] == 3:
                    visited[t[0] + dx[i]][t[1] + dy[i]] = visited[t[0]][t[1]] + 1
                    s_i = t[0] + dx[i]
                    s_j = t[1] + dy[i]
                    flag = 1
                    break
    print('#{} '.format(tc),end='')
    if flag:
        print(visited[s_i][s_j]-2)
    else:
        print(0)

