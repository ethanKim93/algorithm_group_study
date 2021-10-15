import sys
# 하나의 경우에서 각 연산에 대한 가지를 뻗어나가야하므로 bfs
# dfs - 시간초과 // 백트레킹 열심히 하면 될것같기도 하지만 너무 복잡..
sys.stdin = open('sample_input.txt')

import collections

oper = [['*',2],['+',1],['-',1],['-',10]]

def bfs(n):
    global result, size, end
    que = collections.deque([])
    que.append(n)
    while que:
        res,cnt = que.popleft()
        if cnt > result:
            continue
        else:
            for i in range(4):
                op, n = oper[i]
                res1 = res2 = res3 = 0
                if op == '+':
                    res1 = res+n
                    if res1 < size and visited[res1] == 0 :
                        que.append([res1,cnt+1])
                        visited[res1] = 1
                elif op == '-':
                    res2 = res-n
                    if 0 < res2 < size and visited[res2] == 0:
                        que.append([res2,cnt+1])
                        visited[res2] = 1
                elif op == '*':
                    res3 = res*n
                    if res3 < size and visited[res3] == 0:
                        que.append([res3,cnt+1])
                        visited[res3] = 1
                if res1 == end or res2 == M or res3 == M :
                    result = min(result,cnt+1)


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    start = min(N,M)
    end = max(M,N)
    result = 987654321
    size = 1000000
    visited =[0] * 1000001           # 방문표시안하면 메모리 터짐
    bfs([start,0])
    print('#{} {}'.format(tc,result))

#
# def dfs(res,cnt):
#     global result, M
#     if result < cnt :
#         return
#     if res == M:
#         result = min(result,cnt)
#         return
#     if res > M:
#         return
#     else:
#         for i in range(4):
#             op, n = oper[i]
#             if op == '+':
#                 dfs(res+n,cnt+1)
#             elif op == '-':
#                 dfs(res-n,cnt+1)
#             elif op == '*':
#                 dfs(res*n, cnt+1)