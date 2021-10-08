import sys
sys.stdin = open("sample_input.txt")


def half(start, end, val, LR="X"):
    if end - start <= 0:
        return 0

    m = (start + end - 1) // 2

    if A[m] > val:
        return half(start, m, val, "L") if LR != "L" else 0
    elif A[m] < val:
        return half(m + 1, end, val, "R") if LR != "R" else 0
    else:
        return 1


for case in range(int(input())):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    total = 0
    for num in B:
        total += half(0, N, num)

    print("#{} {}".format(case + 1, total))
