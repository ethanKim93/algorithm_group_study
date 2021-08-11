import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 정수의 개수 N과 구간의 개수 M
    numbers = list(map(int, input().split()))  # N개의 정수 ai

    total_list = [] # 모든 구간합 리스트

    for i in range(N-M+1): # 최대 개수
        temp_total = 0
        for j in range(M): # 구간 선회
            temp_total += numbers[i+j]
        total_list.append(temp_total)

    total_max = total_list[0]  # 구간 합 최대
    total_min = total_list[0]  # 구간 합 최소

    for i in total_list:
        if i > total_max:
            total_max = i
    for i in total_list:
        if i < total_min:
            total_min = i

    result = total_max - total_min
    print('#{} {}'.format(test_case, result))
