import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for case in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for w in range(L - 1, R):
            boxes[w] = i + 1

    print("#{}".format(case + 1), end=" ")
    print(*boxes)