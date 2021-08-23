import sys
sys.stdin=open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append(list(range(A, B+1)))
    P = int(input())
    C = []
    for i in range(P):
        C.append(int(input()))

    result = [0] * P
    for i in range(N):
        for j in range(len(AB[i])):
            for k in range(P):
                if AB[i][j] == C[k]:
                    result[k] += 1

    print('#{} '.format(tc), end='')
    print(*result, sep=' ')