import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N, Q = map(int, input().split())
    answer = [0]*N
    for j in range(1, Q+1):
        L, R = map(int, input().split())
        for k in range(L,R+1):
            answer[k-1] = j
    print('#{}'.format(i+1), end=' ')
    print(*answer)