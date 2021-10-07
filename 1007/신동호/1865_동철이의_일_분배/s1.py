import sys
sys.stdin = open('input.txt')

def backtrack(s=0, tot=1):
    global N, visited, P, ans
    if s == N:
        if ans < tot:
            ans = tot
        return
    for i in range(N):
        if not visited[i]:
            if tot * P[s][i]/100 > ans: # 시간 초과가 뜨지 않게 하는 핵심 부분, backtrack을 들어간 후 ans보다 큰지 검증하는 것보다 ans보다 큰지 검증하고 들어가는 것이 시간 훨씬 절약됨
                visited[i] = 1
                backtrack(s+1, tot * P[s][i]/100)
                visited[i] = 0
	            

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    backtrack()
    print('#{} {:.6f}'.format(tc, ans * 100))

# 시간 초과 뜨는 코드
# def backtrack(s=0, tot=1):
#     global N, visited, P, ans
#     if s == N:
#         if ans < tot:
#             ans = tot
#         return
#     if tot < ans:
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             backtrack(s+1, tot * P[s][i]/100)
#             visited[i] = 0


# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     P = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     ans = 0
#     backtrack()
#     print('#{} {:.6f}'.format(tc, ans * 100))