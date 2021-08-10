import sys
sys.stdin = open("sample_input.txt")

for tc in range(1,int(input())+1):
    N, Q = map(int, input().split())
    newbox = [0]*N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        newbox[L-1:R] = [i]*(R-L+1)

    print('#{} {}'.format(tc,' '.join(map(str, newbox))))