import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    miro = [list(input()) for _ in range(16)]
    s_i = s_j = 0
    for i in range(16):
        for j in range(16):
            miro[i][j] = int(miro[i][j])
            if miro[i][j] == 2:
                s_i = i
                s_j = j
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = [(s_i,s_j)]
    flag = 0
    while q:
        t = q.pop(0)
        for i in range(4):
            if t[0]+dx[i] >= 0 and t[1]+dy[i] >=0 and t[0]+dx[i] < 16 and t[1]+dy[i] <16:
                if miro[t[0]+dx[i]][t[1]+dy[i]] == 0:
                    q.append((t[0]+dx[i], t[1]+dy[i]))
                    miro[t[0]+dx[i]][t[1]+dy[i]] = 1
                if miro[t[0]+dx[i]][t[1]+dy[i]] == 3:
                    flag = 1
                    break
    print('#{} '.format(tc),end='')
    if flag:
        print(1)
    else:
        print(0)

