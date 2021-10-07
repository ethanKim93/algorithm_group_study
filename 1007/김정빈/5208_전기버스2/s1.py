import sys
sys.stdin = open("sample_input.txt")

def dfs(idx):
    global cnt, res
    if idx >= len(mi):  # 도착했을 때
        if cnt < res:  # 충전 최소값 찾기
            res = cnt
        return
    if cnt >= res: # 도착안했는데도 res보다 cnt가 크면 유망하지 x 로 종료
        return
    for i in range(mi[idx]+idx, idx, -1):
        cnt += 1
        dfs(i)
        cnt -= 1

for tc in range(1, int(input())+1):
    base = list(map(int, input().split()))
    n, mi = base[0], [0]+base[1:]
    res, cnt = 99999, -1 # 최저 충전횟수, 충전 횟수
    dfs(1)
    print('#{} {}'.format(tc, res))

