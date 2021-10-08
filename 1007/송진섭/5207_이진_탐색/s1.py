import sys
sys.stdin = open('sample_input.txt')


def binary_search(a_list, target):
    n = len(a_list)
    res = 0
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end) // 2
        if a_list[mid] == target:
            return res
        elif a_list[mid] > target:          # 왼쪽
            if res == -1:
                return -10
            end = mid - 1
            res = -1
        else:                               # 오른쪽
            if res == 1:
                return -10
            start = mid + 1
            res = 1
    res = -10
    return res


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_list = sorted(list(map(int, input().split())))
    B_list = list(map(int, input().split()))
    cnt = 0
    for i in B_list:
        result = binary_search(A_list, i)
        if result == 0 or result == 1 or result == -1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))



