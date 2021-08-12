import sys
sys.stdin = open('sample_input.txt')

# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split()) # 부분집합 원소의 수 N, 부분 집합의 합 K
    A = list(range(1, 13))
    length_of_A = len(A)
    result = 0

    for i in range(1 << length_of_A):  # A의 부분집합의 개수
        total = 0  # 부분집합의 합을 담을 변수
        count = 0  # 부분집합의 원소의 수를 담을 변수
        for j in range(length_of_A):  # 원소의 수만큼 비트를 비교한다.
            if i & (1 << j):  # i의 j번째 비트가 1이면
                total += A[j]
                count += 1
        if count == N and total == K:   # 부분집합의 합과 갯수가 주어진 N, K와 같다면
            result += 1     # 조건을 만족하는 부분집합 +1

    print('#{} {}'.format(test_case, result))


