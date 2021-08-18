import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    idx = [0]*N

    for one in range(N):
        cnt = 0
        for two in str2:
            if str1[one] == two:
                cnt += 1
            idx[one] = cnt
    big = 0
    for i in range(N):
        if idx[i] > big:
            big = idx[i]
    print('#{} {}'.format(tc, big))