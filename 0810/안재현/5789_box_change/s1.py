import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for a in range(0, T):
    N, Q = map(int, input().split())
    result = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            result[j] = i
    print("#{}".format(a+1), end=" ")
    print(*result)