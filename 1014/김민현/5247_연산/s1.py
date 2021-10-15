#구현 실패
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def bfs(num,cnt):
    global min_cnt
    if (cnt,num) in usenum:
        return
    usenum.add((cnt,num))
    #print(cnt,num)
    if num > 1000001:
        return
    if cnt > min_cnt:
        return

    if num == M:
        if cnt <= min_cnt:
            min_cnt = cnt
        return
    elif num < M:
        bfs(num*2, cnt+1)
        bfs(num+1, cnt+1)
    elif num > M:
        bfs(num-10, cnt+1)
        bfs(num-1, cnt+1)



for tc in range(1,T+1):
    N,M = map(int,input().split())

    min_cnt = abs(M-N)
    usenum = set()
    bfs(N,0)
    print('#{} {}'.format(tc,min_cnt))