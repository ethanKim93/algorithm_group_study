import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0
    for i in range(len(A)-len(B)+1):
        if A[i:i+len(B)] == B:
            cnt += 1

    min_cnt = len(A) - len(B)*cnt + 1
    print(min_cnt)

    # print('#{} {}'.format(tc, min_cnt))
