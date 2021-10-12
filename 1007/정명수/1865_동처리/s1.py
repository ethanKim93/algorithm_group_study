import sys
sys.stdin = open('input.txt')


def backtrack(n,posible):
    global max_case
    if n >= N:
        if posible > max_case:
            max_case = posible
        return
    if posible <= max_case:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(n+1,posible*company[n][i])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    company = [list(map(lambda x:int(x)/100,input().split())) for _ in range(N)]
    visited = [0]*N
    max_case = 0
    backtrack(0,1)
    print('#{} {:.6f}'.format(tc,max_case*100))