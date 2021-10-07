import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int, input().split())))     # A리스트 정렬해서 받아오기
    B = list(map(int, input().split()))

    result = 0
    for num in B:      # list B에 있는 원소 하나씩 탐색
        s, flag = 0,0  # flag 0:시작 1: 오른쪽 구간 -1: 왼쪽 구간
        e = len(A)-1

        while s <= e:
            m =(s+e)//2

            if num > A[m] and flag != 1:
                s = m + 1
                # m = (s + e) // 2
                flag = 1
            elif num < A[m] and flag != -1:
                e = m - 1
                # m = (s+e)//2
                flag = -1
            elif num == A[m]:
                result += 1
                break

            else:
                break

    print('#{} {}'.format(tc, result))