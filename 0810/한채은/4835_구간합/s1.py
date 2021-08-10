import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    maxi = 0
    mini = 999999

    for i in range(N-M+1):  # M개의 합 비교 횟수만큼 (N-M+1)반복
        total = 0
        for j in range(i, M+i): # M개의 합을 구하기
            total = total + L[j]

        if total > maxi:    # max값 구하기
            maxi = total

        if total < mini:    # min값 구하기
            mini = total

    print('#{} {}'.format(tc, maxi - mini))