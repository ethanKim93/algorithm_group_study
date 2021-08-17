import sys

sys.stdin = open('sample_input.txt')


def palindrome(word):  # 리스트를 입력받아 회문을 검사하고, 회문이 맞다면 문자열로 변환해 반환.
    return_str = 'a' * 101
    if word == word[::-1]:
        return_str = ''.join(word)
    return return_str


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer = 'a' * 101  # 가장 긴 문자열이 100자
    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j] == arr[i][j + M - 1]:  # 가로줄의 회문여부
                answer = palindrome(arr[i][j:j + M])
            if arr[j][i] == arr[j + M - 1][i]:  # 세로줄의 회문여부
                temp = ''
                for k in range(M):  # 세로줄은 slicing 할 수 없기때문에 임시변수에 저장해서 회문 검사
                    temp += arr[j + k][i]
                answer = palindrome(temp)
        if len(answer) == M:  # answer에 회문 문자열이 입력되었으면 반복문 종료
            break
    print('#{} {}'.format(tc, answer))