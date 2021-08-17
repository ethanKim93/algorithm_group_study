import sys
sys.stdin = open('input.txt')
# 회문검사 함수 생성
def is_palindrome(N, M, arr):
    # i행부터 회문 검사 시작
    for i in range(N):
        # 확인할 영역의 시작 인덱스
        # M은 문자열의 길이, N은 배열 한 행의 길이
        # M이 100이면 한 번, 99면 두 번 검사하기 때문
        for j in range(N - M + 1):
            # 이번 영역이 회문이라 가정
            # 나중에 True를 반환하기 위함
            result = 1
            # 회문검사 문자열 길이의 중앙값까지
            # 즉 왼쪽 요소만 검사
            for k in range(M // 2):
                # 왼쪽 요소와 오른쪽 끝 요소를 비교해 나가기
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    # 만약 일치하지 않으면 회문이 아님
                    # 0을 반환해서 False로 만들기
                    result = 0
                    break
            # result값이 True이면(=회문이 있으면) True반환
            if result:
                return True

    # i열부터 시작
    for i in range(N):
        # 확인할 영역의 시작 인덱스
        # M은 문자열의 길이, N은 배열 한 행의 길이
        # M이 100이면 한 번, 99면 두 번 검사하기 때문
        for j in range(N - M + 1):
            # 이번 영역이 회문이라 가정
            # 나중에 True를 반환하기 위함
            result = 1
            # 회문검사 문자열 길이의 중앙값까지
            # 즉 왼쪽 요소만 검사
            for k in range(M // 2):
                # 왼쪽 요소와 오른쪽 끝 요소를 비교해 나가기
                # 위 상황과 인덱스 위치가 바뀜
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    # 만약 일치하지 않으면 회문이 아님
                    # 0을 반환해서 False로 만들기
                    result = 0
                    break
            # result값이 True이면(=회문이 있으면) True 반환
            if result:
                return True


T = 10
for t in range(T):
    # tc 받아오기
    tc = int(input())
    # 입력값 배열로 받아오기
    arr = [str(input()) for _ in range(100)]

    # 반복문을 돌며 문자열의 길이를 M부터 시작
    for M in range(100, 0, -1):
        # 함수값이 True이면(= 문자열 길이 M인 회문이 있으면)
        # 해당 문자열 길이를 그대로 반환
        if is_palindrome(100, M, arr):
            print('#{} {}'.format(tc, M))
            break