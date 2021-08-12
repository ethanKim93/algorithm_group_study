import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binary_check(P, X):
    st = 1
    end = P
    cnt = 0
    while st <= end:
        cnt += 1
        mid = (st+end)
        if mid//2 == X:
            break
        elif mid//2 > X:
            end = mid//2
        else:
            st = mid//2
    return cnt


for tc in range(1,T+1):
    P, A, B = list(map(int, input().split()))
    if binary_check(P, A) == binary_check(P, B):
        winner = 0
    elif binary_check(P, A) > binary_check(P, B):
        winner = 'B'
    else:
        winner = 'A'
    print('#{} {}'.format(tc, winner))