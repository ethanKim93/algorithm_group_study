import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    binary = ''
    result = 'OFF'

    while True:
        a = int(M / 2)
        b = int(M % 2)
        binary += str(b)
        if a != 0:
            M = a
        else:
            binary = binary[::-1]
            break

    cnt = 0
    if len(binary) >= N:
        for i in range(len(binary)-1, len(binary)-N-1, -1):
            cnt += int(binary[i])
        if cnt == N:
            result = "ON"
    print("#{} {}".format(tc + 1, result))