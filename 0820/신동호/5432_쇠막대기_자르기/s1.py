import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    irons = list(input())
    stack = []
    result = 0
    cnt = 0
    for i in range(len(irons)):
        if irons[i] == '(':
            cnt += 1
        elif irons[i-1] == '(':
            cnt -= 1
            result += cnt
        else:
            result += 1
            cnt -= 1
    print('#{} {}'.format(tc, result))