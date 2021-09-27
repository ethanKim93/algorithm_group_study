import copy
import sys
sys.stdin = open('sample_input.txt')

def dfs(G, v, k, cnt):
    global max_cnt
    stack.append(v)
    while stack:
        i,j = stack.pop()
        visited[i][j] = 1
        cnt += 1
        for m in range(4):
            ni = i + di[m]
            nj = j + dj[m]
            if 0<= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 :
                    if (G[ni][nj] < G[i][j]):
                        dfs(G,[ni,nj], k, cnt)
                    elif k > 0 :
                        diff = G[ni][nj] - G[i][j]
                        if diff+1 <= k:
                            # 깊은 복사해야 오류안남 -> 왜냐하면 리스트 자체를 바꿔버리므로 재귀에서 리턴해서 돌아와도 복구가 안됨
                            li_G = copy.deepcopy(G)
                            li_G[ni][nj] -= diff+1
                            dfs(li_G, [ni,nj],-1, cnt)
                            # deepcopy는 오래걸리므로, 밑에처럼 복구하는 방법이 좀 더 효율적인듯
                            # temp = G[ni][nj]
                            # G[ni][nj] -= diff + 1
                            # dfs(G, [ni, nj], -1, cnt)
                            # G[ni][nj] = temp
        if cnt > max_cnt:
            max_cnt = cnt
        visited[i][j] = 0
                
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    map_list = [list(map(int,input().split())) for _ in range(N)]
    max_width = 0
    idx = []

    stack = []
    # map_list[i][j] 가 max_width와 같아지면 idx 리스트에 해당 좌표 추가
    # + 만약 max_width가 갱신된다면, 현재까지의 idx 리스트를 초기화하고 다시 최고높이와 같은 좌표들만 추가하면 이중반복 안 돌 수 있음
    for i in range(N):
        for j in range(N):
            if map_list[i][j] > max_width:
                max_width = map_list[i][j]
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == max_width:
                idx.append([i,j])
    di = [0,0,-1,1]
    dj = [-1,1,0,0]
    # 좌 우 상 하
    cnt = max_cnt = 0
    for x,y in idx:
        visited = [[0] * N for _ in range(N)]
        # 깊은 복사해야 오류 안남
        li = copy.deepcopy(map_list)
        dfs(li,[x,y],K,0)
    print('#{} {}'.format(tc,max_cnt))
    
