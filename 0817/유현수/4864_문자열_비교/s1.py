import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)

    i = 0
    j = 0
    while i < N and j < M:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == N:
        result = 1
    else:
        result = 0


    print('#{} {}'.format(tc, result))
