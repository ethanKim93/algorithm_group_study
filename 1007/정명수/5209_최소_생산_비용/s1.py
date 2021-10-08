import sys
sys.stdin = open('sample_input.txt')

def howmuch(arr):
    cost = 0
    for i in range(N):
        cost += company[i][arr[i]]
    return cost

def backtrack(n,cost):
    global min_case
    if n >= N:
        if cost < min_case:
            min_case = cost
        return
    if cost >= min_case:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(n+1,cost+company[n][i])
            visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    company = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    min_case = 100000
    backtrack(0,0)
    print('#{} {}'.format(tc,min_case))