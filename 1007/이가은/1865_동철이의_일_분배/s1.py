import sys
sys.stdin = open('input.txt')

def per(idx, cnt):
    global result

    if idx == N:
        if result <= cnt:
            result = cnt
        return

    if result >= cnt:
        return

    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1                                         # 방문표시하기
            per(idx+1, round(cnt*pro[idx][i],8))                  # 다음 idx 봐주기
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pro = list(list(map(lambda x : int(x)/100, input().split())) for _ in range(N))
    visited = [0 for _ in range(N)]
    result = 0

    per(0,1)
    print('#{} {:.6f}'.format(tc,result))
