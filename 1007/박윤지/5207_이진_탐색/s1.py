# 문제 이해 안됐고... 사람들 코드 참고

import sys
sys.stdin = open('sample_input.txt', 'r')

def binarySearch(n, arr, key):  # n: arr의 길이
    global ans
    low = 0
    high = n-1
    flag = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            ans += 1
            break
        elif arr[mid] > key and flag != -1:
            high = mid - 1
            flag = -1
        elif arr[mid] < key and flag != 1:
            low = mid + 1
            flag = 1
        else:
            break
    return -1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # sorted(): 정렬된 리스트를 반환
                                                  # .sort(): 본체를 정렬하고 None을 반환
    B = list(map(int, input().split()))

    ans = 0

    for b in B:
        binarySearch(N, A, b)

    print('#{} {}'.format(tc, ans))
    
    
###################################################
# 런타임 에러, 문제 이해한 거
# def binary_search(arr, goal):  # arr: 이진탐색할 배열 / goal: 찾을 숫자
#     global left, right, ans
#     if right and left:
#         ans += 1
#         return 1
#
#     l = 0
#     r = len(arr)-1
#     m = (l+r)//2
#
#     if l == r:  # 배열 한 칸 짜리
#         return 0
#     else:
#         if arr[m] < goal:  # 왼쪽 탐색으로
#             left = 1
#             return binary_search(arr[:m], goal)
#         elif arr[m] > goal:  # 오른쪽 탐색으로
#             right = 1
#             return binary_search(arr[m+1:], goal)