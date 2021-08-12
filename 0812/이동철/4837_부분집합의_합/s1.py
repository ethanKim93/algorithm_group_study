import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    #부분 집합 만들기
    A_list = []
    for i in range(1 << len(A)):
        A_sub_list = []
        for j in range(len(A)):
            if i & (1 << j):
                A_sub_list.append(A[j])
        A_list.append(A_sub_list)

    #조건 만족시켜주는 for문과 if문
    result = 0
    for i in A_list:
        if len(i) == N and sum(i) == K:
            result += 1
    print('#{} {}'.format(tc, result))

