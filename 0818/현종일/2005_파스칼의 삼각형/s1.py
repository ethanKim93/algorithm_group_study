import sys
sys.stdin = open("input.txt")

def pascal(N):
    table = [0] * N
    if N == 1:
        table[0] = 1
    else:
        table[0] = 1
        table[N-1] = 1
        for i in range(1, N-1):
            table[i] = pascal(N-1)[i-1] + pascal(N-1)[i]
    return table

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for j in range(1, N+1):
        print(*pascal(j))

