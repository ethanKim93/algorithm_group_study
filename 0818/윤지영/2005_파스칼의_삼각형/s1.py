import sys
sys.stdin = open("input.txt")

T = int(input())
stack = [0]*10
stack[0] = 1
stack[1] = 1


def pascal(n):
    i = 1
    stack_1 = stack.copy()
    while i < n:
        for k in range(i):
            stack[k] = stack_1[k-1] + stack_1[k]
            stack[k+1] = 1
        print(' '.join(map(str, stack[:k+2])))
        stack_1 = stack.copy()
        i += 1
    return


for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    print(' '.join(map(str, stack[:1])))
    pascal(N)
