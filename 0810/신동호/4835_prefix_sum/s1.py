import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    for ind in range(N-M+1):
        sum_part = 0
        if not ind:
            for number in numbers[ind:ind+M]:
                sum_part += number
                max_ns = min_ns = sum_part
        else:
            for number in numbers[ind:ind + M]:
                sum_part += number
            if sum_part > max_ns:
                max_ns = sum_part
            if sum_part < min_ns:
                min_ns = sum_part

    print('#{} {}'.format(tc, max_ns - min_ns))
