import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    NQ = list(map(int,input().split()))
    N = NQ[0]
    Q = NQ[1]
    result = [0]*N
    for i in range(1,Q+1):
        LR = list(map(int,input().split()))
        for j in range(LR[0]-1,LR[1]):
            result[j] = i
    print('#{}'.format(tc),end='')
    for i in result:
        print(' {}'.format(i),end='')
    print()

