import sys

sys.stdin = open('sample_input.txt')


def binary(Page, key):  # 이진탐색 함수정의
    start = 1
    end = Page
    cnt = 0  # 승패결정값
    while start <= end:
        mid = (start + end) // 2
        if mid == key:  # 찾을값 발견
            break
        elif mid > key:  # 범위줄여
            end = mid  # 주어진값으로 해야하기 때문
            cnt += 1
        else:
            start = mid  # 범위줄여
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    if binary(P, A) < binary(P, B):  # cnt가 적으면 빨리한거
        print('#{} A'.format(tc))
    elif binary(P, A) > binary(P, B):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
