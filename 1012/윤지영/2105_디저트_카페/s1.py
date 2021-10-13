import sys
sys.stdin = open('sample_input.txt')

def move(x,y,l,k,stack,visited):
    for _ in range(l-1):
        x += di[k]
        y += dj[k]
        if 0<= x < N and 0 <= y < N and visited[board[x][y]] == 0:
            visited[board[x][y]] = 1
            stack.append(board[x][y])
        else:
            return -1, -1
    return x,y


def search(x,y,wid,he):
    visited = [0] * 101
    stack = []
    for i in range(4):
        if i %2 == 0:
            x,y = move(x,y,he,i,stack,visited)
        elif i % 2:
            x,y = move(x,y,wid,i,stack,visited)
        if x == -1 or y == -1:
            return -1
    return len(stack)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    di = [1,1,-1,-1]
    dj = [1,-1,-1,1]
    res = -1
    for i in range(N - 2):
        for j in range(1,N-1):
            for m in range(2,N):
                for n in range(2,N):
                    ans = search(i,j,m,n)
                    res = max(res,ans)
    print('#{} {}'.format(tc,res))



# if k == 0 and (i > ni or j > nj):
#     return
# if k == 1 and (ni < i or nj > j):
#     return
# if k == 2 and (ni > i or nj > j):
#     return
# if k == 3 and (ni > i or nj < j):
#     return


# 재귀 - 실패 : 오른쪽아래 > 왼쪽아래 > 왼쪽위 > 그다음에 위로 계속 올라가야하는데 왼쪽 아래로 다시 내려가는 경우도 포함되어버림
# def dfs(start,now, ans):
#     global res
#     if start == now and (ans >= 4):
#         res = max(res,ans)
#         return
#     else:
#         i,j = now
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :
#                 if board[ni][nj] not in stack:
#                     visited[ni][nj] = 1
#                     stack.append(board[ni][nj])
#                     dfs(start,[ni,nj],ans + 1)
#                     visited[ni][nj] = 0
#                     stack.pop()
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     board = [list(map(int,input().split())) for _ in range(N)]
#     di = [1,1,-1,-1]
#     dj = [1,-1,-1,1]
#     res = -1
#     visited = [[0] * N for _ in range(N)]
#     for i in range(N-2):
#         for j in range(1,N-1):
#             stack = []
#             dfs([i,j],[i,j],0)
#     print('#{} {}'.format(tc,res))