import sys
sys.stdin = open('input.txt')


# 조건에 맞는 수를 찾으면 1, 조건에 맞는 수를 찾지 못하면 0을 리턴하는 이진 탐색 함수
def binary_search(n, arr, key):
    low = 0             # 시작 인덱스
    high = n-1          # 끝 인덱스
    before = None       # 이전에 했던 탐색의 방향을 기록하는 변수

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:         # 목표한 값을 찾으면 1을 리턴
            return 1
        elif arr[mid] > key:
            high = mid - 1
            now = 'L'               # 왼쪽을 탐색하면 현재 탐색 방향을 L로 설정
        else:
            low = mid + 1
            now = 'R'               # 오른쪽을 탐색하면 현재 탐색 방향을 R로 설정

        if before == now:           # 이전 탐색 방향과 현재 탐색 방향이 일치하면 0을 리턴
            return 0
        before = now                # 다음 탐색으로 넘어가기 전, 현재 탐색 방향을 이전 탐색 방향에 저장
    return 0                        # 목표한 값을 찾지 못하면 0을 리턴


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))     # A를 입력받은 후, 정렬
    B = list(map(int, input().split()))
    ans = 0
    for num in B:
        ans += binary_search(N, A, num)             # 조건에 맞는 수를 찾을 때마다 ans를 1씩 더한다.
    print('#{} {}'.format(tc, ans))