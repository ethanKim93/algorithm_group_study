import sys
sys.stdin = open("sample_input.txt")

T = int(input())

#1 ~ 12까지의 배열을 생성한다.
num_lists = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    # 1 ~ 12까지 가능한 모든 부분집합의 케이스를 확인한다.
    for case in range(1, 1 << 12):

        # 부분집합의 원소의 갯수를 의미하는 check_time과 부분집합의 합을 의미하는 subset_sum을 정의한다.
        check_time = 0
        subset_sum = 0

        # 1 ~ 12까지의 배열의 각 원소가 부분집합의 케이스 내에 포함되는지 확인한다.
        for elem in range(12):
            if case & (1 << elem) != 0:
                # 포함된다면 부분집합의 원소의 갯수와 부분집합의 합을 업데이트한다.
                check_time += 1
                subset_sum += num_lists[elem]

        # 만약 부분집합의 원소의 갯수가 N이고 그 합이 K일 경우, 가능한 경우를 의미하는 result에 1을 더해준다.
        if check_time == N and subset_sum == K:
            result += 1
    print("#{} {}".format(tc, result))