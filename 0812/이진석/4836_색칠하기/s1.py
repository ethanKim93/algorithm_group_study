import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    reds = [[0] * 10 for _ in range(10)]
    blues = [[0] * 10 for _ in range(10)]
    answer = 0
    for _ in range(N):
        infor = list(map(int, input().split()))
        if not (infor[4] - 1):  # red
            for i in range(infor[1], infor[3] + 1):
                for j in range(infor[0], infor[2] + 1):
                    reds[i][j] = 1
        else:  # blue
            for i in range(infor[1], infor[3] + 1):
                for j in range(infor[0], infor[2] + 1):
                    blues[i][j] = 1

    for i in range(10):
        for j in range(10):
            if reds[i][j] and blues[i][j] == reds[i][j]:
                answer += 1

    print('#{} {}'.format(tc, answer))
