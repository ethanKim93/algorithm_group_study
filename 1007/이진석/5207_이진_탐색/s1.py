import sys
sys.stdin = open('sample_input.txt')

def binary_search(arr, l, r, target):   # 이진탐색
    vector = 0                          # 직전 탐색 기준으로 어느 방향을 탐색중인지 체크할 변수
    while l <= r:                       # 유효한 인덱스일때
        m = (l + r) // 2                # 중심 원소 인덱스
        if arr[m] == target:            # target number를 찾았을 때 True 리턴
            return True
        elif arr[m] > target:           # target이 왼쪽에 있을 때 > 왼쪽 추가탐색
            r = m - 1                   # 오른쪽 끝 갱신
            if vector == 'l':           # 왼쪽을 검색중이었다면 False리턴 (배열에서 가장 작은 숫자보다 target이 작음)
                return False
            vector = 'l'                # 오른쪽을 탐색중이었다면 방향 갱신
        elif arr[m] < target:           # target이 오른쪽에 있을 때 > 오른쪽 추가탐색
            l = m + 1                   # 왼쪽 끝 갱신
            if vector == 'r':           # 오른쪽을 검색중이었다면 False리턴
                return False
            vector = 'r'                # 오른쪽 끝 갱신
    return False

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) # 정렬된 배열
    B = list(map(int, input().split()))         # 확인할 배열
    cnt = 0

    for num in B:
        if binary_search(A, 0, N-1, num):       # True 리턴시 카운트
            cnt += 1
    print('#{} {}'.format(tc, cnt))