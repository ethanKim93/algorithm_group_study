import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 파리의 수가 담긴 arr를 정의한다.
    arr = [0] * N
    for row in range(N):
        arr[row] = list(map(int, input().split()))

    # 최대 파리 수를 담을 fly_num을 정의한다.
    fly_num = 0

    # 파리채가 칠 수 있는 범위 내에서 순회를 돈다.
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            # 파리채가 쳤을 때 죽는 파리 수를 저장하는 임시 변수 temp_fly_num을 선언한다.
            temp_fly_num = 0
            for dr in range(M):
                for dc in range(M):
                    temp_fly_num += arr[row+dr][col+dc]

            #fly_num을 업데이트 한다.
            if temp_fly_num > fly_num:
                fly_num = temp_fly_num

    print("#{} {}".format(tc, fly_num))