from itertools import combinations
import sys
sys.stdin = open('sample_input.txt')


def comb(arr):
    result = []
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            result.append((arr[i], j))
    return result


def happy(arr, case):
    res = 0
    for f1, f2 in comb(case):
        res += arr[f1][f2] + arr[f2][f1]
    return res


T = int(input())
for tc in range(T):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    res = 40000
    for case in combinations(range(n), n//2):
        another = list(set(range(n)) - set(case))
        res1 = happy(arr, case)
        res2 = happy(arr, another)
        if res > abs(res1-res2):
            res = abs(res1-res2)
    print('#{} {}'.format(tc + 1, res))