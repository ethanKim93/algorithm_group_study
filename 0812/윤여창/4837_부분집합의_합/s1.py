import sys
sys.stdin = open('sample_input.txt')
                                        ## 조원들 도움으로 풀었습니다.
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
        for j in range(len(A)):
            if i & (1<<j):
                cnt += 1
                sum_result += A[j]
        if cnt == N and sum_result == K:
            result += 1
    print('#{} {}'.format(tc,int(result)))