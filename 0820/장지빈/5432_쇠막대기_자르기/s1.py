import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A = input()
    stick = i = cnt = 0
    while i < len(A):

        if A[i] == '(' and A[i+1] == ')':
            cnt += stick
            i += 2

        elif A[i] == '(':
            stick += 1
            i += 1

        else:
            cnt += 1
            stick -= 1
            i += 1

    print('#{} {}'.format(tc, cnt))
