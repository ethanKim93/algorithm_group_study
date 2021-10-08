import sys
sys.stdin = open('sample_input.txt', 'r')


def binary_search(arr, left, right, result):
    global flag
    start = left
    end = right
    mid = (left + right) // 2

    if left > right:
        return False

    if result >= arr[mid]:
        if arr[mid] == result:
            return True
        if flag == "R":
            return False
        flag = "R"
        start = mid + 1

    elif arr[mid] > result:
        if flag == "L":
            return False
        flag = "L"
        end = mid - 1

    return binary_search(arr, start, end, result)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 A에 속한 정수의 갯수
    # M은 B에 속한 정수의 갯수
    N_arr = sorted(list(map(int, input().split())))
    # 탐색할 배열은 정렬을 해둬야한다...ㅂㄷㅂㄷ
    M_arr = list(map(int, input().split()))

    answer = 0

    for num in M_arr:
        flag = 0
        if binary_search(N_arr, 0, N - 1, num):
            answer += 1

    print('#{} {}'.format(tc, answer))


# # 박해인 (대표코드)
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     A = sorted(list(map(int, input().split())))
#     B = list(map(int, input().split()))
#     cnt = 0
#
#     for b in B:
#         front, rare = 0, N-1
#         flag = 0
#         while front <= rare:
#             mid = (front+rare)//2
#
#             if A[mid] == b:
#                 # 일치할 때 -> 찾았다!
#                 cnt += 1
#                 break
#             elif b < A[mid]:
#                 # B의 원소가 A 리스트 중간값보다 작을 때
#                 rare = mid-1
#                 if flag == -1:
#                     # 지난 탐색에서 왼쪽 구간을 선택했었는데 또 왼쪽을 탐색하게 되면 while문 탈출해서 다음 원소 탐색
#                     break
#                 flag = -1
#                 # flag = -1 '왼쪽'이라는 뜻
#             else:
#                 # B의 원소가 A 리스트 중간값보다 클 때
#                 front = mid+1
#                 if flag == 1:
#                     # 지난 탐색에서 오른쪽 구간을 선택했었는데 또 오른쪽을 탐색하게 되면 while문 탈출해서 다음 원소 탐색
#                     break
#                 flag = 1
#                 # flag = 1 '오른쪽'이라는 뜻
#
#     print('#{} {}'.format(test_case, cnt))