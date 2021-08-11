import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    box = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = i

    print("#{} {}".format(tc, ' '.join(map(str, box))))
