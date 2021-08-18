import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 개수 T, 1 <= T <= 50

def BruteForce(pattern, target):
    N = len(target)
    M = len(pattern)
    i = 0  # target index
    j = 0  # pattern index
    count = 0

    while j < M and i < N:
        if target[i] != pattern[j]:  # 다르면
            i -= j
            j = -1
        i += 1
        j += 1
        if j == M:  # 검색 성공
            count += 1
            target = target[:i-M] + target[i:]
            i = j = 0  # 초기화 -> 다시 돌 수 있도록
            N = len(target)  # 초기화 -> 다시 돌 수 있도록

    return count

for test_case in range(1, T+1):
    A, B = input().split()  # A: banana  B: bana  A: target B: pattern

    result = 0
    result += BruteForce(B, A)
    result += len(A) - len(B) * BruteForce(B, A)

    print('#{} {}'.format(test_case, result))

