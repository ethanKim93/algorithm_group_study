import sys

sys.stdin = open('input.txt')


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


for test_case in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]   # 가로줄의 회문을 찾을 배열
    arr2 = [[0]*100 for _ in range(100)]
    for i in range(100):                        # 세로줄의 회문을 찾기 위해 arr의 i,j를 서로 바꿔 동시에 회문을 확인할 수 있도록 한다.
        for j in range(100):
            arr2[i][j] = arr[j][i]

    answer = 0
    for i in range(100):                        # 각 배열의 행
        for j in range(100):                    # 각 배열의 열
            for k in range(100 - j, 0, -1):    # 각 행에서 가장 큰 회문을 찾기 위해 가능한 인덱스의 최대값에서부터 1까지 순회
                if palindrome(arr[i][j:j + k]) or palindrome(arr2[i][j:j+k]):
                    if answer < k:
                        answer = k
                    break
    print('#{} {}'.format(tc, answer))
