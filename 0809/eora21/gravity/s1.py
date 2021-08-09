import sys
sys.stdin = open("input.txt")

T = int(input())

for case in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    # print(li)
    h_li = sorted(list(set(li)), reverse=True)
    total = 0
    for c in range(len(h_li)):
        g = N - 1
        for i in range(N - 1, -1, -1):
            if li[i] >= h_li[c] and total < g:
                drop = g - i
                if drop > total:
                    total = drop
                g -= 1

    print("#{} {}".format(case + 1, total))