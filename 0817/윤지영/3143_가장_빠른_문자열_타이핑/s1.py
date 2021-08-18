import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    cnt = i = 0
    N, M = len(A), len(B)
    li_a, li_b = list(A), list(B)
    while i < N-M+1:
        if li_b == li_a[i:i+M]:
            for _ in range(i, i+M):
                li_a.pop(i)
            cnt += 1
        else:
            i += 1
    cnt += len(li_a)
    print('#{} {}'.format(tc, cnt))