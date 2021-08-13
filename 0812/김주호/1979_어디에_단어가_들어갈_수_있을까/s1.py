import sys
sys.stdin = open("input.txt")


def check(blank, cnt):
    if blank == cnt:
        return 1
    return 0


T = int(input())
for case in range(T):
    N, K = map(int, input().split())

    li = []
    for _ in range(N):
        li.append((list(map(int, input().split()))))

    total = 0
    for i in range(N):
        row_blank = 0
        col_blank = 0

        for j in range(N):
            if li[i][j]:
                row_blank += 1

            else:
                total += check(row_blank, K)
                row_blank = 0

            if li[j][i]:
                col_blank += 1

            else:
                total += check(col_blank, K)
                col_blank = 0

        total += check(row_blank, K)

        total += check(col_blank, K)

    print("#{} {}".format(case + 1, total))