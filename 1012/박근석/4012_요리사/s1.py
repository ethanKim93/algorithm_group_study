import sys
sys.stdin = open('input.txt')
from itertools import combinations

def cook(arr, case):
    r = 0
    for f1, f2 in combinations(case,2):
        r += arr[f1][f2] + arr[f2][f1]
    return r

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for i in range(n)]

    res = 40000
    for c1 in combinations(range(n), n//2):
        c2 = list(set(range(n)) - set(c1))
        r1 = cook(matrix, c1)
        r2 = cook(matrix, c2)
        if res > abs(r1-r2):
            res = abs(r1-r2)

    print('#{} {}'.format(tc, res))