import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    cargo.sort(reverse=True)
    capacity.sort(reverse=True)
    # 역순으로 배열해서 무거운 화물과 적재용량이 큰 트럭 먼저 탐색할 수 있도록 정렬

    result = 0
    i, j = 0, 0
    while i < N and j < M:  # 화물이나 트럭 여분이 있을 때 반복
        if cargo[i] <= capacity[j]:  # 트럭이 화물을 실을 수 있을 때
           result += cargo[i]  # 전체 무게에 더해준다.
            i += 1  # 다음 화물을 탐색
            j += 1  # 다음 트럭을 탐색
        else:
            i += 1 # 트럭이 현재 탐색하고 있는 화물을 싣지 못할 때 다음 화물 탐색

    print('#{} {}'.format(test_case, result))