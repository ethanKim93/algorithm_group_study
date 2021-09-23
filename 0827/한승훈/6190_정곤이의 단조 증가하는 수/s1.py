import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    max_ij = -1
    for i in range(N-1):  # Ai * Aj를 num 리스트에 넣기
        for j in range(i+1, N):
            A_ij = A[i] * A[j]
            str_A = str(A_ij)
            for k in range(len(str_A)-1):
                if str_A[k] > str_A[k+1]:
                    break
            else:
                if max_ij < A_ij:
                    max_ij = A_ij

    print('#{} {}'.format(tc, max_ij))


