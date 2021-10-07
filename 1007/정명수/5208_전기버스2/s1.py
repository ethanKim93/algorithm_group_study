import sys
sys.stdin = open('sample_input.txt')

def backtrack(n,cnt):
    global min_case
    if n >= N:
        if cnt < min_case:
            min_case = cnt
        return
    if cnt >= min_case:
        return
    for i in range(1,oilbank[n]+1):
        backtrack(n+i,cnt+1)

T = int(input())
for tc in range(1,T+1):
    oilbank = list(map(int,input().split()))
    N = oilbank[0]
    min_case = 100
    cnt = 0
    backtrack(1,0)
    print('#{} {}'.format(tc,min_case-1))
