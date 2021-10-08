import sys
sys.stdin = open("sample_input.txt")


def pick(step=0, total=0):
    global minimum
    if minimum <= total:
        return

    if step == N:
        minimum = total
        return

    for i in range(N):
        if check[i]:
            check[i] = False
            pick(step + 1, total + field[step][i])
            check[i] = True


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * N

    minimum = 99 * N
    pick()
    print("#{} {}".format(case + 1, minimum))
