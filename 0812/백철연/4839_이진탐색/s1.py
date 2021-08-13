
def binary_search(page, key):
    start = 1
    end = page
    middle = 0
    count = 1
    while key != middle:
        middle = int((start + end) // 2)
        if middle > key:
            end = middle - 1
        else:
            start = middle + 1
        count += 1
    return count
# 어제 수업의 이진탐색 교안을 바탕으로 이진탐색 함수 생성!

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

start = 1

for tc in range(1, T+1):
    r, c1, c2 = map(int, input().split())
    #print(r, c1, c2)
    A = binary_search(r, c1)
    B = binary_search(r, c2)
    result = 0
    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(tc, result))

