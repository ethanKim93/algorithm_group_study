import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0
    idx = 0
    while True:
        if len(A[idx:]) < len(B):
            break
    # for idx in range(0, len(A)-len(B)+1):
    #     if len(A[idx:]) < len(B):
    #         break
        if A[idx:idx+len(B)] == B:
            cnt += 1
            idx += len(B)
        else:
            idx += 1
    # print(cnt)

    if cnt == 0:
        print('#{} {}'.format(tc, len(A)))
    else:
        print('#{} {}'.format(tc, len(A) - (len(B)*cnt) + cnt))
