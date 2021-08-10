import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):

    # 정수의 개수를 nums, 구간의 길이를 boundary라고 정의하고 입력값을 처리하고
    # 주어진 정수를 num_lists에 저장한다.
    nums, boundary = map(int, input().split())
    num_lists = list(map(int, input().split()))

    # 최솟값의 경우 정수의 최대 개수 = 100, 정수 최댓값 = 10000 이므로 10000 * 100
    max_sum = 0
    min_sum = 1000000

    # idx = 0 ~ nums - boundary까지 확인한다
    # 예시 : 배열의 길이가 10이고(0 1 2 3 4 5 6 7 8 9) boundary가 3인경우 7까지만 확인한다
    for idx in range(0, nums - boundary + 1):

        # 구간합을 temp_sum에 저장한다.
        temp_sum = 0
        for boundary_idx in range(idx, idx + boundary):
            temp_sum += num_lists[boundary_idx]

        # 최대 / 최솟값을 최신화한다.
        if max_sum < temp_sum:
            max_sum = temp_sum
        if min_sum > temp_sum:
            min_sum = temp_sum

    result = max_sum - min_sum
    print("#{} {}".format(tc, result))