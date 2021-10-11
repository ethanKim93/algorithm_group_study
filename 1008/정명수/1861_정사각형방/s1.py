import sys
sys.stdin = open('input.txt')

def finder(a,b):
    max_num = arr[a][b]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [(a,b)]
    while q:
        t1,t2 = q.pop()
        for i in range(4):
            di = dx[i]+t1
            dj = dy[i]+t2
            if 0 <= di < N and 0 <= dj < N:
                if arr[di][dj]-1 == arr[t1][t2]:
                    q.append((di, dj))
                    max_num = max(max_num,arr[di][dj])
    return max_num

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    answer = arr[0][0]
    for i in range(N):
        for j in range(N):
            cnt = finder(i,j)-arr[i][j]+1
            if cnt == max_cnt and answer > arr[i][j]:
                max_cnt = cnt
                answer = arr[i][j]
            elif cnt > max_cnt:
                max_cnt = cnt
                answer = arr[i][j]
    print('#{} {} {}'.format(tc,answer,max_cnt))