import sys, time
sys.stdin = open('input.txt')


#가지치기 X
def powerset(n):
    global hei_sum, N
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                pow[i].append(height[j])
        ans = sum(pow[i])
        if ans >= B and (hei_sum > ans):
            hei_sum = ans

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    height = sorted(list(map(int,input().split())))
    hei_sum = 987654321
    pow = [[] for _ in range(1<<N)]
    powerset(height)
    print('#{} {}'.format(tc,hei_sum-B))




# 가지치기..?
# def powerset(n,k, ans,rs):
#     global hei_sum
#     if k == n:
#         if ans >= B:
#             if hei_sum > ans:
#                 hei_sum = ans
#             return
#     if ans + rs < B :
#         return
#     else:
#         for i in range(n):
#             if used[i] == 0:
#                 p[i] = arr[i]
#                 used[i] = 1
#                 powerset(n,k+1, ans+height[p[i]],rs-height[p[i]])
#                 used[i] = 0
#
# T = int(input())
# for tc in range(1,T+1):
#     N, B = map(int,input().split())
#     height = sorted(list(map(int,input().split())))
#     hei_sum = 987654321
#     p = [0] * (N+1)
#     tot = sum(height)
#     arr = [i for i in range(N)]
#     used = [0] * (N+1)
#     powerset(N,0,0,tot)
#     print('#{} {}'.format(tc,hei_sum-B))