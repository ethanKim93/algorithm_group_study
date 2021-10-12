import sys
sys.stdin = open('input.txt')

def perm(n,k,ans):
    global max_per
    if ans == 0:
        return
    if ans < max_per:
        return
    if k == n:
        if ans > max_per:
            max_per = ans
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1,ans*percent[k-1][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    percent = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            percent[i][j] /= 100
    max_per = 0
    arr = [i for i in range(N)]
    perm(N,0,1)
    print('#{} {:06.6f}'.format(tc,max_per*100))





# 시간 초과 -> 최대값 갱신하고 리턴을 안해서 시간초과난거였다...

def perm(n,k,ans):
    global max_per
    if ans == 0:
        return
    if ans <= max_per:
        return
    if k == n:
        if ans > max_per:
            max_per = ans
        return
    else:
        for i in range(N):
            if not used[i]:
                p[k] = arr[i]
                used[i] = 1
                perm(n,k+1,ans*percent[k][p[k]])
                used[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    percent = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            percent[i][j] /= 100
    max_per = 0
    used = [0] * (N+1)
    p = [0] * N
    arr = [i for i in range(N)]
    perm(N,0,1)
    print('#{} {:06.6f}'.format(tc,max_per*100))