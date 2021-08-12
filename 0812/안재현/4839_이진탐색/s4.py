import sys

sys.stdin = open('sample_input.txt')


def binary(left, right, target, count):  # 이진탐색 함수정의
    mid = int((left+right)/2)

    if target < mid:
        return binary(left, mid, target, count+1)
    elif target > mid:
        return binary(mid, right, target, count+1)
    else:
        return count

T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    count_a = binary(1, P, A, 0)
    count_b = binary(1, P, B, 0)

    if count_a < count_b:  # cnt가 적으면 빨리한거
        print('#{} A'.format(tc))
    elif count_a > count_b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))


