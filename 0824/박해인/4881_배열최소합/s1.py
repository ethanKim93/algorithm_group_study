import sys
sys.stdin = open('sample_input.txt')

def array_min_sum(idx, total):
    global array_sum

    if total > array_sum:  # 유망하지 않다면,
        return

    if idx == N:  # 모든 행이 선택된 경우,
        array_sum = total
        return

    for j in range(N):
        if check[j]:  # 이미 선택한 열이라면 더이상 선택하지 않고 넘어가기
            continue

        check[j] = 1
        total += numbers[idx][j]
        array_min_sum(idx+1, total)

        check[j] = 0
        total -= numbers[idx][j]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    idx = 0  # 선택하려는 행 인덱스
    check = [0 for _ in range(N)] # 열을 선택했는지 기록
    total = 0
    array_sum = 9999999

    array_min_sum(0, 0) # 첫행 total 부터 시작

    print('#{} {}'.format(test_case, array_min_sum(0, 0)))



