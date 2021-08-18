import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1 = list(set(str1))
    N, M = len(str1), len(str2)
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if str1[i] == str2[j]:
                cnt += 1
        if result < cnt:
            result = cnt

    print('#{} {}'.format(tc, result))