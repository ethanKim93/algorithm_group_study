# 검색함. 이해중...
import sys
sys.stdin = open('sample_input.txt')


def checkDesserts(sr, sc, left, right):
    global MAX
    cafe = [0] * 101
    cnt = 0
    lr = sr + left
    lc = sc - left
    rr = sr + right
    rc = sc + right
    br = sr + left + right
    bc = sc + right - left

    for dis in range(1, left + 1):
        if cafe[A[sr + dis][sc - dis]]:
            return
        cafe[A[sr + dis][sc - dis]] = 1
        if cafe[A[br - dis][bc + dis]]:
            return
        cafe[A[br - dis][bc + dis]] = 1
        cnt += 2

    for dis in range(1, right + 1):
        if cafe[A[lr + dis][lc + dis]]:
            return
        cafe[A[lr + dis][lc + dis]] = 1
        if cafe[A[rr - dis][rc - dis]]:
            return
        cafe[A[rr - dis][rc - dis]] = 1
        cnt += 2

    MAX = max(MAX, cnt)


def makeDistance(sr, sc):
    for left in range(1, sc + 1):
        for right in range(1, N - sc):
            if sr + left + right > N - 1:
                continue
            checkDesserts(sr, sc, left, right)


T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    MAX = -1
    for sr in range(N - 2):
        for sc in range(1, N - 1):
            makeDistance(sr, sc)

    print("#{} {}".format(tc + 1, MAX))
