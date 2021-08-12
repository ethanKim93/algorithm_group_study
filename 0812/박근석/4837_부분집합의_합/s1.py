import sys
sys .stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # arr = list(map(int, input().split()))
    # n = len(arr)
    A = range(1, 13)


    for i in range(1<<len(A)):
        part = 0
        count = 0
        for j in range(len(A)):
            if i & (1<<j):
                part += A[j]
                count += 1
        if part == K and count == N and i != 0:
            result = 1
            break
    else:
        result = 0

    print('#{} {}'.format(tc, result))
