import sys
sys.stdin = open('sample_input.txt')

x = int(input())

for tc in range(1, x+1):
    N, Q = map(int, input().split())
    result_li = [0] * N
    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            result_li[j]=i

    print('#{} {}'.format(tc, ' '.join(map(str,result_li))))
