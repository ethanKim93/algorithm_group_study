import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(0, T):
    R = input()
    A = input()
    C = ''
    count = 0   # M 문자열이 N 문자열 일부와 동일한지 체크
    search = 0  # while문을 돌리기 위한 값
    while search + len(R) <= len(A):
        for i in range(len(R)):
            C += A[i + search]  # C에 R의 길이만큼 A를 잘라서 넣는다.
        if C == R:
            count = 1           # 동일할 경우 count를 1로 변경
            search += 1
            C = ''
        else:
            search += 1         # 동일하지 않을 경우 그냥 넘긴다.
            C = ''
    print('#{} {}'.format(tc+1, count))
