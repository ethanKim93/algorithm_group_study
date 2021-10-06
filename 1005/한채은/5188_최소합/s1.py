from pprint import pprint
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 시작점
            if i == 0 and j == 0:
                continue

            # 첫번째 Column인 경우에는 위에서만 내려올 수 있기 때문에 위의 값을 더해줌.
            if i == 0 and j > 0:
                arr[j][i] += arr[j - 1][i]
            # 첫번째 Row인 경우에는 왼쪽에서만 올 수 있기 때문에 왼쪽의 값을 더해줌.
            elif j == 0 and i > 0:
                arr[j][i] += arr[j][i - 1]
            # 위의 두 경우도 아닐땐 왼쪽과 위쪽 값 중 최소값을 더해줌.
            elif i > 0 and j > 0:
                arr[j][i] += min(arr[j - 1][i], arr[j][i - 1])

    print("#{} {}".format(tc, arr[N - 1][N - 1]))