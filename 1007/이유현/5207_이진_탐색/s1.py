import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for num in B:
        left = 0
        right = N-1
    #     left_cnt = right_cnt = 0
    #
    #     while left <= right:
    #         if abs(left_cnt - right_cnt) == 2:
    #             break
    #
    #         mid = (left + right) // 2
    #         if num == A[mid]:
    #             ans += 1
    #             break
    #
    #         elif num < A[mid]:
    #             right = mid -1
    #             left_cnt += 1
    #             if abs(left_cnt - right_cnt) == 2:
    #                 break
    #
    #         elif num > A[mid]:
    #             left = mid + 1
    #             right_cnt += 1
    #             if abs(left_cnt - right_cnt) == 2:
    #                 break


        # 왼쪽으로 갔는지 오른쪽으로 갔는지 체크하기 위한 용도
        flag = 0
        # 탐색범위가 같아지거나 엇갈릴때까지 반복한다.
        while left <= right:
            # 중간지점의 위치를 구한다.
            mid = (left + right) // 2
            # 중간지점의 값이 정답이라면 answer를 늘리고 반복문을 중지한다.
            if A[mid] == num:
                ans += 1
                break
            # 선택한 인덱스 값이 찾는값보다 크다면
            elif A[mid] > num:
                # 선택한 인덱스 위쪽은 필요없으므로 최대 인덱스 위치를 수정한다.
                right = mid - 1
                # 이전에도 왼쪽을 선택했다면 중지
                if flag == 1: break
                # 왼쪽으로 갔다고 표시한다.
                flag = 1
            else:
                # 반대의 상황이라면 최소값을 바꿔준다.
                left = mid + 1
                # 이전에 오른쪽으로 갔다면 중지
                if flag == -1: break
                # 오른쪽으로 갔다고 표시한다.
                flag = -1

    print('#{} {}'.format(tc, ans))

