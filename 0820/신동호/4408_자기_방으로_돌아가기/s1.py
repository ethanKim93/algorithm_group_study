import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    R = [0] * 201

    A = [0] * 201
    B = [0] * 201
    result = 0
    for i in range(N):
        a = (AB[i][0]+1)//2
        b = (AB[i][1]+1)//2
        if a > b:
            a, b = b, a
        A[a] += 1
        B[b] += 1
    for i in range(1, len(R)):
        R[i] = R[i-1] + A[i] - B[i-1]
        if R[i] > result:
            result = R[i]
    print('#{} {}'.format(tc, result))