import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def go(start):
    global min_cnt,cnt
    battery = station[start]
    if (start + battery) >= (N-1):
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for j in range(1,battery+1):
        if cnt > min_cnt:
            break
        cnt += 1 #cnt 증가
        if start+j < N-1:
            go(start+j)
        cnt -= 1 #cnt 감소

for tc in range(1,T+1):

    data = list(map(int,input().split()))
    N = data[0]
    station = data[1:]+[0]
    min_cnt = N
    cnt = 0
    go(0)
    print('#{} {}'.format(tc,min_cnt))
