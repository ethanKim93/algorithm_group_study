import sys
sys.stdin = open("sample_input.txt")


def dp():
    for i in range(1, N):
        energy = st[i]
        for step in range(energy):
            try:
                change[i + step] = min(change[i + step], change[i - 1] + 1)
            except IndexError:
                return

        if change[-1] != N:
            return


for case in range(int(input())):
    st = list(map(int, input().split()))
    N = st[0]
    change = [N] * N
    change[0] = -1
    dp()

    print("#{} {}".format(case + 1, change[-1]))
