import sys
from copy import deepcopy
sys.stdin = open('sample_input1.txt')

d = [-1, 1, 0, 0]

def find_top(idx):
    for i in range(H):
        if arr[i][idx]:
            return crush(i, idx, arr[i][idx])
            
def crush(i, j, mv):
    if mv == 1:
        arr[i][j] = 0
    if mv > 1:
        arr[i][j] = 0
        # 상, 하, 좌, 우로 n-1 칸 이동하면서 재귀적으로 분쇄
        for n in range(1, mv):
            for k in range(4):
                ni, nj = i+d[k]*n, j+d[k-2]*n
                if 0 <= ni < H and 0 <= nj < W:
                    crush(ni, nj, arr[ni][nj])
            
def arrange():
    for j in range(W):
        i = pivot = H-1
        while i >= 0:
            # 첫번째 0인 지점을 pivot으로 정하자
            if not arr[i][j]:
                pivot = i
                while i >= 0:
                    # 다음 지점부터 0이 아닌 지점의 위치를 찾고 찾을 시 처음 0의 위치와 자리바꿈
                    if arr[i][j]:
                        arr[pivot][j], arr[i][j] = arr[i][j], arr[pivot][j]
                        # 위치 바꾼 다음자리 부터 수색
                        i = pivot-1
                        break
                    i -= 1
            else:
                i -= 1

def box_count():
    cnt = 0
    for i in range(H):
        cnt += W - arr[i].count(0)
    return cnt

def make_case(k):
    if k == N:
        print(idx_case)
        tot_case.append(idx_case[:])
        return
    for i in range(W):
        idx_case[k] = i
        make_case(k+1)
        idx_case[k] = 0

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = W*H
    # 부술 벽돌의 위치의 모든 경우의 수 다 해보기?!
    # 완전탐색의 경우 W ** N 만큼 ~> 최대 12**4 = 20736번의 경우의 수
    idx_case = [0]*N
    tot_case = []
    make_case(0)
    print(tot_case[:10])
    for case in tot_case:
        arr = deepcopy(org)
        for w in case:
            find_top(w)
            arrange()
        min_cnt = min(min_cnt, box_count())
        if not min_cnt: break   # 다 부순 경우 더 이상 돌 필요 없음
    print('#{} {}'.format(tc, min_cnt))