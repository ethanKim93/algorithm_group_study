import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        front, rare = 0, N-1
        flag = 0
        while front <= rare:
            mid = (front+rare)//2

            if A[mid] == b:  # 일치할 때 -> 찾았다!
                cnt += 1
                break
            elif b < A[mid]:  # B의 원소가 A 리스트 중간값보다 작을 때
                rare = mid-1
                if flag == -1:  # 지난 탐색에서 왼쪽 구간을 선택했었는데 또 왼쪽을 탐색하게 되면 while문 탈출해서 다음 원소 탐색
                    break
                flag = -1  # flag = -1 '왼쪽'이라는 뜻
            else:  # B의 원소가 A 리스트 중간값보다 클 때
                front = mid+1
                if flag == 1:  # 지난 탐색에서 오른쪽 구간을 선택했었는데 또 오른쪽을 탐색하게 되면 while문 탈출해서 다음 원소 탐색
                    break
                flag = 1  # flag = 1 '오른쪽'이라는 뜻

    print('#{} {}'.format(test_case, cnt))