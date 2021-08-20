import sys

sys.stdin = open("sample_input.txt")


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n - 1) + 2 * (paper(n - 2))


T = int(input())
for tc in range(0, T):
    N = int(input())
    result = paper(N//10)

    print("#{} {}".format(tc + 1, result))
