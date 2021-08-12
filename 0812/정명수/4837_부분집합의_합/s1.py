import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int, input().split())

    numbers = list(range(1,13))
    coms = []                          #부분 집합
    for i in range(1<<12):
        com = []
        for j in range(12):
            if i & (1<<j):
                com.append(numbers[j])
        coms.append(com)               # 부분집합으로 이루어진 집합
    answer = 0
    for sources in coms:               # 각 부분집합 대입
        source_sum = 0
        for i in sources:                               #부분집합의 합 구하기
            source_sum += i
        if source_sum == K and len(sources) == N:       # 조건에 맞는 집합만큼 +
            answer += 1
    print('#{} {}'.format(test_case, answer))



