import sys
sys.stdin = open('s_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    roots = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    result = [0] * 5001
    for i in range(len(roots)):
        for j in range(roots[i][0], roots[i][0] + abs(roots[i][0] - roots[i][1]) + 1):
            result[j] += 1

    print("#{}".format(test_case), end=" ")
    for i in range(P):
        print(result[C[i]], end=" ")
    print()