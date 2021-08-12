import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for case in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if i % 2:
                if li[i] > li[j]:
                    li[i], li[j] = li[j], li[i]
            else:
                if li[i] < li[j]:
                    li[i], li[j] = li[j], li[i]

    print("#{}".format(case + 1), end=" ")
    for k in range(10):
        print(li[k], end=" ")
    print()