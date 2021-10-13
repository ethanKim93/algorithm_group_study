import sys
sys.stdin = open("sample_input.txt")


dx = [1,-1,0,0]
dy = [0,0,1,-1]

T = int(input())

def DFS(r,c,line):
    if len(line) == 7:
        #if line not in ans:
        ans.add(line)
        return

    for k in range(4):
        dr = r + dx[k]
        dc = c + dy[k]

        if dr < 0 or dr >= 4 or dc < 0 or dc >= 4:
            continue

        DFS(dr,dc,line+board[dr][dc])

for tc in range(1,T+1):
    board = [list(map(str,input().split()))for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            DFS(i,j,board[i][j])

    print("#{} {}".format(tc,len(ans)))