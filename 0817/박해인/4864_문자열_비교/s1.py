import sys
sys.stdin = open('sample_input.txt')
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수 T, 1 <= T <= 50

def BruteForce(pattern, target):
    N = len(target)
    M = len(pattern)
    i = 0 # target index
    j = 0 # pattern index

    while j < M and i < N:
        if target[i] != pattern[j]:  # 다르면
            i -= j
            j = -1
        i += 1
        j += 1

    if j == M:  # 검색 성공
        return 1
    else:
        return 0

for test_case in range(1, T+1):
    str1 = input().rstrip()  # 공백 제거
    str2 = input().rstrip()

    print('#{} {}'.format(test_case, BruteForce(str1, str2)))

