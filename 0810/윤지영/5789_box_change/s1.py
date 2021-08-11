import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N,Q = map(int,input().split())
    L = []
    R = []
    for i in range(1,Q+1):
        L_i, R_i = map(int,input().split())
        L.append(L_i)
        R.append(R_i)

    box = [0] * N
    for i in range(1,Q+1):
        for j in range(L[i-1], R[i-1]+1):
            box[j-1] = i

    result = ''
    for i in range(N):
        result = result + str(box[i]) + ' '
    print('#{} {}'.format(tc, result))