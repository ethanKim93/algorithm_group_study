import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb
    Plist = list(range(1, P+1)) # 1 부터 P까지 수를 원소로 갖는 Plist
    start = 0
    end = len(P)-1

    counta = 0  # A의 탐색 횟수
    countb = 0  # B의 탐색 횟수

    while start <= end:
        middle = (start + end) // 2 # 그냥 /만 쓰면 정수가 안나올 수 있으니까 몫만 반환하는 //
        if Plist[middle] == Pa: # A의 검색 성공
            print('A')
        elif a[middle] > key:
            end = middle - 1 # end를 중간 -1 다음 인덱스로 바꿔주면서 middle 이후 구간을 모두 버림
        else:
            start = middle + 1 # start를 중간 + 1 다음 인덱스로 바꿔주면서 middle 이전 구간을 모두 버림
    return -1 # 검색 실패