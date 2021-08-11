import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    flag = False

    # 전체 집합을 input_lists로 정의한다.
    input_lists = list(map(int, input().split()))

    # 공집합이 아닌 모든 부분집합에 대해 고려해본다.
    for case in range(1, 1<<len(input_lists)):
        temp_sum = 0

        # 공집합이 아닌 부분집합 내에 포함되는 원소들을 temp_sum에 더해준다
        # 이 과정은 부분집합의 합을 구하는 과정이다.
        for i in range(len(input_lists)):
            if case & (1 << i):
                temp_sum += input_lists[i]

        # 부분집합의 합이 0일 경우 반복문을 종료한다.
        if temp_sum == 0:
            flag = True
            break

    print("#{} {}".format(tc, int(flag)))
