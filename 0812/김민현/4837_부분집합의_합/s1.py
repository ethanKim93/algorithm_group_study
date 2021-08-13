import sys
sys.stdin = open('sample_input.txt')

T = int(input())
A = []
for i in range(1,13):
    A.append(i)

for tc in range(1,T+1):
    N,K = map(int, input().split())
    result = 0
    for i in range(1 << len(A)):
        sum_result = 0
        cnt = 0
        #str_result = '' #debug
        for j in range(len(A)):
            if i & (1<<j):
                cnt += 1
                sum_result += A[j]
                #str_result += str(A[j])+' '#debug
        if cnt == N and sum_result == K:
            result += 1
            #print(str_result)
            #print()
    print('#{} {}'.format(tc,int(result)))

