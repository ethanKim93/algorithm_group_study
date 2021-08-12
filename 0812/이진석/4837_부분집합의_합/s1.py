import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    A = [n for n in range(1, 13)]
    subsets = []  # A의 부분집합 리스트
    answer = 0
    for i in range(1, 1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(A[j])
        subsets.append(temp)
    N, K = map(int, input().split())

    for subset in subsets:  # 부분집합 각각을 순회
        if len(subset) == N:    # 부분집합의 원소의 갯수가 N개 일때
            temp = 0
            for elem in subset: # 부분집합의 원소의 합 저장
                temp += elem
            if temp == K:       # 부분집합의 원소의 합이 K 이면 카운트
                answer += 1
    print('#{} {}'.format(tc, answer))