import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binarySearch(page, key):
    start = 1
    end = page
    count = 0   # 탐색 횟수를 담을 변수

    while start <= end:
        count += 1 # 탐색 횟수 추가
        middle = (start + end) // 2 # 그냥 /만 쓰면 정수가 안나올 수 있으니까 몫만 반환하는 //
        if middle == key: # 검색 성공
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    return count

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())  # 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb

    count_A = binarySearch(P, Pa)  # A의 탐색 횟수
    count_B = binarySearch(P, Pb)  # B의 탐색 횟수

    if count_B < count_A:  # B의 탐색횟수가 더 적다면
        result = "B"
    elif count_A < count_B:  # A의 탐색횟수가 더 적다면
        result = "A"
    else:
        result = 0

    print('#{} {}'.format(test_case, result))