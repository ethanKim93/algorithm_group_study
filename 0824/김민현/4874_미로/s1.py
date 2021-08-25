import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [[1]+list(map(int,input()))+[1] for _ in range(N)]
    block = [1]*(N+2)
    matrix.insert(0,block)
    matrix.append(block)

    ax = [0,1,0,-1]
    ay = [1,0,-1,0]

    visit = []
    for i in range(N+2):
        for j in range(N+2):
            if matrix[i][j] == 2:
                start = (i,j)
            elif matrix[i][j] == 3:
                end = (i,j)

    x,y = start

    stack = [start]
    ans = 0
    while True:
        visit.append((x,y))
        for k in range(4): #이동 가능한 곳 stack에 저장.
            c = matrix[x+ax[k]][y+ay[k]]
            if matrix[x+ax[k]][y+ay[k]] == 3:  # 끝좌표와 같다면
                ans = 1
                break
            elif matrix[x+ax[k]][y+ay[k]] == 0 and (x+ax[k],y+ay[k]) not in visit:
                stack.append((x+ax[k],y+ay[k]))
        if ans == 1: break
        if stack: #stack이 있다면,
                x,y = stack.pop()
        else: #stack이 없을 경우
            ans = 0
            break

    print('#{} {}'.format(tc,ans))