import sys
sys.stdin = open("input.txt")

for case in range(10):
    N, st = input().split()
    st = list(st)

    i = 0
    while i < len(st) - 1:
        if st[i] == st[i + 1]:
            del(st[i])
            del(st[i])
            i = -1
        i += 1

    print("#{} {}".format(case + 1, ''.join(st)))
