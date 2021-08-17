import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    cnt = 0
    idx = 0
    while True:
        if A[idx:idx+len(B)] == B:
            cnt += 1
            idx += len(B)

        elif idx > len(A)-len(B):
            cnt += len(A) - idx
            break

        else:
            idx += 1
            cnt += 1
    print('#{} {}'.format(tc, cnt))