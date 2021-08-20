import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    st = list(input())

    i = 0
    while i < len(st) - 1:
        if st[i] == st[i + 1]:
            del(st[i])
            del(st[i])
            i = -1
        i += 1

    print("#{} {}".format(case + 1, len(st)))