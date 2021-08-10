import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    now = 0
    result = 0

    while not N <= now + K:
        sub = [stop for stop in stops if now < stop <= now + K]
        try:
            now = sub[-1]
            result += 1
        except:
            result = 0
            break
    print('#{} {}'.format(tc, result))