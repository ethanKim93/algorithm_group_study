import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    now = 0
    result = 0
    first = 1
    for stop in stops:
        if stop <= now + K:
            first = 0
            park = stop
        elif first:
            result = 0
            break
        else:
            now = park
            result += 1
            first = 1
    print(result)
