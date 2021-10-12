import sys
sys.stdin = open("input.txt")


def pick(step=0, total=100.0):
    global work_per
    if total <= work_per:
        return

    if step == N:
        work_per = total
        return

    for i in range(N):
        if check[i]:
            check[i] = False
            pick(step + 1, total * field[step][i] / 100)
            check[i] = True


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * N

    work_per = 0.0
    pick()
    print("#{} {:6f}".format(case + 1, work_per))
