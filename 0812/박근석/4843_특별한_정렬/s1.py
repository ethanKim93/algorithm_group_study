import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(len(A)-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    new_list = []
    for i in range(5):
        new_list.append(A[N-1-i])
        new_list.append(A[0+i])

    result = " ".join(map(str, new_list))
    print('#{} {}'.format(tc, result))
