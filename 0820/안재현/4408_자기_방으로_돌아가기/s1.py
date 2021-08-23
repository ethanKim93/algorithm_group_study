import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(0, T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201
    for i in room:
        if i[0] < i[1]:
            s = (i[0] + 1) // 2
            e = (i[1] + 1) // 2
        else:
            e = (i[0] + 1) // 2
            s = (i[1] + 1) // 2

        for j in range(s, e+1):
            cnt[j] += 1

    result = 0
    for j in range(len(cnt)):
        if result < cnt[j]:
            result = cnt[j]

    print("#{} {}".format(tc + 1, result))