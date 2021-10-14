import sys
sys.stdin = open('../5251_최소_이동_거리/sample_input.txt')


# def DFS(num, cnt):
#     global ans
#     if num == M and num <= 1000000:
#         if ans > cnt:
#             ans = cnt
#     else:
#         if cnt < ans:
#             if num <= M//2:
#                 DFS(num * 2, cnt + 1)
#             elif num < M:
#                 DFS(num + 1, cnt + 1)
#             elif num >= M-10:
#                 DFS(num - 10, cnt + 1)
#             else:
#                 DFS(num - 1, cnt + 1)


# def BFS(s, cnt):
#     global ans
#     Q = [(s, cnt)]
#     while Q:
#         curr = Q.pop()
#         n = curr[0]
#         c = curr[1]
#         if c < ans and n <= M*2+1:
#             if n == M:
#                 if ans > c:
#                     ans = c
#             elif n < M:
#                 Q.append((n*2, c+1))
#                 Q.append((n+1, c+1))
#             else:
#                 Q.append((n-1, c+1))
#                 Q.append((n-10, c+1))


# def DFS(m, cnt):
#     global ans
#     if m < N // 2:
#         return
#     if m == N:
#         if ans > cnt:
#             ans = cnt
#     else:
#         if cnt < ans:
#             if m % 2:
#                 DFS(m - 1, cnt + 1)
#                 DFS(m + 1, cnt + 1)
#                 DFS(m + 10, cnt + 1)
#             else:
#                 DFS(m // 2, cnt + 1)


def DFS(num, cnt):
    global ans
    stack = [(num, cnt)]
    while stack:
        m, c = stack.pop()
        print(m, c)
        if m == N and ans > c:
            ans = c
        if c < ans and m > 0:
            if m % 2:
                stack.append((m+1, c+1))
                stack.append((m-1, c+1))
                stack.append((m+10, c+1))
            else:
                stack.append((m//2, c+1))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ans = 987654321
    DFS(M, 0)
    print('#{} {}'.format(tc, ans))