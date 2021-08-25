import sys
sys.stdin = open('input.txt')
min_sum = 90
def pat(check, n, sumt):
    global min_sum
    if sum(check) == N:
        if min_sum > sumt:
            min_sum = sumt
    else:
        if sumt > min_sum:
            return
        for i in range(N):
            if check[i] != 1:
                check[i] = 1
                pat(check,n+1,sumt+arr[n][i])
                check[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    check = [0]*N
    sum_a = 0
    min_sum = 90
    pat(check, 0, 0)
    print('#{} '.format(tc),end='')
    print(min_sum)
