import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [0,1]
dy = [1,0]
def small(i,j,sums):
    global min_case
    if i==N-1 and j==N-1:
        if sums<min_case:
            min_case = sums
        return
    if sums>min_case:
        return
    for x in range(2):
        di = i+dx[x]
        dj = j+dy[x]
        if 0<=di<N and 0<=dj<N:
            small(di,dj,sums+arr[di][dj])

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_case = 1000000
    small(0,0,arr[0][0])
    print('#{} {}'.format(tc,min_case))
