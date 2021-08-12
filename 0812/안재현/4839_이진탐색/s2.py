import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(T):
    P, A, B = map(int, input().split())

    l1 = l2 = 1
    r1 = r2 = P
    f1 = f2 = False
    while True:
        c1 = int((l1 + r1) / 2)
        c2 = int((l2 + r2) / 2)

        if c1 > A:
            r1 = c1
        elif c1 < A:
            l1 = c1
        else:
            f1 = True

        if c2 > B:
            r2 = c2
        elif c2 < B:
            l2 = c2
        else:
            f2 = True

        if f1 and not f2:
            print("#{} A".format(case + 1))
            break
        if f2 and not f1:
            print("#{} B".format(case + 1))
            break
        if f2 and f1:
            print("#{} 0".format(case + 1))
            break