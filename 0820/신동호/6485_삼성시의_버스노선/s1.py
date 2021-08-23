import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [0] * 5001
    B = [0] * 5001
    for i in range(N):
        A[AB[i][0]] += 1
        B[AB[i][1]] += 1
    S = [0] * 5001
    for i in range(1, len(S)):
        S[i] = S[i-1] + A[i] - B[i-1]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        print(S[C[i]], end=' ')
    print()