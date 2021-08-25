import sys
sys.stdin = open("sample_input.txt")


def backtracking(row=0, val=0):
    global total
    if row == N:
        total = val
        # print(columns)
        return
    else:
        for col in range(N):
            if check[col]:
                columns[row] = col
                check[columns[row]] = False
                val += num[row][columns[row]]
                if val >= total:
                    val -= num[row][columns[row]]
                    check[columns[row]] = True
                    columns[row] = -1
                    continue
                else:
                    backtracking(row + 1, val)
                    val -= num[row][columns[row]]
                    check[columns[row]] = True
                    columns[row] = -1
        return total


for case in range(int(input())):
    N = int(input())

    num = [list(map(int, input().split())) for _ in range(N)]
    columns = [-1] * N  # 넣을 대상
    check = [True] * N  # index 로 무엇을 넣을 수 있는지

    total = 101

    print("#{} {}".format(case + 1, backtracking()))

