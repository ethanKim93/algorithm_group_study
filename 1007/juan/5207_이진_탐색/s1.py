def binary_search():
    global A, cnt
    left,right = 0,N-1
    before = None                   # 탐색전 상태 초기화
    while left <= right:            # 탐색 종료 조건
        mid = (left+right)//2
        if i == A[mid]:             # 탐색 성공
            cnt += 1                # 이 분기를 탔다는건 지금까지 이진 탐색의 좌우영역을 번갈아가며 탐색했다는 의미
            return
        elif i < A[mid]:            # 대상이 왼쪽 영역에 있는 경우
            right = mid-1           # 오른쪽 경계를 mid-1 로 갱신
            now = 'L'               # 이번에 왼쪽 영역을 탐색했음 을 기록
        else:                       # 대상이 오른쪽 영역에 있는 경우
            left = mid+1            # 왼쪽 경계를 mid+1 로 갱신
            now = 'R'               # 이번에 오른쪽 영역을 탐색했음 을 기록
        if now == before:           # 이전 탐색기록과 이번 탐색기록 이 일치하면 탐색 중단
            return
        before = now                # 위에서 리턴되서 종료되지 않았다면 이번 탐색기록을 이전 탐색기록에 저장


import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    cnt = 0
    A = sorted(list(map(int, input().split())))     # 이진 탐색 해야 하는 배열은 정렬
    B = list(map(int, input().split()))
    for i in B:
        binary_search()                             # B의 요소들을 순회하며 이진 탐색 함수 호출
    print('#{} {}'.format(tc, cnt))