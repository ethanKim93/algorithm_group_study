import sys

sys.stdin = open('input.txt')


# 보충수업
for tc in range(1, 11):
    L = int(input())
    H = list(map(int, input().split()))
    # print(L)
    # print(buildings)
    ans = 0
    for i in range(2, L - 2):
        maxV = H[i - 2]
        if maxV < H[i - 1]:
            maxV = H[i - 1]
        if maxV < H[i + 1]:
            maxV = H[i + 1]
        if maxV < H[i + 2]:
            maxV = H[i + 2]
        if H[i] > maxV:
            ans += H[i] - maxV
    print('#{0} {1}'.format(tc, ans))

