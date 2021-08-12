import sys
sys.stdin = open('sample_input.txt')

def binary_search(left, right, target, count):
    mid = int((left+right)/2)

    if target < mid:
        return binary_search(left, mid, target, count+1)
    elif target > mid:
        return binary_search(mid, right, target, count+1)
    else:
        return count


T = int(input())

for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    count_a = binary_search(1, P, Pa, 0)
    count_b = binary_search(1, P, Pb, 0)

    if count_a > count_b:
        result = 'B'
    elif count_a < count_b:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(t, result))