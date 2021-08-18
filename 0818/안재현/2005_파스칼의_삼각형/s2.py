import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(0, T):
    N = int(input())
    print('#{}'.format(tc+1))
    empty = ''
    cnt = 0
    for i in range(N):
        # print(N)
        if cnt <= N:
            if i + 1 != N:
                empty = empty + str(i + 1 - 1) + ' '
                cnt += 1
            elif i + 1 == N:
                empty = empty + str(i + 1 - 1) + ' '
                cnt += 1
        elif cnt > N:
            if i - 1 != 1:
                empty = empty + str(i - cnt - 1) + ' '
                cnt += 1
            elif i - 1 == 1:
                empty = empty + str(i - cnt - 1) + ' '
                cnt += 1
                break
        print(empty)

