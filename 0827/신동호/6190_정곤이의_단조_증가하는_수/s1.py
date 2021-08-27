import sys
sys.stdin = open('s_input.txt')

def up(num):
    nu = num
    one = nu%10
    while nu:
        nu //= 10
        if one < nu % 10:
            return -1
        one = nu % 10
    return num


def check():
    global result
    for i in range(N-1):
        if result > A[i] * A[i+1]:
            return result
        for j in range(i+1, N):
            if result > A[i] * A[j]:
                break
            if result < up(A[i] * A[j]):
                result = up(A[i] * A[j])
    return result




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    used = [0] * (N+1)
    A.sort(reverse=True)
    result = -1
    print('#{} {}'.format(tc, check()))
