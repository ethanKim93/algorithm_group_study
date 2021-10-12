import sys
sys.stdin = open('sample_input.txt')


def perm(n,r,s,k):
    global result
    if k == r:
        combB = []
        for m in range(N):
            if m not in combA:
                combB.append(m)
        ansA = ansB = 0
        for i in range(N//2):
            for j in range(N//2):
                if i != j:
                    ansA += board[combA[i]][combA[j]]
                    ansB += board[combB[i]][combB[j]]
        res = abs(ansA-ansB)
        result = min(res, result)
        return
    else:
        for i in range(s,n-r+k+1):
            combA[k] = i
            perm(n,r,i+1,k+1)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    peA =[]
    peB =[]
    combA =[0] * (N//2)
    result = 987654321
    perm(N,N//2,0,0)
    print('#{} {}'.format(tc,result))



# 순열은 중복이 많아 시간초과나므로 조합으로 풀기
# def perm(n,k):
#     global result
#     if k == n:
#         res = cal(arr[:])
#         result = min(result, res)
#         return
#
#     else:
#         for i in range(k,n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n,k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
#
# def cal(li):
#     ansA = ansB = 0
#     for i in range(N//2):
#         for j in range(N//2):
#             if i != j:
#                 ansA += board[li[i]][li[j]]
#     for m in range(N//2,N):
#         for n in range(N//2,N):
#             if m != n:
#                 ansB += board[li[m]][li[n]]
#     return abs(ansA-ansB)
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     board = [list(map(int,input().split())) for _ in range(N)]
#     arr = [i for i in range(N)]
#     per = []
#     result = 987654321
#     perm(N,0)
#     print('#{} {}'.format(tc,result))