import sys
sys.stdin = open('sample_input.txt')


def binarySearch(a, key):
    start = 1
    end = a
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        if middle == key:
            break
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_A = binarySearch(P, A)
    cnt_B = binarySearch(P, B)

    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc, result))


