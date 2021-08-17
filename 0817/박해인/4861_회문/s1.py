import sys
sys.stdin = open('sample_input.txt')

T = int(input())
def isPalindrome(N, M, arr):

    result = ''

    # 행 검사
    for row in range(N):
        for col in range(N-M+1):  # M만큼 확인을 해야하므로 N-M
            for i in range(M//2):
                if arr[row][col+i] != arr[row][col+M-1-i]:
                    break
            else:
                result = arr[row][col:col+M]

    # 열 검사
    for row in range(N):
        for col in range(N-M+1):
            for i in range(M // 2):
                if arr[col+i][row] != arr[col+M-1-i][row]:
                    break
            else:
                for j in range(col, col+M):
                        result += arr[j][row]

    return result

for test_case in range(1, T+1):
    N, M = map(int, input().split())  #  NxN 크기의 글자판, 길이가 M
    arr = [input() for _ in range(N)]  # 2차원 배열말고 리스트 내 str으로 받기

    print('#{} {}'.format(test_case, isPalindrome(N, M, arr)))