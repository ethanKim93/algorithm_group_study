import sys

sys.stdin = open("s_input.txt")


T = int(input())

for a in range(0, T):
    N = int(input())
    ab = []
    empty = []
    for i in range(0, N):
        A, B = map(int, input().split())
        ab.append([A, B])
    P = int(input())
    for j in range(0, P):
        c = int(input())
        cnt = 0
        for k in range(len(ab)):
            if ab[k][0] <= c <= ab[k][1]:
                cnt += 1
        empty.append(str(cnt))

    print('#{}'.format(a + 1), end='')
    for s in range(len(empty)):
        print(' {}'.format(empty[s]), end='')
    print()

