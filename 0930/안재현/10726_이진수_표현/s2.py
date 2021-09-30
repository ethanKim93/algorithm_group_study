import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    binary = format(M, 'b')
    result = 'OFF'
    cnt = 0
    if len(binary) >= N:
        for i in range(len(binary) - 1, len(binary) - N - 1, -1):
            cnt += int(binary[i])
        if cnt == N:
            result = "ON"
    print("#{} {}".format(tc + 1, result))
