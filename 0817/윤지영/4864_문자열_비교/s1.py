import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N,M = len(str1), len(str2)
    for i in range(M):
        if str1 in str2:
            result = 1
        else:
            result = 0
    print('#{} {}'.format(tc, result))