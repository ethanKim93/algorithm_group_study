import sys
sys.stdin = open('sample_input.txt')

def pa(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return pa(n-1) + 2*(pa(n-2))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = pa(N//10)

    print("#{} {}".format(tc, result))