#시간 초과
import sys
sys.stdin = open('input.txt')
def p(n):
    global min_sum
    if n == N:
        idx = 0
        arsum = 0
        for k in P:
            arsum += arr[idx][k]
            idx += 1
        if arsum < min_sum:
            min_sum = arsum

    else:
        if sum(P) > min_sum:
            return
        for i in range(n,N):
            P[i], P[n] = P[n], P[i]
            p(n+1)
            P[i], P[n] = P[n], P[i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = list(range(N))
    arr = []
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    min_sum = arr[0][0]+arr[1][1]+arr[2][2]
    p(0)
    print('#{} {}'.format(tc,min_sum))
