import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')
# 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
def BruteForce(target, pattern):
    M = len(pattern)
    N = len(target)
    i = 0 # target index
    j = 0 # pattern index
    count = 0

    while j < M and i < N:
        if target[i] != pattern[j]: # 다르면
            i -= j
            j = -1
        i += 1
        j += 1
        if j == M:  # 검색 성공
            count += 1
            j = 0

    return count


for _ in range(1, 11): # 테스트케이스 10개 고정
    test_case = int(input())
    pattern = input()
    target = input()

    print('#{} {}'.format(test_case, BruteForce(target, pattern)))