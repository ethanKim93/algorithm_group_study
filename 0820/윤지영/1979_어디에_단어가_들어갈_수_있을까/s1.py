import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N,K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    result_r = cnt = 0
    for i in range(N):
        for j in range(N):
            if li[i][j] == 1:
                cnt += 1
            if li[i][j] == 0 or j == N-1:
                if cnt == K:
                    result_r += 1
                cnt = 0
    result_c = cnt = 0
    for i in range(N):
        for j in range(N):
            if li[j][i] == 1:
                cnt += 1
            if li[j][i] == 0 or j == N-1:
                if cnt == K:
                    result_c += 1
                cnt = 0
    ans = result_c + result_r
    print('#{} {}'.format(tc,ans))


# def check(N, K, reverse='True'):
#     result = cnt = 0
#     li_1 = li[:]
#     for i in range(N):
#         for j in range(N):
#             j_1 = j
#             if reverse == 'False':
#                 li_1[i][j] = li[j][i]
#                 j_1 = i
#             if li_1[i][j] == 1:
#                 cnt += 1
#             if li_1[i][j] == 0 or j_1 == N-1:
#                 if cnt == K:
#                     result += 1
#                 cnt = 0
#     return result

