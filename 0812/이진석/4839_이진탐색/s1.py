import sys

sys.stdin = open('sample_input.txt')

def binary_check(start, end, target):
    cnt = 0
    while start <= end:
        middle = (end + start) // 2
        if target == middle:
            cnt += 1
            return cnt
        elif target > middle:
            start = middle
            cnt += 1
        else:
            end = middle
            cnt += 1
    return False

for tc in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())
    result_a = binary_check(1, P, Pa)
    result_b = binary_check(1, P, Pb)

    if result_a < result_b:
        print('#{} A'.format(tc))
    elif result_a > result_b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
