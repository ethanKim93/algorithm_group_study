import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    n, q = map(int, input().split())  # 상자 수: n, Case: q
    maps = [0] * n  # 상자 map

    for i in range(1, q + 1):
        l, r = map(int, input().split())

        for x in range(l - 1, r):  # 상자 index start = 0, Input start = 1
            maps[x] = i

        # maps 요소들 str로 변환 뒤, join으로 list형식 벗어나기
    print("#{} {}".format(tc, " ".join(map(str, maps))))
