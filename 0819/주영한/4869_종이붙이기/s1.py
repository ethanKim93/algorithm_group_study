import sys
sys.stdin = open("sample_input.txt")

T = int(input())
dp = [1] * 50
dp[1] = 3

for tc in range(1, T + 1):
    N = int(input()) // 10
    for idx in range(2, N):
        # 현재 경우는 직전의 경우에 세로로 타일을 하나 붙이는 경우와
        # 2차례 전의 경우에 가로로 배열된 타일 2개나 정사각형 타일을 붙이는 경우로 구성된다.
        dp[idx] = dp[idx -1] + dp[idx - 2] * 2
    print("#{} {}".format(tc, dp[N - 1]))