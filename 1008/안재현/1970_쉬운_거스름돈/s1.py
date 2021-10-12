import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    RN = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    R = [0] * len(RN)

    for i in range(len(RN)):
        if N // RN[i] != 0:
            R[i] = N // RN[i]
            N = N % RN[i]
    print("#{}".format(tc + 1))
    print("{}".format(" ".join(map(str, R))))
