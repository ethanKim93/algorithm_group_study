import sys
sys.stdin = open('sample_input.txt')

def per(idx, cnt):
    global result, cnt

    if idx == N:
        if result > cnt:                # 지정된 result 값 보다 cnt가 최소이면
            result = cnt                # 최솟값으로 지정
        return

    if result <= cnt:                   # 가지치기
        return

    for i in range(0, N):
        if visited[i] == 0:
            cnt += factory[idx][i]      # 생산비용 더하기
            visited[i] = 1              # 방문표시하기
            per(idx+1)                  # 다음 idx 봐주기
            cnt -= factory[idx][i]      # 원복
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 9999999999
    cnt = 0
    visited = list(0 for i in range(N))
    factory = list(list(map(int, input().split())) for _ in range(N))

    per(0)
    print('#{} {}'.format(tc,result))