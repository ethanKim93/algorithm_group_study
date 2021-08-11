import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # N X N 배열을 생성한다.
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 결과값에 해당하는 total을 정의한다.
    total = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                temp_sum = 0
                ti = i + di
                tj = j + dj
                # 각 이동 후 인덱스가 배열 내부에 있는지 확인하고, 외부에 있을 경우
                # continue로 무시한다.
                if ti < 0 or ti > (N-1) or tj < 0 or tj > (N-1):
                    continue

                # 배열 내부에 있을 경우, 이웃한 값과 해당 요소의 차의 절대값을 구하고 이를 total에 합한다.
                temp_sum = arr[ti][tj] - arr[i][j]
                if temp_sum < 0:
                    temp_sum = - temp_sum
                total += temp_sum

    print("# {} {}".format(tc, total))
