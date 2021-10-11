import sys
sys.stdin = open('sample_input (1).txt')


def paste(i,j, ans):
    global cnt
    if len(ans) == 7:
        result.add(ans)
        return
    while i < 4 and j < 4:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                paste(ni,nj,ans+str(board[ni][nj]))
                ni -= di[k]
                nj -= dj[k]
                i = ni
                j = nj
        return
    return

T = int(input())
for tc in range(1,T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    #    우 하 좌 상
    cnt = 0
    result = set()
    for i in range(4):
        for j in range(4):
            paste(i,j,str(board[i][j]))
    print('#{} {}'.format(tc,len(result)))





# 한번 방문한 곳 방문 못한다는 가정 하에 작성
# result = []
# def paste(i,j, ans):
#     if len(ans) == 7:
#         if ans not in result:
#             result.append(ans)
#         return
#     while i < 4 and j < 4:
#         visited[i][j] = 1
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             while 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] == 0:
#                 visited[ni][nj] = 1
#                 paste(ni,nj,ans+str(board[ni][nj]))
#                 visited[ni][nj] = 0
#                 ni -= di[k]
#                 nj -= dj[k]
#         return
#
#
# T = int(input())
# for tc in range(1,T+1):
#     board = [list(map(int,input().split())) for _ in range(4)]
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     #    우 하 좌 상
#     visited = [[0] * 4 for _ in range(4)]
#     for i in range(4):
#         for j in range(4):
#             paste(i,j,str(board[i][j]))
#     print(result)


# 처음에 시도했던 리스트에 append 하는 방식 런타임 에러 해결 (아마 메모리 초과 or while 무한반복였던듯..?)
# def paste(i,j, ans):
#     global cnt
#     if len(ans) == 7:
#         if ans not in result:
#             result.append(ans)
#             cnt += 1
#         return
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < 4 and 0 <= nj < 4:
#             paste(ni,nj,ans+str(board[ni][nj]))
#
# T = int(input())
# for tc in range(1,T+1):
#     board = [list(map(int,input().split())) for _ in range(4)]
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     #    우 하 좌 상
#     cnt = 0
#     result = []
#     for i in range(4):
#         for j in range(4):
#             paste(i,j,str(board[i][j]))
#     print('#{} {}'.format(tc,cnt))