import sys
sys.stdin = open("input.txt")

# 실패코드

def select_worker():
    global tmp, n_height
    if n_height > tmp:
        return

    if n_height >= height:
        if n_height < tmp:
            tmp = n_height
        return

    for idx in range(N):
        if not used[idx]:
            used[idx] = 1
            n_height += workers[idx]
            select_worker()
            n_height -= workers[idx]
            used[idx] = 0


for tc in range(1, int(input())+1):
    N, height = map(int, input().split())
    workers = list(map(int, input().split()))
    tmp = 987654321
    used = [0] * N
    n_height = 0

    select_worker()
    print('#{} {}'.format(tc, tmp-height))
