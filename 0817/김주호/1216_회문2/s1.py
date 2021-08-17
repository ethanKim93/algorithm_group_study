import sys
sys.stdin = open("input.txt")

for case in range(10):
    N = int(input())

    li = [input() for _ in range(100)]

    ans = 0
    for area in range(100, -1, -1):
        for i in range(100):
            row_col = ["", ""]
            for j in range(100 - area + 1):
                row_col[0] = li[i][j: j + area]
                row_col[1] = ''.join([row[i] for row in li[j: j + area]])

                for rc in row_col:
                    if rc == rc[::-1]:
                        ans = area
                        break
                if ans:
                    break
            if ans:
                break
        if ans:
            break

    print("#{} {}".format(N, ans))